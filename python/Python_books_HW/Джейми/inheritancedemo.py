import classdemo as cd
peter = cd.BasicStaff('Peter', 0)
john = cd.ManagmentStaff('John', 0, 1000, 0)
print(peter)
print(john)
print('Peter\'s Pay = ', peter.calculatePay())
print('John\'s Pay = ', john.calculatePay())
print('John\'s Performance Bonus = ', john.calculatePerfBonus())
totalPay = john + peter
print('Total Pay for Both Staff =', totalPay)