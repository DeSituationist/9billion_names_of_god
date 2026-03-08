n = 3
address = '221b Baker Street, NW1 6XE, London'
employee = {
    'age': 45,
    'role': 'CTO',
    'SSN': 'AB1234567',
}
# Области видимости
def local():
    age = 7
    print(age, 'printing from local scope')
age = 5
local()
print(age, 'printing from global scope')
def enclosing_func():
    age = 13
    def local():
        print(age, 'printing from local scope')
    local()
age = 5
print(age, 'printing from gloval scope')
enclosing_func()