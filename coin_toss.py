import random


def heads_tails(number_of_flips):
    heads_count = 0
    tails_count = 0
    for i in range(number_of_flips):
        rand = random.randint(1, 2)
        print(rand)
        if rand == 1:
            heads_count += 1
            print(heads_count, 'heads')
        else:
            tails_count += 1
            print(tails_count, 'tails')
    print('heads', heads_count)
    print('tails', tails_count)


heads_tails(1000000)
