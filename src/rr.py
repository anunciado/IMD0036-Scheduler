import os
import sys
import time
import signal
from heapq import *
from input_reader import Input_Reader
from task import Task
from collections import deque

class RR(object):
    """Classe que representa um algoritmo de escalonamento Round Robin. Esse algoritmo
    define uma fatia de tempo para a execução de cada processo. Caso um processo não termine
    a execução durante a fatia, ele é recolocado no final da fila de espera"""
    def __init__(self, tasks):
        self.tasks = list(sorted(tasks, key=lambda x: x.priority,reverse=True))
        self.pids = list([0] * len(tasks))
        self.quantumValue = 0

    def quantum(self):
        self.quantumValue = 9/len(self.tasks)
        for task in self.tasks:
            task.quantum = self.quantumValue

    # Retorna uma referẽncia para o processo a ser executado baseado no id
    def get_task(self, id_):
        for task in self.tasks:
            if task.id == id_:
                return task
        return None

    # Inicia um processo
    def start_task(self, task_):
        for task in self.tasks:
            if task == task_:
                child = os.fork()
                if child == 0:
                    task.run()
                    sys.exit(0)
                else:
                    return child
        return -1

    # Para um processo
    def stop_task(self, child):
        os.kill(child, signal.SIGSTOP)

    # Recomeça um processo
    def cont_task(self, child):
        os.kill(child, signal.SIGCONT)

    # Mata um processo
    def kill_task(self, child):
        os.kill(child, signal.SIGKILL)

    def run(self):
        aux = 0
        while(self.tasks):
            self.quantum()
            task = self.get_task(self.tasks[aux%len(self.tasks)].id)
            task.timeleft -= self.quantumValue
            if(aux < len(self.tasks)):
                taskId = self.start_task(task)
                self.pids[aux] = taskId
                print('Processo escalonador de pid %s iniciou o processo filho %s com prioridade %s de pid %s.' % (str(os.getpid()), str(task.id), str(task.priority), str(taskId)))
                time.sleep(self.quantumValue)
            else:
                taskId = self.pids[aux%len(self.tasks)]
                self.cont_task(taskId)
                print('Processo escalonador de pid %s retomou o processo filho %s com prioridade %s de pid %s.' % (str(os.getpid()), str(task.id), str(task.priority), str(taskId)))
                time.sleep(self.quantumValue)
            if(task.timeleft <= 0):
                self.kill_task(taskId)
                print('Processo escalonador de pid %s matou o processo filho %s de pid %s.\n' % (str(os.getpid()), str(task.id), str(taskId)))
                self.tasks.remove(task)
                self.pids.remove(taskId)
                aux -= 1
            else:
                self.stop_task(taskId)
                print('Processo escalonador de pid %s parou o processo filho %s de pid %s.\n' % (str(os.getpid()), str(task.id), str(taskId)))
            aux += 1
