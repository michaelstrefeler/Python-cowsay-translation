import sys
from textwrap import wrap

def cowsay(text):
    return bubble(text) + cow()

def bubble(text):

    lines = wrap(text, 40)

    bubble = ''
    if len(lines) == 1:
        top = ' ' + '_' * (len(text)+2) + ' '
        middle = '< ' + text + ' >'
        bottom =' ' + '-' * (len(text)+2) + ' '  
    else:
        top = ' ' + '_'* 40 + ' '
        middle = ''
        for i in range(0, len(lines)):
            if i == 0:
                middle += '/ ' + lines[i] + ' \\'
            elif i == len(lines) -1 :
                middle += '\n' + r'\ ' + lines[i]
                middle = middle + ' ' * (len(lines[0]) - len(lines[i])) + ' /'
            else:
                middle += '\n| ' + lines[i]
                middle += ' ' * (len(lines[0]) - len(lines[i])) + ' |'
        bottom = ' ' + '-'* 40 + ' ' 
    
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