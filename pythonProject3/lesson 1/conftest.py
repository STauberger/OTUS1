class Employee:
    def __init__(self, name: str, selary: int):
        self.name = name
        self.selary = selary
    @staticmethod
    def print_me():
      print ('GGGGGG')
    def employee_info (self):
        print (f'Name{self.name},{self.selary}')
        self.print_me()

print(Employee)
alice = Employee('Alice', 1000)
alice.employee_info()
print(alice)
bob = Employee('Bob', 5000)
bob.employee_info()
bob.selary = 6000
bob.employee_info()
print(bob)
print(id(alice),id(bob))