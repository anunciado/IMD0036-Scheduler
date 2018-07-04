import csv
import sys

"""Leitor de inputs"""
class Input_Reader():
    def __init__(self, file):
        self.file = file

    def run(self):
        r = []
        try:
            reader = csv.reader(self.file)
            for row in reader:
                r.append(row)
        finally:
            self.file.close()
            r = [[int(j) for j in i] for i in r]
            return r
