def create_namedtuple(**fields):
    def constructor(*args):
        if len(args) != len(fields):
            raise TypeError(f'{len(fields)} argument(s) required, but {len(args)} provided')
        return {field: arg for field, arg in zip(fields.keys(), args)}
    return constructor

def replace_namedtuple(namedtuple, field, value):
    if field not in namedtuple:
        raise ValueError(f'{field} is not a valid field for this namedtuple')
    return {**namedtuple, **{field: value}}

def get_namedtuple(namedtuple, field):
    if field not in namedtuple:
        raise ValueError(f'{field} is not a valid field for this namedtuple')
    return namedtuple[field]



if __name__ == "__main__":
    Person = create_namedtuple(name='', age=0)
    p1 = Person('Иван', 20)
    p2 = replace_namedtuple(replace_namedtuple(p1, 'name', 'Алексей'), 'age', 21)
    print(get_namedtuple(p1, 'name'), get_namedtuple(p1, 'age'))
    print(get_namedtuple(p2, 'name'), get_namedtuple(p2, 'age'))