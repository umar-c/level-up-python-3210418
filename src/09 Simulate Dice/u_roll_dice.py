import random

# def build_sample_space(*args):
#     sub_sample_space = []
#     for i in range(1, args[0]+1):
#         sub_sample_space.append(build_sample_space(*args[1]))

# This solution builds the sample space for all the outcomes
# and then calculates the probability of each outcome.
# This solution can only take 2 dice for now. It can be
# expanded to 3 dice for manually building the sample space,
# but for anything beyond that, we'll need a generic formula
# to build the sample space for n dice.
# See https://www.lucamoroni.it/the-dice-roll-sum-problem/ for details.
def roll_2_dice(*args):
    if len(args) != 2:
        print("This method requires 2 dice! Exiting...")
        return
    
    print(f"Dice({len(args)}) = {list(args)}")
    print(*args)

    sample_space = []

    for i in range(1, args[0]+1):
        for j in range(1, args[1]+1):
            sample_space.append((i, j))

    outcomes_per_digit = dict.fromkeys(range(len(args), sum(args)+1), 0.0)
    print(outcomes_per_digit)
 
    for digit in range(len(args), sum(args)+1):
        for pair in sample_space:
            if pair[0] + pair[1] == digit:
                outcomes_per_digit[digit] += 1
        outcomes_per_digit[digit] = float(outcomes_per_digit[digit] * 100 /len(sample_space))
    
    for digit, prob in outcomes_per_digit.items():
        print(f"{digit:2d}: {prob:.2f}")

# Method using the random function to simulate dice rolling
# and counting the occurances of each outcome.
def roll_dice(*dice, num_trials=1_000_000):
    if len(dice) == 0:
        print("At least one dice is required! Exiting...")
        return
    
    max_sum = sum(dice)
    nums = range(len(dice), max_sum + 1)
    prob_table = dict.fromkeys(nums, 0.0)

    for trial in range(num_trials):
        print('Calculating probabilities for roll_dice(' + '{0}'.format(list(dice)) + ')... '
        + '{0:5}'.format('\\' if not trial%2 else '/' if not trial%3 else '-')
        + '[ {0:10} ] {1:3}%'.format('#'*int(round(trial/num_trials*10)), int(round(trial/num_trials*100))), end='\r')

        total = 0
        for die in range(len(dice)):
            total += random.randrange(1, dice[die]+1)

        prob_table[total] += 1

    print('\n Sum  Probability')
    for num, prob in prob_table.items():
        prob_table[num] /= float(num_trials) / 100
        print(f"{num:3d}:  |  {prob_table[num]:.02f}")

# commands used in solution video for reference
if __name__ == '__main__':
    roll_2_dice(4, 6)
    print('\n')
    roll_dice(6)
    print('\n')
    roll_dice(4, 6, 6)
    print('\n')
    roll_dice(6, 6, 6)
    print('\n')
    roll_dice(4, 6, 6, 20)
    print('\n')
    roll_dice(4, 6, 6, 8, 10, 12, 12, 14, 16, 18, 18, 20, 24)

    # Check the results using this link: https://anydice.com/
    # For example, to calculate probabilities for roll_dice(4, 6, 6, 20),
    # enter this in the input window: output 1d4+2d6+1d20
    # Here are the results:
    # Sum  Probability
    #  4:  |  0.03
    #  5:  |  0.14
    #  6:  |  0.35
    #  7:  |  0.69
    #  8:  |  1.18
    #  9:  |  1.81
    # 10:  |  2.50
    # 11:  |  3.19
    # 12:  |  3.82
    # 13:  |  4.31
    # 14:  |  4.65
    # 15:  |  4.86
    # 16:  |  4.97
    # 17:  |  5.00
    # 18:  |  5.00
    # 19:  |  5.00
    # 20:  |  5.00
    # 21:  |  5.00
    # 22:  |  5.00
    # 23:  |  5.00
    # 24:  |  4.97
    # 25:  |  4.86
    # 26:  |  4.65
    # 27:  |  4.31
    # 28:  |  3.82
    # 29:  |  3.19
    # 30:  |  2.50
    # 31:  |  1.81
    # 32:  |  1.18
    # 33:  |  0.69
    # 34:  |  0.35
    # 35:  |  0.14
    # 36:  |  0.03
