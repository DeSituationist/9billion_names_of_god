class AgeDesc:
    def __get__(self, instance, owner) : return 40
    def __set__(self, instance, value) : instance._age = value
class descriptors:
    age = AgeDesc()
x = descriptors()
print(x.age) # AgeDesc.__get__
x.age = 42 #AgeDec.__set__
print(x._age)