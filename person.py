

class Person:
    def __init__(self, name, job=None, pay=0 ):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay*(1+percent))

    def __str__(self):
        return '[Person:%s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent+bonus)

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        if not isinstance(person, Person):
            print("%s is not a right type" % person)
            return
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__=='__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=10000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(),sue.lastName())
    sue.giveRaise(0.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(0.10)
    print(tom.lastName())
    print(tom)
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()





