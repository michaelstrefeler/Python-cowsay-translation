from sys import argv
from textwrap import wrap

# List of all available cows
cow_list = [
    'apt', 'beavis.zen', 'bong', 'bud-frogs', 'bunny', 'calvin', 'cheese',
    'cock', 'cower', 'daemon', 'default', 'dragon', 'dragon-and-cow', 'duck',
    'elephant', 'elephant-in-snake', 'eyes', 'flaming-sheep', 'ghostbusters',
    'gnu', 'head-in', 'hellokitty', 'kiss', 'kitty', 'koala', 'kosh',
    'luke-koala', 'mech-and-cow', 'meow', 'milk', 'moofasa', 'moose',
    'mutilated', 'pony', 'pony-smaller', 'ren', 'satanic', 'sheep', 'skeleton',
    'snowman', 'small', 'sodomized', 'sodomized-sheep', 'stegosaurus',
    'stimpy', 'supermilker', 'surgery', 'suse', 'three-eyes', 'turkey',
    'turtle', 'tux', 'udder', 'unipony', 'unipony-smaller', 'vader',
    'vader-koala', 'www'
]


def cowsay(text, animal='default'):
    eyes = 'oo'
    tongue = '  '
    # Manually specifies the cow's eye-type
    if '-e' in argv:
        if argv.index('-e') + 1 in range(0, len(argv)):
            if argv.index('-e') + 2 in range(0, len(argv)):
                eyes = argv[argv.index('-e') + 1][:2]
                text = text.replace(f'-e {argv[argv.index("-e")+1]} ', '')
            else:
                print('cowsay: error no text added after -e eye_string')
                exit()
        else:
            print('cowsay: error no text added after -e')
            exit()

    # "Borg mode", uses == in place of oo for the cow's eyes
    if '-b' in argv:
        eyes = '=='
        text = text.replace('-b ', '')

    # "Greedy", uses $$
    if '-g' in argv:
        eyes = '$$'
        text = text.replace('-g ', '')

    # "paranoid", uses @@
    if '-p' in argv:
        eyes = '@@'
        text = text.replace('-p ', '')
    # "Stoned", uses ** to represent bloodshot eyes
    # plus a descending U to represent an extruded tongue

    if '-s' in argv:
        eyes = '**'
        tongue = 'U '
        text = text.replace('-s ', '')

    # "Tired", uses --
    if '-t' in argv:
        eyes = '--'
        text = text.replace('-t ', '')

    # "Wired", uses OO
    if '-w' in argv:
        eyes = 'OO'
        text = text.replace('-w ', '')

    # "Youthful", uses .. to represent smaller eyes
    if animal == 'small' or '-y' in argv:
        eyes = '..'
        text = text.replace('-y ', '')

    # Manually specifies the cow's tongue shape
    if '-T' in argv:
        if argv.index('-T') + 1 in range(0, len(argv)):
            if argv.index('-T') + 2 in range(0, len(argv)):
                tongue = argv[argv.index('-T') + 1][:2]
                if len(tongue) < 2:
                    tongue = tongue + ' '
                text = text.replace(f'-T {tongue}', '')
            else:
                print('cowsay: error no text added after -T tongue_string')
                exit()
        else:
            print('cowsay: error no text added after -T')
            exit()

    # "Dead", uses XX, plus a descending U to represent an extruded tongue
    if '-d' in argv:
        if eyes == 'oo':
            eyes = 'XX'
        if 'sheep' in animal:
            eyes = eyes.lower()
        tongue = 'U '
        text = text.replace('-d ', '').replace(eyes, '')

    # Adds a third eye if three-eyes is selected
    if animal == 'three-eyes':
        eyes = eyes + eyes[0]
    return bubble(text) + cow(animal, eyes, tongue)


def bubble(text):
    if text == '':
        print('error: No text was entered after the parameters')
        exit()
    lines = wrap(text, 38)

    bubble = ''
    if len(lines) == 1:
        top = ' ' + '_' * (len(text) + 2) + ' '
        middle = '< ' + text + ' >'
        bottom = ' ' + '-' * (len(text) + 2) + ' '
    else:
        for i in range(0, len(lines)):
            top = ' ' + '_' * (len(lines[i]) + 40 - len(lines[i]))
            text = lines[i] + ' ' * (len(top) - 2 - len(lines[i]))
            if i == 0:
                middle = '/ ' + text + '\\'
            elif i == len(lines) - 1:
                middle += '\n' + '\\ ' + text + '/'
            else:
                middle += '\n' + '| ' + text + '|'

            bottom = top.replace('_', '-')
    bubble = top + '\n' + middle + '\n' + bottom
    return bubble


def cow(animal, eyes, tongue):
    with open(f'cows/{animal}.txt', 'r') as myAnimal:
        data = myAnimal.read().replace('$eyes', eyes)
        data = data.replace('$tongue', tongue)
    return '\n' + data


def handler():
    if len(argv) < 2:
        print(f'Try again.\nUsage: {argv[0]} [-h] [-l] message')

    elif len(argv) >= 2 and '-h' in argv:
        params = '[-h] [-l] [-f cowfile] [-e eyes] [-T tongue] message'
        print(f'Usage: {argv[0]} {params}')

    elif len(argv) >= 2 and '-l' in argv:
        print(' '.join([cow for cow in cow_list]))

    elif argv[1] == '-f':
        animal = argv[2]
        words = [arg for arg in argv if arg != argv[0] and arg != '-f']
        text = ' '.join([word for word in words])
        text = text.partition(' ')[2].replace(f'{animal} ', '', 1)

        if animal.lower() in cow_list:
            print(cowsay(text, animal))
        else:
            print(f'cowsay: Could not find {animal} cowfile')
    else:
        text = ' '.join([arg for arg in argv if arg != argv[0]])
        print(cowsay(text))


if __name__ == '__main__':
    handler()
