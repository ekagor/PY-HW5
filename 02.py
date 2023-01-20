# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import time
import random

def task_info():
    print('Игра 2021 конфета.')
    print('На столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга.')
    print('За один ход можно забрать не более чем 28 конфет')
    print('Все конфеты оппонента достаются сделавшему последний ход.')

def player_move(min_step: int, max_step: int) -> int:
    candy_out = -1
    while candy_out < min_step or candy_out > max_step:
        candy_out = int(input(f'Сколько конфет Вы забираете? '
            f'Введите количество от {min_step} до {max_step}: '))
    return candy_out

def win_algorithm(candy_on_table: int, min_pick_up: int, max_pick_up: int):
    return candy_on_table-candy_on_table//(min_pick_up+max_pick_up)*(min_pick_up+max_pick_up)

def bot_random(min_pick_up: int, max_pick_up: int) -> int:
    return random.randint(min_pick_up, max_pick_up)

def bot_intelligence(candy_on_table: int, min_pick_up: int, max_pick_up: int) -> int:
    way_num = win_algorithm(candy_on_table, min_pick_up, max_pick_up)
    if way_num >= min_pick_up and way_num < min_pick_up+max_pick_up:
        return way_num
    else:
        return random.randint(min_pick_up, max_pick_up)

def spelling(number_candies: int) ->str:
    spell = 'конфет'
    ones = [1, 21]
    twines = [2, 3, 4, 22, 23, 24]
    if number_candies in ones:
        spell = 'конфету'
    elif number_candies in twines:
        spell = 'конфеты' 
    return spell

candy = 2021
min_step = 1
max_step = 28
task_info()
player_1 = input('Вы - первый игрок, назовите ваше имя: ')
if input('Для игры вдвоем введите "1": ') == '1':
    player_2 = input('Вы - второй игрок, назовите ваше имя: ')
else:
    player_2 = 'Robot'
player_dict = {1: player_1, 2: player_2}
bot_level = input('Для игры с умным роботом введите "1".\n'
    'Для игры с глупым роботом введите любой другой символ: ')
if bot_level == '1':
    bot_level = int(bot_level)
else:
    bot_level = 2
print('Сейчас узнаем кто ходит первым')
player_num = int(time.time()//1%2+1)
print(f'Первым ходит {player_dict[player_num]}')
print('Играем')
candy_out = 0
while candy > 0:
    if player_dict[player_num] != 'Robot':
        candy_out = player_move(min_step, max_step)
    elif bot_level == 1:
        candy_out = bot_intelligence(candy, min_step, max_step)
    else:
        candy_out = bot_random(min_step, max_step)
    candy = candy - candy_out
    print(f'{player_dict[player_num]} забрал {candy_out} {spelling(candy_out)}.\n'
        f'На столе осталось {candy} {spelling(candy)}.')
    if player_num+1 > 2:
        player_num = 1
    else:
        player_num = 2
if player_num+1 > 2:
    player_num = 1
else:
    player_num = 2  
print('!!!')      
print(f'Выиграл {player_dict[player_num]}!!!')
print()