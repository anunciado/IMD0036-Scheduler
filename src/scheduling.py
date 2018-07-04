import sys
from heapq import *
from input_reader import Input_Reader
from output_writer import Output_Writer
from scheduler_type import Scheduler_Type
from task import Task
from normal import Normal
from fifo import FIFO
from rr import RR

class Scheduler(object):

    def __init__(self, args):
        self.args = args
        self.tasks = []
        self.algorithm = None

    def set_scheduler_type(self):
        try:
            algorithm_name = self.args[2].lower()
        except IndexError:
            print ("Algoritmo não especificado\nFinalizando...")
            return -1
        if algorithm_name == "normal":
            self.algorithm = Normal(self.tasks)
            return 0
        elif algorithm_name == "fifo":
            self.algorithm = FIFO(self.tasks)
            return 0
        elif algorithm_name == "rr":
            self.algorithm = RR(self.tasks)
            return 0
        else:
            print ("Algoritmo não listado\nFinalizando...")
            return -1

    def run(self):
        try:
            file = open(self.args[1], 'rt')
        except IOError:
            print ("O arquivo de entrada não existe.\nFinalizando...")
            sys.exit()

        reader = Input_Reader(file)
        csv_list = reader.run()

        for row in csv_list:
            self.tasks.append(Task(row))

        if (self.set_scheduler_type() == -1):
            print ("Error")
        self.algorithm.run()

        #reporter = output_writer(self.args, self.tasks)
        #reporter.run()

if __name__ == "__main__":
     e = Scheduler(sys.argv)
     e.run()


# In[ ]:
