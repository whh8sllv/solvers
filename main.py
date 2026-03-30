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

F = bin_list_to_number(generate_number(256, 10))
G = bin_list_to_number(generate_number(256, 10))
x = bin_list_to_number(generate_number(256, 10))
y = bin_list_to_number(generate_number(256, 10))

print(F)
print(len(bin(F)[2:]))
print(bin(F)[2:].count('1'))
print(bin(F)[2:].count('0'))