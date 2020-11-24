import gc


def first_function(a=3, b=5):
    c = a + b
    return c


print(first_function(1, 2))
print(first_function())

gc.collect()
