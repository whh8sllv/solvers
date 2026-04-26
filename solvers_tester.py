from main import *

# cases -- розмір вибірки

# def generate_sample(cases, n, m, h):
#     sample = []
#     for i in range(cases):
#         GM = get_module(n, m)
#         F = bin_list_to_number(generate_number(n, h))
#         G = bin_list_to_number(generate_number(n, h))
#         x = bin_list_to_number(generate_number(n, h))
#         y = bin_list_to_number(generate_number(n, h))
#         W = calculate_w(F, G, x, y, GM)
#         sample.append((n, m, h, GM, F, G, x, y, W))
#     return sample

# test_cases = generate_sample(10, 1279, 512, 17)

'''test #1: sample = 10, n = 1279, m = 512, h = 17'''

def get_input():
    # test_cases = generate_sample(10, 1279, 512, 17)
    print('Select type of solver that you want to be tested')
    print('1 --- Solver1 \n'
    '2 --- Solver2_MI1 \n'
    '3 --- Solver2_MI2 \n'
    '4 --- Solver3 \n'
    '5 --- Solver4 \n'
    '6 --- Solver4_modified')
    solver_number = int(input('Your choice is '))
    print('Add your input data')
    n = int(input('n = '))
    m = int(input('m = '))
    h = int(input('h = '))
    sample = int(input('sample size = '))
    if solver_number == 4:
        epsilon = int(input('epsilon = '))
        return solver_number, n, m, h, epsilon, sample
    return solver_number, n, m, h, sample

def equality_test(list1, list2):
    if list1 == list2:
        return 1
    else:
        return 0

def bit_accuracy_test(list1, list2):
    true_bits = sum(x_true == x_calculated for x_true, x_calculated in zip (list1, list2))
    return true_bits

def bit1_accuracy_test(list1, list2):
    true_bits1 = sum(x_true == x_calculated  == '1' for x_true, x_calculated in zip (list1, list2))
    return true_bits1

def bit0_accuracy_test(list1, list2):
    true_bits0 = sum(x_true == x_calculated  == '0' for x_true, x_calculated in zip (list1, list2))
    return true_bits0

def bit1_extra_test(list1, list2):
    extra_bits1 = sum((x_true == '0' and x_calculated == '1') for x_true, x_calculated in zip (list1, list2))
    return extra_bits1 / list2.count('1') if list2.count('1') != 0 else 0

def bit1_missing_test(list1, list2):
    missing_bits1 = sum((x_true == '1' and x_calculated == '0') for x_true, x_calculated in zip (list1, list2))
    return missing_bits1 / list1.count('1') if list1.count('1') != 0 else 0

def run_tests():
    input_data = get_input()

    if input_data[0] == 1:
        time_list, equality_list, bit_accuracy_list, ones_correct_list, zeros_correct_list, ones_extra_list, ones_missing_list = [], [], [], [], [], [], []
        for _ in range(input_data[4]):
            solver = Solver1(input_data[1], input_data[2], input_data[3])
            x = bin(solver.x)[2:].zfill(input_data[1])
            x_true = [i for i in x]
            res = solver.recover_x()
            x_solver = res[0]
            time = res[1]
            time_list.append(time)
            equality_list.append(equality_test(x_true, x_solver))
            bit_accuracy_list.append(bit_accuracy_test(x_true, x_solver))
            ones_correct_list.append(bit1_accuracy_test(x_true, x_solver))
            zeros_correct_list.append(bit0_accuracy_test(x_true, x_solver))
            ones_extra_list.append(bit1_extra_test(x_true, x_solver))
            ones_missing_list.append(bit1_missing_test(x_true, x_solver))
        avg_time = sum(time_list) / len(time_list)
        equality = sum(equality_list)
        success_probability = equality / input_data[4]
        avg_bit_accuracy = sum(bit_accuracy_list) / len(bit_accuracy_list)
        avg_ones_accuracy = sum(ones_correct_list) / len(ones_correct_list)
        avg_zeros_accuracy = sum(zeros_correct_list) / len(zeros_correct_list)
        avg_ones_extra = sum(ones_extra_list) / len(ones_extra_list)
        avg_ones_missing = sum(ones_missing_list) / len(ones_missing_list)
        return avg_time, equality, success_probability, avg_bit_accuracy, avg_ones_accuracy, avg_zeros_accuracy, avg_ones_extra, avg_ones_missing, input_data[1], input_data[3]

    
    if input_data[0] == 2:
        ...
    if input_data[0] == 3:
        ...
    if input_data[0] == 4:
        ...
    if input_data[0] == 5:
        equality_list_x, bit_accuracy_list_x, ones_correct_list_x, zeros_correct_list_x, ones_extra_list_x, ones_missing_list_x = [], [], [], [], [], []
        equality_list_y, bit_accuracy_list_y, ones_correct_list_y, zeros_correct_list_y, ones_extra_list_y, ones_missing_list_y = [], [], [], [], [], []
        time_list = []
        for _ in range(input_data[4]):
            solver = Solver4(input_data[1], input_data[2], input_data[3])
            x = bin(solver.x)[2:].zfill(input_data[1])
            y = bin(solver.y)[2:].zfill(input_data[1])
            x_true = [i for i in x]
            y_true = [i for i in y]
            res = solver.recover_x()
            x_solver, y_solver, time = res[0], res[1], res[2]
            time_list.append(time)
            equality_list_x.append(equality_test(x_true, x_solver))
            bit_accuracy_list_x.append(bit_accuracy_test(x_true, x_solver))
            ones_correct_list_x.append(bit1_accuracy_test(x_true, x_solver))
            zeros_correct_list_x.append(bit0_accuracy_test(x_true, x_solver))
            ones_extra_list_x.append(bit1_extra_test(x_true, x_solver))
            ones_missing_list_x.append(bit1_missing_test(x_true, x_solver))
            equality_list_y.append(equality_test(y_true, y_solver))
            bit_accuracy_list_y.append(bit_accuracy_test(y_true, y_solver))
            ones_correct_list_y.append(bit1_accuracy_test(y_true, y_solver))
            zeros_correct_list_y.append(bit0_accuracy_test(y_true, y_solver))
            ones_extra_list_y.append(bit1_extra_test(y_true, y_solver))
            ones_missing_list_y.append(bit1_missing_test(y_true, y_solver))
        avg_time = sum(time_list) / len(time_list)

        equality_x = sum(equality_list_x)
        success_probability_x = equality_x / input_data[4]
        avg_bit_accuracy_x = sum(bit_accuracy_list_x) / len(bit_accuracy_list_x)
        avg_ones_accuracy_x = sum(ones_correct_list_x) / len(ones_correct_list_x)
        avg_zeros_accuracy_x = sum(zeros_correct_list_x) / len(zeros_correct_list_x)
        avg_ones_extra_x = sum(ones_extra_list_x) / len(ones_extra_list_x)
        avg_ones_missing_x = sum(ones_missing_list_x) / len(ones_missing_list_x)
 
        equality_y = sum(equality_list_y)
        success_probability_y = equality_y / input_data[4]
        avg_bit_accuracy_y = sum(bit_accuracy_list_y) / len(bit_accuracy_list_y)
        avg_ones_accuracy_y = sum(ones_correct_list_y) / len(ones_correct_list_y)
        avg_zeros_accuracy_y = sum(zeros_correct_list_y) / len(zeros_correct_list_y)
        avg_ones_extra_y = sum(ones_extra_list_y) / len(ones_extra_list_y)
        avg_ones_missing_y = sum(ones_missing_list_y) / len(ones_missing_list_y)

        x_data = [equality_x, success_probability_x, avg_bit_accuracy_x, avg_ones_accuracy_x, avg_zeros_accuracy_x, avg_ones_extra_x, avg_ones_missing_x]
        y_data = [equality_y, success_probability_y, avg_bit_accuracy_y, avg_ones_accuracy_y, avg_zeros_accuracy_y, avg_ones_extra_y, avg_ones_missing_y]

        return avg_time, x_data, y_data, input_data[1], input_data[3]

    if input_data[0] == 6:
        equality_list_x, bit_accuracy_list_x, ones_correct_list_x, zeros_correct_list_x, ones_extra_list_x, ones_missing_list_x = [], [], [], [], [], []
        equality_list_y, bit_accuracy_list_y, ones_correct_list_y, zeros_correct_list_y, ones_extra_list_y, ones_missing_list_y = [], [], [], [], [], []
        time_list = []
        for _ in range(input_data[4]):
            solver = Solver4_modified(input_data[1], input_data[2], input_data[3])
            x = bin(solver.x)[2:].zfill(input_data[1])
            y = bin(solver.y)[2:].zfill(input_data[1])
            x_true = [i for i in x]
            y_true = [i for i in y]
            res = solver.recover_x()
            x_solver, y_solver, time = res[0], res[1], res[2]
            time_list.append(time)
            equality_list_x.append(equality_test(x_true, x_solver))
            bit_accuracy_list_x.append(bit_accuracy_test(x_true, x_solver))
            ones_correct_list_x.append(bit1_accuracy_test(x_true, x_solver))
            zeros_correct_list_x.append(bit0_accuracy_test(x_true, x_solver))
            ones_extra_list_x.append(bit1_extra_test(x_true, x_solver))
            ones_missing_list_x.append(bit1_missing_test(x_true, x_solver))
            equality_list_y.append(equality_test(y_true, y_solver))
            bit_accuracy_list_y.append(bit_accuracy_test(y_true, y_solver))
            ones_correct_list_y.append(bit1_accuracy_test(y_true, y_solver))
            zeros_correct_list_y.append(bit0_accuracy_test(y_true, y_solver))
            ones_extra_list_y.append(bit1_extra_test(y_true, y_solver))
            ones_missing_list_y.append(bit1_missing_test(y_true, y_solver))
        avg_time = sum(time_list) / len(time_list)

        equality_x = sum(equality_list_x)
        success_probability_x = equality_x / input_data[4]
        avg_bit_accuracy_x = sum(bit_accuracy_list_x) / len(bit_accuracy_list_x)
        avg_ones_accuracy_x = sum(ones_correct_list_x) / len(ones_correct_list_x)
        avg_zeros_accuracy_x = sum(zeros_correct_list_x) / len(zeros_correct_list_x)
        avg_ones_extra_x = sum(ones_extra_list_x) / len(ones_extra_list_x)
        avg_ones_missing_x = sum(ones_missing_list_x) / len(ones_missing_list_x)
 
        equality_y = sum(equality_list_y)
        success_probability_y = equality_y / input_data[4]
        avg_bit_accuracy_y = sum(bit_accuracy_list_y) / len(bit_accuracy_list_y)
        avg_ones_accuracy_y = sum(ones_correct_list_y) / len(ones_correct_list_y)
        avg_zeros_accuracy_y = sum(zeros_correct_list_y) / len(zeros_correct_list_y)
        avg_ones_extra_y = sum(ones_extra_list_y) / len(ones_extra_list_y)
        avg_ones_missing_y = sum(ones_missing_list_y) / len(ones_missing_list_y)

        x_data = [equality_x, success_probability_x, avg_bit_accuracy_x, avg_ones_accuracy_x, avg_zeros_accuracy_x, avg_ones_extra_x, avg_ones_missing_x]
        y_data = [equality_y, success_probability_y, avg_bit_accuracy_y, avg_ones_accuracy_y, avg_zeros_accuracy_y, avg_ones_extra_y, avg_ones_missing_y]

        return avg_time, x_data, y_data, input_data[1], input_data[3]

'''Solver 1'''
# tests = ['AVG time', 'Recovered numbers', 'Success probability', 'AVG bit accuracy', 'AVG bit 1 accuracy',
#          'AVG bit 0 accuracy', 'Fraction of extra bits 1', 'Fraction of missing bits 1']
# test1 = run_tests()
# for i in range(len(tests)):
#     if i == 3:
#         print(f'{tests[i]} by Solver#1: {test1[i]} bits from {test1[-2]} bits')
#     elif i == 4:
#         print(f'{tests[i]} by Solver#1: {test1[i]} bits from {test1[-1]} bits')        
#     elif i == 5:
#         print(f'{tests[i]} by Solver#1: {test1[i]} bits from {test1[-2] - test1[-1]} bits') 
#     else:
#         print(f'{tests[i]} by Solver#1: {test1[i]}')

'''Solver 4'''
# tests = ['Recovered numbers', 'Success probability', 'AVG bit accuracy', 'AVG bit 1 accuracy',
#          'AVG bit 0 accuracy', 'Fraction of extra bits 1', 'Fraction of missing bits 1']
# test5 = run_tests()
# x_data = test5[1]
# y_data = test5[2]
# print(f'AVG time by Solver#4: {test5[0]}')
# print()
# print('***recovering x report***')
# for i in range(len(tests)):
#     if i == 2:
#         print(f'{tests[i]} by Solver#4: {x_data[i]} bits from {test5[3]} bits')
#     elif i == 3:
#         print(f'{tests[i]} by Solver#4: {x_data[i]} bits from {test5[-1]} bits')        
#     elif i == 4:
#         print(f'{tests[i]} by Solver#4: {x_data[i]} bits from {test5[3] - test5[-1]} bits') 
#     else:
#         print(f'{tests[i]} by Solver#4: {x_data[i]}')
# print()
# print('***recovering y report***')
# for i in range(len(tests)):
#     if i == 2:
#         print(f'{tests[i]} by Solver#4: {y_data[i]} bits from {test5[3]} bits')
#     elif i == 3:
#         print(f'{tests[i]} by Solver#4: {y_data[i]} bits from {test5[-1]} bits')        
#     elif i == 4:
#         print(f'{tests[i]} by Solver#4: {y_data[i]} bits from {test5[3] - test5[-1]} bits') 
#     else:
#         print(f'{tests[i]} by Solver#4: {y_data[i]}')

'''Solver 4 modified'''
# tests = ['Recovered numbers', 'Success probability', 'AVG bit accuracy', 'AVG bit 1 accuracy',
#          'AVG bit 0 accuracy', 'Fraction of extra bits 1', 'Fraction of missing bits 1']
# test5 = run_tests()
# x_data = test5[1]
# y_data = test5[2]
# print(f'AVG time by Solver#4: {test5[0]}')
# print()
# print('***recovering x report***')
# for i in range(len(tests)):
#     if i == 2:
#         print(f'{tests[i]} by Solver#4: {x_data[i]} bits from {test5[3]} bits')
#     elif i == 3:
#         print(f'{tests[i]} by Solver#4: {x_data[i]} bits from {test5[-1]} bits')        
#     elif i == 4:
#         print(f'{tests[i]} by Solver#4: {x_data[i]} bits from {test5[3] - test5[-1]} bits') 
#     else:
#         print(f'{tests[i]} by Solver#4: {x_data[i]}')
# print()
# print('***recovering y report***')
# for i in range(len(tests)):
#     if i == 2:
#         print(f'{tests[i]} by Solver#4: {y_data[i]} bits from {test5[3]} bits')
#     elif i == 3:
#         print(f'{tests[i]} by Solver#4: {y_data[i]} bits from {test5[-1]} bits')        
#     elif i == 4:
#         print(f'{tests[i]} by Solver#4: {y_data[i]} bits from {test5[3] - test5[-1]} bits') 
#     else:
#         print(f'{tests[i]} by Solver#4: {y_data[i]}')