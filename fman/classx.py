# Datatype classes

class Docs:
    '''To set docs string.'''

    def __init__(self, string: str = None):
        self.string = string

    def __str__(self):
        return self.string


class Version:
    '''To set version string.'''

    def __init__(self, string: str = None):
        self.string = string

    def __str__(self):
        return self.string


class Author:
    '''To set author string.'''

    def __init__(self, string: str = None):
        self.string = string

    def __str__(self):
        return self.string


class Dev_Status:
    '''To set development status string.'''

    def __init__(self, string: str = None):
        self.string = string

    def __str__(self):
        return self.string


#a = Author('Almas Ali')

# print(type(a))


class ClassExplore:
    '''Learn more about Python class and you can create new magic method here.'''

    def __init__(self, cls: any):
        self.cls = cls

    def __version__(self):
        '''Version string.'''
        return '1.0.0'

    def __author__(self):
        '''Author string.'''
        return 'Md. Almas Ali'

    def __dev_status__(self):
        return f'{self.version()} alpha'

    def docs(self):
        '''To get docs string.'''
        try:
            return Docs(self.cls.__doc__)
        except AttributeError:
            raise AttributeError('docs string not found !')

    def version(self):
        '''To get version string.'''
        try:
            return Version(self.cls.__version__(self))
        except AttributeError:
            raise AttributeError('version string not found !')

    def author(self):
        '''To get author name string.'''
        try:
            return Author(self.cls.__author__(self))
        except AttributeError:
            raise AttributeError('author name string not found !')

    def dev_status(self):
        '''To get development status string.'''
        try:
            return Dev_Status(self.cls.__dev_status__(self))
        except AttributeError:
            raise AttributeError('development status string not found !')


# c = ClassExplore(ClassExplore)

# #print(c.docs())
# #print(c.version())
# #print(c.author())
# print(type(c.dev_status()))
