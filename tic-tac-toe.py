print('Вы запустили игру крестики нолики!)'.center(140, ' '))

def show(pole):
    print(f'\t\t\t\t\t{pole[:3]}', f'\t\t\t\t\t{pole[3:6]}',f'\t\t\t\t\t{pole[6:]}', sep='\n')
    return '\n'


def post_hrest(free_pos, pole):
    try:
        hrest = input(f"Выберите где вы поставите крестик\n{free_pos}\nЦифра:")
        free_pos.remove(hrest)
        pole[int(hrest)-1] = '+'
        return free_pos, pole
    except ValueError:
        print("Выберите доступную позицию!!!".center(150,' '))
        return post_hrest(free_pos, pole)
    

def post_null(free_pos, pole):
    try:
        noliki = input(f"Выберите где вы поставите нолик\n{free_pos}\nЦифра:")
        free_pos.remove(noliki)
        pole[int(noliki)-1] = '0'
        return free_pos, pole
    except ValueError:
        print("Выберите доступную позицию!!!".center(150,' '))
        return post_null(free_pos, pole)


def paraleli(pole):
    d = {'+':'КРЕСТИКИ', '0':'НОЛИКИ'}
    if pole[0][0] == pole[1][1] == pole[2][2] != '*':
        print(f'\n\t\t\t\t\t{d.get(pole[0][0])} ВЫИГРАЛИ!!!\t\t\t\n')
        return f'{d.get(pole[0][0])} ВЫИГРАЛИ!!!'
    elif pole[0][-1] == pole[1][1] == pole[2][0] != '*':
        print(f'\n\t\t\t\t\t{d.get(pole[0][0])} ВЫИГРАЛИ!!!\t\t\t\n')
        return f'{d.get(pole[0][-1])} ВЫИГРАЛИ!!!'
    else:
        return False


def diagonals(item, pole):
    d = {'+':'КРЕСТИКИ', '0':'НОЛИКИ'}
    if any([all(map(lambda x: x ==item, pole[elem])) for elem in range(3)]):
        print(f'\n\t\t\t\t\t{d.get(item)} ВЫИГРАЛИ!!!\t\t\t\n')
        return f'{d.get(item)} ВЫИГРАЛИ!!!'
    return False


def vertical(item, pole):
    d = {'+':'КРЕСТИКИ', '0':'НОЛИКИ'}
    if any([all(map(lambda x: x ==item, [pole[pos][elem] for pos in range(3)])) for elem in range(3)]):
        print(f'\n\t\t\t\t\t{d.get(item)} ВЫИГРАЛИ!!!\t\t\t\n')
        return f'{d.get(item)} ВЫИГРАЛИ!!!'
    return False



#def decor(func):
#    def wrapper():
#        quit = input("Вы хотите играть? да/нет: ")
#        if quit.lower() == 'нет':
#            return 'ПОКА!'
#        elif quit.lower() == 'да':
#            return func()
#        else:
#            print('Выберите да\\нет')
#            return wrapper()
#    return wrapper
#
#@decor
def main():
    pole_igri = ['*'] * 9
    while True:
        swobodnie = [str(i+1) for i, it in enumerate(pole_igri) if it == '*']
        swobodnie, pole_igri = post_hrest(swobodnie, pole_igri)
        special = [pole_igri[0:3],pole_igri[3:6],pole_igri[6:],]
        par = paraleli(special)
        dia_hres = diagonals('+', special)
        ver_hres = vertical('+', special)
        if par:
            show(pole_igri)
            return par
        elif dia_hres:
            show(pole_igri)
            return dia_hres
        elif ver_hres:
            show(pole_igri)
            return ver_hres
        
        if all(map(lambda x: x == '*', swobodnie)):
            show(pole_igri)
            return "Game Over".center(150,' ')
        swobodnie, pole_igri = post_null(swobodnie, pole_igri)
        special = [pole_igri[0:3],pole_igri[3:6],pole_igri[6:],]
        par_null = paraleli(special)
        dia_null = diagonals('0', special)
        ver_null = vertical('0', special)
        if par_null:
            show(pole_igri)
            return par_null
        elif dia_null:
            show(pole_igri)
            return dia_null
        elif ver_null:
            show(pole_igri)
            return ver_null
        show(pole_igri)

def wrapper():
        quit = input("Вы хотите играть? да/нет: ")
        if quit.lower() == 'нет':
            return 'ПОКА!'
        elif quit.lower() == 'да':
            return main()
        else:
            print('Выберите да\\нет')
            return wrapper()


while True:
    txt = wrapper() == 'ПОКА!'
    if txt:
        break
    else:
        wrapper()