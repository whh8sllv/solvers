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
    solver_number = int(input('Your choice is Solver#'))
    print('Add your input data')
    n = int(input('n = '))
    m = int(input('m = '))
    h = int(input('h = '))
    sample = int(input('sample size = '))
    if solver_number == 4:
        epsilon = int(input('epsilon = '))
        return solver_number, n, m, h, epsilon, sample
    return solver_number, n, m, h, sample

def run_tests():
    input_data = get_input()

    if input_data[0] == 1:
        time_list = []
        for _ in range(input_data[4]):
            solver = Solver1(input_data[1], input_data[2], input_data[3])
            x = bin(solver.x)[2:]
            x_true = [i for i in x]
            res = solver.recover_x()
            x_solver = res[0]
            time = res[1]
            time_list.append(time)
        return sum(time_list) / len(time_list), time_list
    
    if input_data[0] == 2:
        ...
    if input_data[0] == 3:
        ...
    if input_data[0] == 4:
        ...
    if input_data[0] == 5:
        ...
    if input_data[0] == 6:
        ...

test1 = run_tests()
print(f'AVG time of Solver1 = {test1[0]}')
print(test1[1])