from ClassFileCSV import file_csv1

i= 0 
while i < 3:
    name = str(input('Seu nome: '))
    age = int(input('Sua idade: '))
    position = int(input('Sua posição na fila: '))
    print('#='*15)
    file_csv1.add_datas(name,age,position)
    i+=1

