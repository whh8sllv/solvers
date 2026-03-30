import random

def generate_number(n, h):
    num = []
    for i in range(h-1):
        num.append('1')
    for j in range(n-h):
        num.append('0')
    random.shuffle(num)
    res = ['1'] + num
    return res

def bin_list_to_number(binary_list):
    binary_string = ''.join(binary_list)
    return int(binary_string, 2)

def get_module(n, m):
    return 2**n - 2**m - 1

def calculate_w(F, G, x, y, module):
    W = (F*x + G*y) % module
    return W

# F = bin_list_to_number(generate_number(256, 10))
# G = bin_list_to_number(generate_number(256, 10))
# x = bin_list_to_number(generate_number(256, 10))
# y = bin_list_to_number(generate_number(256, 10))

# print(F)
# print(len(bin(F)[2:]))
# print(bin(F)[2:].count('1'))
# print(bin(F)[2:].count('0'))

class Solver1():

    def __init__(self, n, m, h):
        self.n = n
        self.m = m
        self.h = h
        self.GM = get_module(self.n, self.m)
        self.F = bin_list_to_number(generate_number(self.n, self.h))
        self.G = bin_list_to_number(generate_number(self.n, self.h))
        self.x = bin_list_to_number(generate_number(self.n, self.h))
        self.y = bin_list_to_number(generate_number(self.n, self.h))
        self.W = calculate_w(self.F, self.G, self.x, self.y, self.GM)
    
    def recover_x(self):
        res = []
        for r in range(self.n):
            delta_r = (self.W).bit_count() - ((self.W - ((2**r * self.F) % self.GM)) % self.GM).bit_count()
            if (r >= (self.n - self.m)) and (0 < delta_r <= (self.h + r - self.n + self.m)):
                res.append('1')
            elif (r < (self.n - self.m)) and (0 < delta_r <= self.h):
                res.append('1')
            else:
                res.append('0')
        return res

solve1 = Solver1(128, 72, 10)
x = bin(solve1.x)[2:]
x_true = [i for i in x]
print(x_true)
x_recovered = solve1.recover_x()
print(x_recovered)
print(x_recovered.count('1'))