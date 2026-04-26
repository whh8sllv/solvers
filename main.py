import random
import time

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
        start_time = time.time()
        res = []
        for r in range(self.n):
            delta_r = (self.W).bit_count() - ((self.W - ((2**r * self.F) % self.GM)) % self.GM).bit_count()
            if (r >= (self.n - self.m)) and (0 < delta_r <= (self.h + r - self.n + self.m)):
                res.append('1')
            elif (r < (self.n - self.m)) and (0 < delta_r <= self.h):
                res.append('1')
            else:
                res.append('0')
        end_time = time.time()
        return res[::-1], abs(start_time - end_time)

# solve_new = Solver1(1279, 512, 17)
# x = bin(solve_new.x)[2:]
# x_true = [i for i in x]
# test = []
# for i in range(len(x_true)):
#     if x_true[i] == '1':
#         test.append(i)

# tt1 = solve_new.recover_x()
# print(test)
# print(tt1.count('1'))
# test2 = []
# for i in range(len(tt1)):
#     if tt1[i] == '1':
#         test2.append(i)
# print(test2)

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
            # print(delta_r)
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
    
# solve3 = Solver2_MI2(128, 72, 10)
# x = bin(solve3.x)[2:]
# x_true = [i for i in x]
# print(x_true)
# x_recovered = solve3.recover_x()
# print(x_recovered)
# print(x_recovered.count('1'))  

class Solver3():

    def __init__(self, n, m, h, epsilon):
        self.n = n
        self.m = m
        self.h = h
        self.GM = get_module(self.n, self.m)
        self.F = bin_list_to_number(generate_number(self.n, self.h))
        self.G = bin_list_to_number(generate_number(self.n, self.h))
        self.x = bin_list_to_number(generate_number(self.n, self.h))
        self.y = bin_list_to_number(generate_number(self.n, self.h))
        self.W = calculate_w(self.F, self.G, self.x, self.y, self.GM)
        self.epsilon = epsilon

    def recover_x(self):
        recovered_res = []
        for r in range(self.n):
            d = (self.W - ((2**r * self.F) % self.GM)) % self.GM
            ham_d = d.bit_count()
            delta_r = (self.W).bit_count() - ham_d
            wt_r = ((2**r * self.F) % self.GM).bit_count()
            res = abs(delta_r - wt_r)
            # print(res)
            if res <= self.epsilon:
                recovered_res.append('1')
            else:
                recovered_res.append('0')
        return recovered_res
    
# solve4 = Solver3(128, 72, 10, 10)
# x = bin(solve4.x)[2:]
# x_true = [i for i in x]
# print(x_true)
# x_recovered = solve4.recover_x()
# print(x_recovered)
# print(x_recovered.count('1'))

class Solver4_modified():

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
        start_time = time.time()
        counter = self.W
        i_list, j_list = [], []
        a = ['0'] * self.n
        b = ['0'] * self.n
        iterator = 0
        while (a.count('1') + b.count('1') < 2*self.h) and iterator < 2 * self.n:
            # print(iterator)
            # i for F
            m_i = None
            need_i = None
            for i in range(self.n):
                if i in i_list:
                    continue
                delta_i = counter.bit_count() - ((counter - 2**i * self.F) % self.GM).bit_count()
                if m_i is None or m_i <= delta_i:
                    m_i = delta_i
                    need_i = i
            # j for G
            m_j = None
            need_j = None
            for j in range(self.n):
                if j in j_list:
                    continue
                delta_j = counter.bit_count() - ((counter - 2**j * self.G) % self.GM).bit_count()
                if m_j is None or m_j <= delta_j:
                    m_j = delta_j
                    need_j = j
            if m_i > m_j:
                if a.count('1') == self.h:
                    i_list.append(need_i)
                else:    
                    counter = (counter - 2**need_i * self.F) % self.GM
                    a[need_i] = '1'
                    i_list.append(need_i)
            elif m_j > m_i:
                if b.count('1') == self.h:
                    j_list.append(j)
                else:
                    counter = (counter - 2**need_j * self.G) % self.GM
                    b[need_j] = '1'
                    j_list.append(need_j)
            else:
                z = random.choice(['i', 'j'])
                if z == 'i':
                    if a.count('1') == self.h:
                        i_list.append(need_i)
                    else:
                        counter = (counter - 2**need_i * self.F) % self.GM
                        a[need_i] = '1'
                        i_list.append(need_i)
                else:
                    if b.count('1') == self.h:
                        j_list.append(j)
                    else:
                        counter = (counter - 2**need_j * self.G) % self.GM
                        b[need_j] = '1'
                        j_list.append(need_j)
            iterator += 1
        end_time = time.time()
        return a[::-1], b[::-1], end_time - start_time

# solve_new = Solver4_modified(1279, 512, 17)
# x = bin(solve_new.x)[2:]
# x_true = [i for i in x]
# test = []
# for i in range(len(x_true)):
#     if x_true[i] == '1':
#         test.append(i)

# print()

# tt1 = solve_new.recover_x()
# print(test)
# print(tt1[0].count('1'))
# test2 = []
# for i in range(len(tt1[0])):
#     if tt1[0][i] == '1':
#         test2.append(i)
# print(test2)
# y = bin(solve_new.y)[2:]
# y_true = [i for i in y]
# testy = []
# for i in range(len(y_true)):
#     if y_true[i] == '1':
#         testy.append(i)
# print(testy)
# print('***')
# print(tt1[1].count('1'))
# test3 = []
# for i in range(len(tt1[1])):
#     if tt1[1][i] == '1':
#         test3.append(i)
# print(test3)



class Solver4():

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
        start_time = time.time()
        counter = self.W
        i_list, j_list = [], []
        a = ['0'] * self.n
        b = ['0'] * self.n
        iterator = 0
        while a.count('1') + b.count('1') < 2*self.h and iterator < 2 * self.n:
            m_i = None
            need_i = None
            for i in range(self.n):
                if i in i_list:
                    continue
                delta_i = counter.bit_count() - ((counter - 2**i * self.F) % self.GM).bit_count()
                if m_i is None or m_i <= delta_i:
                    m_i = delta_i
                    need_i = i
            m_j = None
            need_j = None
            for j in range(self.n):
                if j in j_list:
                    continue
                delta_j = counter.bit_count() - ((counter - 2**j * self.G) % self.GM).bit_count()
                if m_j is None or m_j <= delta_j:
                    m_j = delta_j
                    need_j = j
            if m_i > m_j:
                counter = (counter - 2**need_i * self.F) % self.GM
                a[need_i] = '1'
                i_list.append(need_i)
            elif m_j > m_i:
                counter = (counter - 2**need_j * self.G) % self.GM
                b[need_j] = '1'
                j_list.append(need_j)
            else:
                z = random.choice(['i', 'j'])
                if z == 'i':
                    counter = (counter - 2**need_i * self.F) % self.GM
                    a[need_i] = '1'
                    i_list.append(need_i)
                else:
                    counter = (counter - 2**need_j * self.G) % self.GM
                    b[need_j] = '1'
                    j_list.append(need_j)
            iterator += 1
        end_time = time.time()
        return a[::-1], b[::-1], end_time - start_time



# solve_new = Solver4(1279, 512, 17)
# x = bin(solve_new.x)[2:]
# x_true = [i for i in x]
# test = []
# for i in range(len(x_true)):
#     if x_true[i] == '1':
#         test.append(i)

# print()

# tt1 = solve_new.recover_x()
# print(test)
# print(tt1[0].count('1'))
# test2 = []
# for i in range(len(tt1[0])):
#     if tt1[0][i] == '1':
#         test2.append(i)
# print(test2)
# y = bin(solve_new.y)[2:]
# y_true = [i for i in y]
# testy = []
# for i in range(len(y_true)):
#     if y_true[i] == '1':
#         testy.append(i)
# print(testy)
# print('***')
# print(tt1[1].count('1'))
# test3 = []
# for i in range(len(tt1[1])):
#     if tt1[1][i] == '1':
#         test3.append(i)
# print(test3)