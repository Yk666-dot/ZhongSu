import random


def random_num(num):
    i = 1
    lis = []
    while i <= num:
        lis.append(str(random.randint(0, 9)))
        i += 1
    return ''.join(lis)