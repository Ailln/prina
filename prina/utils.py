import inspect


def prina(*args):
    result_list = []
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    for arg in args:
        flag = True
        for key, value in callers_local_vars:
            if value is arg:
                result_list.append(key + ": " + str(value))
                flag = False

        if flag:
            result_list.append(str(arg))

    result = " ".join(result_list)
    print(result)
    return result
