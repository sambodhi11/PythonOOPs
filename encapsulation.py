class Employee:
    def __init__(self, name, salary, project):
        self.name = name
        self._salary = salary
        self.__project = project

    def display(self):
      print("Name:", self.name)
      print('Salary:', self._salary)
        
    def set(self):
        print(self.name, 'is working on', self.__project)
emp = Employee('Sambodhi', 10000, 'Django')

emp.display()  
emp.set()  
#print("name:", emp.name)
#print("Salary:", emp._salary)
#print("Project:", emp._Employee__project) 