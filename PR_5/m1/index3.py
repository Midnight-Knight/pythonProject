class RaisesContext:
    def __init__(self, expected_exception):
        self.expected_exception = expected_exception
        self.actual_exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            raise AssertionError(f"{self.expected_exception.__name__} not raised")

        if not issubclass(exc_type, self.expected_exception):
            return False

        self.actual_exception = exc_value
        return True


def raises(expected_exception):
    return RaisesContext(expected_exception)

if __name__ == "__main__":
    with raises(ValueError) as e:
        raise ValueError("oops")

    assert isinstance(e.actual_exception, ValueError)
    assert str(e.actual_exception) == "oops"