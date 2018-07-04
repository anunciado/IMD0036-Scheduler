import os
import time

class Task():
    """Classe que representa um processo, e que guarda suas informações relevantes"""
    def __init__ (self, input_row):
        # id do processo criado
        self.id = input_row[0]
        # prioridade do processo que vai ser criado
        self.priority = input_row[1]
        # quantum calculado pela política de escalonamento atual
        self.quantum = input_row[2]
        # tempo de execução do processo criado
        self.burst = input_row[3]
        # tempo restante de execução do processo criado
        self.timeleft = self.burst

    # Executa sua função principal
    def run(self):
        while(self.burst != 0):
            print('Processo filho %s com prioridade %s de pid %s está rodando.' % (str(self.id), str(self.priority), str(os.getpid())))
            self.burst -= 1
            time.sleep(1)
