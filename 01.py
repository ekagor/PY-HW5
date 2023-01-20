# Напишите программу, удаляющую из текста 
# все слова, содержащие ""абв""

def task_info():
    print('Программа удаляет из текста все слова, содержащие "абв"')

def del_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

task_info()
my_text = 'Незадачливый Клабва иабв заяц коралабвлы был оабвзадачен озадачен \
Кларытабв новой поэтомуабв задачей абв съелабв абву коралабвлы Карабвла ихабв отобабврав'
string = del_words(my_text)
print(my_text)
print(string)