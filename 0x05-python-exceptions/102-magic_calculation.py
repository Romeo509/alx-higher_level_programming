#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except SomeSpecificException:
            # Handle SomeSpecificException
            pass
        except AnotherSpecificException:
            # Handle AnotherSpecificException
            pass
        except Exception as e:
            # Handle other exceptions
            result = b + a
            break
    return result
