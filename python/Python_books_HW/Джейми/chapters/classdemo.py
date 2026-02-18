class Staff:
    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print('creating staff object')
    def __str__(self):
        return 'Position = {}, Name = {}, Pay = {}'.format(self._position, self.name, self.pay)
    def calculatePay(self):
        prompt = 'Enter number of hours worked for %s: '%(self.name)
        hours = input(prompt)
        prompt = 'Enter hourly rate for %s: '%(self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay
officeStaff1 = Staff('Basic', 'Yvonne', 0)
print(officeStaff1.name)
print(officeStaff1._position)
officeStaff1._position = 'Manger'
print(officeStaff1._position)
#officeStaff1.calculatePay()
print(officeStaff1.pay)
print(officeStaff1)
print('-'*20 + 'Part two' + '-'*20)
class Staff:
    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print('creating staff object')
    def __str__(self):
        return 'Position = {}, Name = {}, Pay = {}'.format(self._position, self.name, self.pay)
    def calculatePay(self):
        prompt = 'Enter number of hours worked for %s: '%(self.name)
        hours = input(prompt)
        prompt = 'Enter hourly rate for %s: '%(self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay
    @property
    def position(self):
        print('Getter Method')
        return self._position
    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            print('Setter called')
            self._position = value
        else:
            print('Position is invalid. No changes made')
officeStaff1 = Staff('Basic', 'Yvonne', 0)
print(officeStaff1.position)
officeStaff1.position = 'Manager'
print(officeStaff1.position)
officeStaff1.position = 'CEO'
print(officeStaff1.position)
print('-'*20 + 'Корректировка имен' + '-'*20)
class A:
    def __init__(self):
        self.__x = 5
        self._y = 6
varA = A()
print(varA._y)
print(varA._A__x)
class ManagmentStaff(Staff):
    def __init__(self, pName, pPay, pAllowance, pBonus):
        super().__init__('Manager', pName, pPay)
        self.allowance = pAllowance
        self.bonus = pBonus
    def calculatePay(self):
        basicPay = super().calculatePay()
        self.pay = basicPay + self.allowance
        return self.pay
    def calculatePerfBonus(self):
        prompt = 'Enter performance grade for %s' %(self.name)
        grade = input(prompt)
        if(grade == 'A'):
            self.bonus = 1000
        else:
            self.bonus = 0
        return self.bonus
    def __add__(self, other):
        return self.pay + other.pay
class BasicStaff(Staff):
    def __init__(self, pName, pPay):
        super().__init__('Basic', pName, pPay)
    