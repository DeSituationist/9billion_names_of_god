class ListInstance:
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t{attribute}={value}\n'.format(attribute=attr, value=self.__dict__[attr])
        return result
    def __str__(self):
        return '<Instance of {class_name}, address {address} : {ls_of_names_values}>'.format(class_name = self.__class__.__name__,
                                                                                             address = id(self),
                                                                                             ls_of_names_values = self.__attrnames())
if __name__ == '__main__':
    class Spam(ListInstance):
        def __init__(self) : self.data1 = 'food'
    x = Spam()
    print(x)