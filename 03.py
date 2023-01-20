# Создайте программу для игры в ""Крестики-нолики"".

def task_info():
    print('Игра Крестики-нолики')

playing_field = [1,2,3,
                4,5,6,
                7,8,9]

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def playing_field_print():
    print(playing_field[0], end = " ")
    print(playing_field[1], end = " ")
    print(playing_field[2])

    print(playing_field[3], end = " ")
    print(playing_field[4], end = " ")
    print(playing_field[5])

    print(playing_field[6], end = " ")
    print(playing_field[7], end = " ")
    print(playing_field[8])                      

def step_playing_field(step,symbol):
    ind = playing_field.index(step)
    playing_field[ind] = symbol   

def get_result():
    win = ""
    for i in victories:
        if playing_field[i[0]] == "X" and playing_field[i[1]] == "X" and playing_field[i[2]] == "X":
            win = "X"
        if playing_field[i[0]] == "O" and playing_field[i[1]] == "O" and playing_field[i[2]] == "O":
            win = "O"   
    return win    

game_over = False
player1 = True
task_info()

while game_over == False:

    playing_field_print()

    if player1 == True:
        symbol = "X"
        step = int(input("Ход первого игрока: "))
    else:
        symbol = "O"
        step = int(input("Ход вторго игрока: "))

    step_playing_field(step,symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not(player1)            

playing_field_print()
print("Победил", win)    