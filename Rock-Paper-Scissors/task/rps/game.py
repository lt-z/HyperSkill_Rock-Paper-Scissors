import random

users = {}
o_choices = 'rock,paper,scissors'


def rps(user, choices, user_choice):
    choices = choices.split(',')
    t_choices = choices[choices.index(user_choice) + 1:] + choices[:choices.index(user_choice)]
    lose = t_choices[:len(t_choices) // 2]

    comp = random.choice(choices)
    if user_choice == comp:
        print(f'There is a draw ({user_choice})')
        return update_rating(user, 50)
    elif comp in lose:
        print(f'Sorry, but computer chose {comp}')
    else:
        print(f'Well done. Computer chose {comp} and failed')
        return update_rating(user, 100)


def update_rating(user, points):
    """Updates users dict and writes to rating.txt"""
    users[user] = users.get(user, 0) + points
    rate = open('rating.txt', 'w')
    for k, v in users.items():
        print(f'{k} {v}', file=rate, flush=True)
    rate.close()


def read_rating():
    """Reads rating.txt and adds it to users dict"""
    with open('rating.txt', 'r') as f:
        exist = f.read().splitlines()
    for item in exist:
        test = item.split()
        users[test[0]] = int(test[1])


read_rating()
name = input(f'Enter your name: ')
print(f'Hello, {name}')
user_list = input()
if not user_list:
    user_list = o_choices
print("Okay, let's start")

while True:
    intake = input()
    if intake == '!exit':
        print('Bye!')
        break
    if intake == '!rating':
        print(f'Your rating: {users.get(name, 0)}')
    elif intake not in user_list:
        print('Invalid input')
    else:
        rps(name, user_list, intake)
