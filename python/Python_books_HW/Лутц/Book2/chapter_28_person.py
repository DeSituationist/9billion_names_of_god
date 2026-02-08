class Person:
    def __init__(self, name, pay=0, job=''):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self) : return self.name.split()[-1]
    def giveRaise(self, percent) : self.pay = int(self.pay * (1 + percent))
    def __str__(self) : return 'Person\'s name: {name}. He has a pay of {pay} dollars. His position in company is: {job}'.format(name=self.name, job=self.job, pay=self.pay)
class Manager(Person):
    def __init__(self, name, pay) : Person.__init__(self, name, pay, job = 'mgr')
    def giveRaise(self, percent, bonus=.10): Person.giveRaise(self, percent + bonus)
class Department:
    def __init__(self, *args) : self.members = list(args)
    def addMember(self, person) : self.members.append(person)
    def giveRaise(self, percent) : 
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self): 
        for person in self.members:
            print(person)
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Johnes', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName())
    print('Sue has a pay of {pay} dollars'.format(pay=round(sue.pay)))
    tom = Manager('Tom Johnes', 50000)
    print(tom.lastName())
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaise(.1)
    development.showAll()