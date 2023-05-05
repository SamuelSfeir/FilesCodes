import os
try:
    with open('C:\\Users\\samue\\OneDrive\\Área de Trabalho\\test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('Error: That file was not found')
