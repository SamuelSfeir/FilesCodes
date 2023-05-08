import os

source = 'test.txt'
destination = 'C:\\Users\\samue\\OneDrive\\Área de Trabalho'

with open('testing.txt','w') as file:
    file.write('Just a test')

with open('testing.txt','a') as file:
    file.write('\nAlso another test')

with open('testing.txt','r') as file:
    print(file.read())
