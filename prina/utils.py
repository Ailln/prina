import inspect


def prina(*args):
    result = {}
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    for arg in args:
        for key, value in callers_local_vars:
            if value is arg:
                result[key] = value

    print(result)
