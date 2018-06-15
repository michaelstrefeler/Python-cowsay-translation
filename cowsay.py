import sys
from textwrap import wrap

def cowsay(text):
    return bubble(text) + cow()

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
            if i == 0:
                print(len(lines[i])-len(top))
                middle = '/ ' + lines[i] + ' ' * (len(top) - 2 - len(lines[i])) + '\\'
            elif i == len(lines) -1:
                middle += '\n' + '\\ ' + lines[i] + ' ' * (len(top) - 2 - len(lines[i])) + '/'
            else:
                middle += '\n' + '| ' + lines[i] + ' ' * (len(top) - 2 - len(lines[i])) + '|'  
            

            bottom = top.replace('_', '-')        
    bubble = top + '\n' + middle + '\n' + bottom
    return bubble

def cow():
    return r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||"""    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage:\n{sys.argv[0]} -l\n{sys.argv[0]} -h\n{sys.argv[0]} message')
        exit()

    sentence = ''
    for arg in sys.argv:
        if arg != 'cowsay.py':
            if not sentence:
                sentence = arg
            else:
                sentence = sentence + ' ' + arg

    print(cowsay(sentence))    