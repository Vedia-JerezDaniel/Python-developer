class Singleton(object):
        _instance = None

        def __new__(cls, *args, **kwargs):
            if Singleton._instance is None:
                Singleton._instance = object.__new__(cls)

            return Singleton._instance



s1 = Singleton()
s2 = Singleton()

print(s1 is s2)


s1.x = 100
print(s2.x)

s2.x = 200
print(s1.x)

s1.y = 300
print(s1.y)