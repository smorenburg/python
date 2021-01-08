def square(num):
    return num * num


def square_lambda(num):
    return num * num


assert square(4) == square_lambda(4)
