import os
import sys
import time
import signal
from heapq import *
from input_reader import Input_Reader
from task import Task
from collections import deque

class Normal(object):
    """Classe que representa um escalonador de prioridade não-preemptivo.
    Ele recebe uma lista de tasks, e define sua função de prioridade
    como a própria prioridade do processo"""

    def __init__(self, tasks):
        # Ordena os processos baseado em suas prioridades
        self.tasks = deque(sorted(tasks, key=lambda x: x.priority,reverse=True))

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

    # Mata um processo
    def kill_task(self, child):
        os.kill(child, signal.SIGKILL)

    def run(self):
        while(self.tasks):
            task = self.get_task(self.tasks[0].id)
            taskId = self.start_task(task)
            print('Processo escalonador de pid %s iniciou o processo filho %s com prioridade %s de pid %s.' % (str(os.getpid()), str(task.id), str(task.priority), str(taskId)))
            time.sleep(task.timeleft)
            self.kill_task(taskId)
            print('Processo escalonador de pid %s matou o processo filho %s de pid %s.\n' % (str(os.getpid()), str(task.id), str(taskId)))
            self.tasks.popleft()
