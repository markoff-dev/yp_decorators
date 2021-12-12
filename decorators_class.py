class A:

    def a(self):
        return id(self)

    @classmethod
    def b(cls):
        return id(cls)

    @staticmethod
    def c():
        return 'c'

    @property
    def d(self):
        return "d"

    # @property
    # def is_yang(self):
    #     return self.age < 18


obj_a = A()
print('ID класса А =', id(A))
print('ID объекта obj_a (экземпляра класса А) =', id(obj_a))
# print('ID self =', obj_a.a())
# print('ID cls =', obj_a.b())
# print('staticmethod =', obj_a.c())
# print('property =', obj_a.d)
