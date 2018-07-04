
def inputLog(debug):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(func.__name__, args[1:])
            return func(*args, **kwargs)

        if debug:
            return wrapper
        else:
            return func
    return decorator

def outputLog(debug):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(func.__name__, result)
            return result

        if debug:
            return wrapper
        else:
            return func
    return decorator

def DebugSetting():
    return {
        'Queue' : False,
        'Graph' : False,
        'Dijkstra' : True,
        'BinaryTree' : True
    }