#from abc import ABC
class Computer():
    @classmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running")


L = Laptop()
L.process()