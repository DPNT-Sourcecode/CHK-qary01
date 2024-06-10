# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    raise ValueError("Both inputs must be integers")
