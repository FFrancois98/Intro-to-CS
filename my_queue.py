class MyQueue:
    def __init__(self):
        self.values = []
    def add(self, value):
        self.values.append(value)

    def remove(self):
        self.values.pop(0)

    def print_values(self):
        print(self.values)

my_queue = MyQueue()
my_queue.add(5)
my_queue.add('pizza')
my_queue.add(False)
my_queue.add('sunshine')
my_queue.print_values()
my_queue.remove()
my_queue.print_values()
my_queue.add(42)
my_queue.remove()
my_queue.print_values()
