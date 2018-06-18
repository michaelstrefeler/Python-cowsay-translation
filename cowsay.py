import sys
from textwrap import wrap

cow_list = ['apt', 'beavis.zen', 'bong', 'bud-frogs', 'bunny', 'calvin', 'cheese', 'cock', 'cower', 'daemon', 'default', 'dragon', 'dragon-and-cow', 'duck', 'elephant', 'elephant-in-snake', 'eyes', 'flaming-sheep', 'ghostbusters', 'gnu', 'head-in', 'hellokitty', 'kiss', 'kitty', 'koala', 'kosh', 'luke-koala', 'mech-and-cow', 'meow', 'milk', 'moofasa', 'moose', 'mutilated', 'pony', 'pony-smaller', 'ren', 'satanic', 'sheep', 'skeleton', 'snowman', 'small', 'sodomized', 'sodomized-sheep', 'stegosaurus', 'stimpy', 'supermilker', 'surgery', 'suse', 'three-eyes', 'turkey', 'turtle', 'tux', 'udder', 'unipony', 'unipony-smaller', 'vader', 'vader-koala', 'www']

def cowsay(text, animal='default'):
    eyes = 'oo'
    tongue = '  '
    # Manually specifies the cow's eye-type
    if '-e' in sys.argv:
        eyes = sys.argv[sys.argv.index('-e')+1][:2]
        text = text.replace(f'-e {eyes}', '')
    # "Bord mode", uses == in place of oo for the cow's eyes
    if '-b' in sys.argv:
        eyes = '=='
        text = text.replace(f'-b ', '')
    # "Greedy", uses $$
    if '-g' in sys.argv:
        eyes = '$$'
        text = text.replace(f'-g ', '')  
    # "paranoid", uses @@
    if '-p' in sys.argv:
        eyes = '@@'
        text = text.replace(f'-p ', '')
    # "Stoned", uses ** to represent bloodshot eyes, plus a descending U to represent an extruded tongue
    if '-s' in sys.argv:
        eyes = '**'
        tongue = 'U '
        text = text.replace(f'-s ', '')
    # "Tired", uses --
    if '-t' in sys.argv:
        eyes = '--'
        text = text.replace(f'-t ', '')
    # "Wired", uses OO
    if '-w' in sys.argv:
        eyes = 'OO'
        text = text.replace(f'-w ', '')                   
    # "Youthful", uses .. to represent smaller eyes
    if animal == 'small' or '-y' in sys.argv:
        eyes = '..'      
    
    # Manually specifies the cow's tongue shape
    if '-T' in sys.argv:
        tongue = sys.argv[sys.argv.index('-T')+1][:2]
        if len(tongue) < 2:
            tongue = tongue + ' '    
        text = text.replace(f'-T {tongue}', '')
   # "Dead", uses XX, plus a descending U to represent an extruded tongue
    if '-d' in sys.argv:
        if eyes == '':
            eyes = 'XX'
        if 'sheep' in animal:
            eyes = eyes.lower()
        tongue = 'U '
        text = text.replace(' -d ', '').replace(eyes, '')
    # Adds a third eye if three-eyes is selected
    if animal == 'three-eyes':
        eyes = eyes + eyes[0]                    
    return bubble(text) + cow(animal, eyes, tongue)

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

def cow(animal, eyes, tongue):
    with open(f'cows/{animal}.txt', 'r') as myAnimal:
        data = myAnimal.read().replace('$eyes', eyes).replace('$tongue', tongue)  
    return '\n' + data

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Try again.\nUsage: {sys.argv[0]} [-h] [-l] message')     
    elif len(sys.argv) >= 2 and '-h' in sys.argv:
        print(f'Usage: {sys.argv[0]} [-h] [-l] [-f cowfile] message')    
    elif len(sys.argv) >= 2 and '-l' in sys.argv:
        print(' '.join([cow for cow in cow_list]))
    elif sys.argv[1] == '-f':
        animal = sys.argv[2]
        sentence = ' '.join([arg for arg in sys.argv if arg != 'cowsay.py' and arg != '-f']).partition(' ')[2] # Removes cowfile name from sentence
        if animal in cow_list:
            print(cowsay(sentence, animal))
        else:
            print(f'cowsay: Could not find {animal} cowfile')                 
    else:
        sentence = ' '.join([arg for arg in sys.argv if arg != 'cowsay.py']) 
        print(cowsay(sentence, 'default'))    