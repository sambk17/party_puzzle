from random_numbers import random_numbers

def strategy(num):
    random_num = random_numbers(num)
    strat = list(range(1,num+1))
    predicted_list = []
    for i in range(len(strat)):
        other_nums = sum(random_num) - random_num[i] + strat[i]
        mod = other_nums % num
        if mod == 0:
            predicted_list.append(1)
        else:
            predicted_list.append(mod)
    return random_num, predicted_list

def simulation(num, loops=100):
    count = 0
    for i in range(loops):
        random_num, predicted_list = strategy(num)
        count += int(True in [i in random_num for i in predicted_list])
    return count

if __name__ == '__main__':
    num_A = 10
    loop_A = 1000
    num_B = 11
    loop_B = 10000

    print('There were %s' % num_A + ' who played the game %s' %loop_A + ' times and based off the strategy, they won %s' % simulation(num_A, loops=loop_A) + ' times')
    print('There were %s' % num_B + ' who played the game %s' %loop_B + ' times and based off the strategy, they won %s' % simulation(num_B, loops=loop_B) + ' times')