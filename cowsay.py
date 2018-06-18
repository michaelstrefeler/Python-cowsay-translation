import sys
from textwrap import wrap

cow_list = ['bong', 'default']

def cowsay(text, animal='default'):
    return bubble(text) + cow(animal)

def bubble(text):

    lines = wrap(text, 38)

    bubble = ''
    if len(lines) == 1:
        top = ' ' + '_' * (len(text)+2) + ' '
        middle = '< ' + text + ' >'
        bottom =' ' + '-' * (len(text)+2) + ' '
    else:
        for i in range(0, len(lines)):
            top = ' ' + '_' * (len(lines[i]) + 40 - len(lines[i]))
            text = lines[i] + ' ' * (len(top) - 2 - len(lines[i]))
            if i == 0:
                middle = '/ ' + text + '\\'
            elif i == len(lines) -1:
                middle += '\n' + '\\ ' + text + '/'
            else:
                middle += '\n' + '| ' + text + '|'  
            
            bottom = top.replace('_', '-')        
    bubble = top + '\n' + middle + '\n' + bottom
    return bubble

def cow(animal):
    if animal == 'default':
        return r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||"""    
    else:
        with open(f'cows/{animal}.txt', 'r') as myAnimal:
            data = myAnimal.read()  
        return '\n' + data

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Try again.\nUsage: {sys.argv[0]} [-h] [-l] message')     
    elif len(sys.argv) >= 2 and sys.argv[1] == '-h':
        print(f'Usage: {sys.argv[0]} [-h] [-l] message')    
    elif len(sys.argv) >= 2 and sys.argv[1] == '-l':
        print(' '.join([cow for cow in cow_list]))
    elif sys.argv[1] == '-f':
        animal = sys.argv[2]
        sentence = ' '.join([arg for arg in sys.argv if arg != 'cowsay.py' and arg != '-f' and arg != animal])
        if animal in cow_list:
            print(cowsay(sentence, animal))
        else:
            print(f'cowsay: Could not find {animal} cowfile')                 
    else:
        sentence = ' '.join([arg for arg in sys.argv if arg != 'cowsay.py']) 
        print(cowsay(sentence, 'default'))    