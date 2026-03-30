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

# solve1 = Solver1(128, 72, 10)
# x = bin(solve1.x)[2:]
# x_true = [i for i in x]
# print(x_true)
# x_recovered = solve1.recover_x()
# print(x_recovered)
# print(x_recovered.count('1'))

class Solver2_MI1():

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
    
    def calculate_MI(self, r):
        ham_i = []
        for i in range(self.n):
            if i == r:
                continue
            num1 = (2**r * self.F) % self.GM
            num2 = (2**i * self.F) % self.GM
            ham_i.append((num1 & num2).bit_count())
        sigma_F = max(ham_i)
        ham_j = []
        for j in range(self.n):
            num1 = (2**r * self.F) % self.GM
            num2 = (2**j * self.G) % self.GM
            ham_j.append((num1 & num2).bit_count())
        sigma_G = max(ham_j)
        return ((self.h - 1) * sigma_F + self.h * sigma_G)
    
    def get_lower_limit(self, r):
        MI = self.calculate_MI(r)
        wt_r = ((2**r * self.F) % self.GM).bit_count()
        return wt_r - MI

    def recover_x(self):
        res = []
        for r in range(self.n):
            delta_r = (self.W).bit_count() - ((self.W - ((2**r * self.F) % self.GM)) % self.GM).bit_count()
            print(delta_r)
            low_limit = self.get_lower_limit(r)
            # print(low_limit)
            if (r >= (self.n - self.m)) and (low_limit < delta_r <= (self.h + r - self.n + self.m)):
                res.append('1')
            elif (r < (self.n - self.m)) and (low_limit < delta_r <= self.h):
                res.append('1')
            else:
                res.append('0')
        return res

# solve2 = Solver2_MI1(128, 72, 10)
# x = bin(solve2.x)[2:]
# x_true = [i for i in x]
# print(x_true)
# x_recovered = solve2.recover_x()
# print(x_recovered)
# print(x_recovered.count('1'))    


class Solver2_MI2():

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
    
    def calculate_MI(self, r):
        ham_i = []
        for i in range(self.n):
            if i == r:
                continue
            num1 = (2**r * self.F) % self.GM
            num2 = (2**i * self.F) % self.GM
            ham_i.append((num1 & num2).bit_count())
        sigma_F = max(ham_i)
        ham_j = []
        for j in range(self.n):
            num1 = (2**r * self.F) % self.GM
            num2 = (2**j * self.G) % self.GM
            ham_j.append((num1 & num2).bit_count())
        sigma_G = max(ham_j)
        sigma_max = max(sigma_F, sigma_G)
        return (sigma_max * (2*self.h - 1))
    
    def get_lower_limit(self, r):
        MI = self.calculate_MI(r)
        wt_r = ((2**r * self.F) % self.GM).bit_count()
        return wt_r - MI

    def recover_x(self):
        res = []
        for r in range(self.n):
            delta_r = (self.W).bit_count() - ((self.W - ((2**r * self.F) % self.GM)) % self.GM).bit_count()
            # print(delta_r)
            low_limit = self.get_lower_limit(r)
            print(low_limit)
            if (r >= (self.n - self.m)) and (low_limit < delta_r <= (self.h + r - self.n + self.m)):
                res.append('1')
            elif (r < (self.n - self.m)) and (low_limit < delta_r <= self.h):
                res.append('1')
            else:
                res.append('0')
        return res
    
solve3 = Solver2_MI2(128, 72, 10)
x = bin(solve3.x)[2:]
x_true = [i for i in x]
print(x_true)
x_recovered = solve3.recover_x()
print(x_recovered)
print(x_recovered.count('1'))  