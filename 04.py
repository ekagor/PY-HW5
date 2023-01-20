# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open ('file_005.txt', 'r') as data:
    file = ''.join(line.strip() for line in data)

list_01, result_list = file[0], ''
i = 0

for elem in file:
    if elem != list_01[-1]:
        result_list+= str(i) + list_01[-1]
        i=1
        list_01 = elem
    else:
        i+=1
        list_01+=elem
result_list+=str(i)+list_01[-1]            

with open ('file_007.txt', 'w') as data:
    data.writelines(result_list)
with open ('file_007.txt', 'r') as data:   
    file2 = ''.join(line.strip() for line in data)

result_list = ''

for elem in file2:
    if elem.isalpha():
        elem = file2.index(elem)
        num = int(file2[0:elem])
        result_list+=num*elem
        file2 = file2[elem+1:]
with open ('file_010.txt', 'w') as data:
    data.writelines(result_list)     

print(result_list)    