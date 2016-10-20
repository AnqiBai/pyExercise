# -*- coding: utf-8 -*-

# 如果一个函数定义中包含yield关键字， 那这个函数就不是一个普通的函数，而是一个generator；


def triangles():
    i = [1]
    yield i
    while True:
        num = len(i)
        t_i = [1]
        index = 0
        while (index + 1) < num:
            t_i.append(i[index] + i[index + 1])
            index += 1
        t_i.append(1)
        i = t_i
        yield i


# expected output:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

test = triangles()

n = 0


for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
