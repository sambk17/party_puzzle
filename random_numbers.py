import random

def random_numbers(num):
    return random.choices(range(1,num+1), k=num)

if __name__ == '__main__':
    num_A = 10
    num_B = 11

    print('There were %s' % num_A + ' who played the game and these are the results: %s' % random_numbers(num_A))
    print('There were %s' % num_B + ' who played the game and these are the results: %s' % random_numbers(num_B))