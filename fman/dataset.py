class Dataset:
    '''Dataset is a custom datatype for global use case.'''

    def __init__(self, list: list = None):
        '''Dataset takes only a list of different values.'''
        if list == None:
            self.list = []
        self.list = list

    def push(self, value: any):
        '''To add a new value in dataset to end.'''
        return self.list.append(value)

    def insert(self, position: int = 0, value: any = ''):
        '''To insert a value in dataset in anywhere. As default it add in front.'''
        return self.list.insert(position, value)

    def pop(self):
        '''To remove last value of dataset.'''
        return self.list.pop()

    def peek(self, index: int):
        '''To get a value by its index number.'''
        return self.list[index]

    def remove(self, value: any):
        '''To remove a value from dataset.'''
        return self.list.remove(value)

    def find(self, value: any):
        '''To find any value in dataset.'''
        num = 0
        for l in self.list:
            if l == value:
                return num
            num += 1

    def count(self, value: any):
        '''To count any repeated value in dataset.'''
        return self.list.count(value)

    def sort(self):
        '''To sort the dataset.'''
        return self.list.sort()

    def reverse(self):
        '''To reverse dataset.'''
        return self.list.reverse()

    def clear(self):
        '''To clear dataset.'''
        return self.list.clear()

    def len(self):
        '''To get length of dataset.'''
        return len(self.list)

    def slice(self, start: int = None, end: int = None, jump: int = None):
        '''To slice dataset.'''
        return self.__return_value(self.list[start:end:jump])

    def __str__(self):
        '''To return dataset object.'''
        return f'<{str(self.list)[1:-1]}>'

    def __add__(self, value):
        '''To add dataset instances.'''
        return Dataset(self.list + str(value)[1:-1].replace('\'', '').split(','))

    def __getitem__(self, position):
        '''To get dataset iterate able and sliceable.'''
        return self.list[position]

    def __len__(self):
        '''To get len of dataset.'''
        return len(self.list)

    def __reversed__(self):
        '''To reversed the dataset instance.'''
        return self.list[::-1]

    def __repr__(self):
        '''To get representative string.'''
        return f'<{str(self.list)[1:-1]}>'

    def __cast(self, value):
        '''To cast dataset object to list. (Internal use only)'''
        return list(value[1:-1])

    @staticmethod
    def __return_value(value):
        '''To get dataset instance. (Internal use only)'''
        return f'<{str(value)[1:-1]}>'

    @staticmethod
    def __get_value(value):
        '''To get dataset value. (Internal use only)'''
        return f'{str(value)[1:-1]}'


v = Dataset(['Almas', 'Ali', '8262'])

v.push('pranto')

v.pop()

v.push('tom')

c = v.count('tom')

f = v.find('Ali')

p = v.peek(3)

v.sort()

v.reverse()

# v.clear()

#v = v.slice(1,2,4)

#v = v.__return_value()

#v = v+v+v+v

#v = v.len()


#v= Dataset()

# print(type(v))
# print(len(v))

# for b in v:
#	print(b)

# print(v[2])

# print(reversed(v))

print(v)
