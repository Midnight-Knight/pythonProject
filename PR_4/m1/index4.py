class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(A):
    pass

class E(C, D):
    pass

class F(E):
    pass

def get_inheritance(cls):
    return ' -> '.join(c.__name__ for c in cls.mro())

if __name__ == "__main__":
    print(get_inheritance(A))
    print(get_inheritance(B))
    print(get_inheritance(C))
    print(get_inheritance(D))
    print(get_inheritance(E))
    print(get_inheritance(F))
