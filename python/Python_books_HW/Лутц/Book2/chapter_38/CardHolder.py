print('-'*30 + 'EXAMPLE-1-properties' + '-'*30)
class CardHolder:
    acctlen = 8
    reitreage = 59.5
    def __init__(self, acct, name, age, addr):
        self._acct = acct
        self._name = name
        self._age =  age
        self._addr = addr
    def getName(self):
        return self._name
    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self._name = value
    name = property(getName, setName)
    def getAge(self):
        return self._age
    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('Invalid age')
        else:
            self._age = value
    age = property(getAge, setAge)
    def getAcct(self):
        return self._acct[:-3] + '***'
    def setAcct(self, value):
        if len(value) != self.acctlen:
            raise TypeError('invalid acct number')
        else:
            self._acct = value
    acct = property(getAcct, setAcct)
    def remainGet(self):
        return self.reitreage - self.age
    remain = property(remainGet)
    def __str__(self):
        return 'Name: {}, Age: {}, Acct: {}, Addr: {}'.format(self._name, self._age, self._acct, self._addr)
if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print(bob)
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    #bob.acct = '23-45-67-89'
    print(bob)
    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    print(sue)
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')  # Недопустимый возраст для sue
    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")  # Невозможно установить sue.remain
    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')  # Недопустимый номер счета для sue
print('-'*30 + 'EXAMPLE-2-descriptors-class-values' + '-'*30)
#Данные разделяются между всеми экземплярами класса, что является минусом
class CardHolder:
    acctlen = 8
    retireage = 59.5
    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age =  age
        self.addr = addr
    class Name:
        def __get__(self, instance, owner):
            return self.name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value
    name = Name()
    class Age:
        def __get__(self, instance, owner):
            return self.age
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value
    age = Age()
    class Acct:
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:
                raise TypeError('invalid acct number')
            else:
                self.acct = value
    acct = Acct()
    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age
        def __set__(self, instance, value):
            raise TypeError('cant set remain')
    remain = Remain()
    def __str__(self):
        return 'Name: {}, Age: {}, Acct: {}, Addr: {}'.format(self.name, self.age, self.acct, self.addr)
if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print(bob)
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    #bob.acct = '23-45-67-89'
    print(bob)
    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    print(sue)
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')  # Недопустимый возраст для sue
    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")  # Невозможно установить sue.remain
    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')  # Недопустимый номер счета для sue
print('-'*30 + 'EXAMPLE-2-instance-values' + '-'*30)
class CardHolder:
    acctlen = 8
    retireage = 59.5
    def __init__(self, acct, name, age, addr):
        self._acct = acct
        self._name = name
        self._age =  age
        self._addr = addr
    class Name:
        def __get__(self, instance, owner):
            return instance._name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            instance._name = value
    name = Name()
    class Age:
        def __get__(self, instance, owner):
            return instance._age
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                instance._age = value
    age = Age()
    class Acct:
        def __get__(self, instance, owner):
            return instance._acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:
                raise TypeError('invalid acct number')
            else:
                instance._acct = value
    acct = Acct()
    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age
        def __set__(self, instance, value):
            raise TypeError('cant set remain')
    remain = Remain()
    def __str__(self):
        return 'Name: {}, Age: {}, Acct: {}, Addr: {}'.format(self._name, self._age, self._acct, self._addr)
if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print(bob)
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    #bob.acct = '23-45-67-89'
    print(bob)
    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    print(sue)
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')  # Недопустимый возраст для sue
    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")  # Невозможно установить sue.remain
    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')  # Недопустимый номер счета для sue
print('-'*30 + 'EXAMPLE-2-getattr' + '-'*30)
class CardHolder:
    acctlen = 8
    retireage = 59.5
    def __init__(self, acct, name, age, addr):
        self._acct = acct
        self.name = name
        self.age = age
        self.addr = addr
    def __getattr__(self, name):
        if name == 'acct':
            return self._acct[:-3] + '***'
        elif name == 'remain':
            return self.retireage - self.age
        else:
            raise AttributeError(name)
    def __setattr__(self, name, value):
        if name == 'name':
            value = value.lower().replace(' ', '_')
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif name == 'remain':
            raise TypeError('cant set remain')
        self.__dict__[name] = value
    def __str__(self):
        return 'Name: {}, Age: {}, Acct: {}, Addr: {}'.format(self.name, self.age, self._acct, self.addr)
if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print(bob)
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    #bob.acct = '23-45-67-89'
    print(bob)
    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    print(sue)
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')  # Недопустимый возраст для sue
    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")  # Невозможно установить sue.remain
    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')  # Недопустимый номер счета для sue