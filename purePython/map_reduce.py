# -*- coding: utf-8 -*-

# map() 函数需要两个参数， 一个函数和一个Iterable对象；
# map 作为高阶函数， 事实上它把运算规则抽象了；

# reduce() 函数需要两个参数， 一个函数 f 和一个序列 [x1, x2, x3, x4];
# 具体的效果是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4);


def char2num(s):
    char_list = {'0': 0, '1': 1, '2': 2, '3': 3,
                 '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return char_list[s]


# 利用 map 函数， 将用户输入的不规范名字变成首字母大写， 其它小写的规范名字。

def normalize(name):
    firstChar = name[0]
    others = name[1:]
    return firstChar.upper() + others.lower()


# prod 求乘积的函数
def product(x, y):
    return x * y


def prod(L):
    return reduce(product, L)


# 利用 map 和 reduce 编写一个将字符串转换成浮点数的函数；


def str2int(s):
    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(char2num, s))


def str2decimal(s):
    count = len(s)
    number = str2int(s)
    return (number / (float(10) ** count))


def str2float(s):
    dp, fp = s.split('.')
    return str2int(dp) + str2decimal(fp)


# test normalize

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# test prod

print(3 * 5 * 7 * 9, ' = ', prod([3, 5, 7, 9]))

# test str2float

print('123,456', str2float('123.456'), type(str2float('123.456')))
