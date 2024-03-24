
laukums = [[' ' for _ in range(3)] for _ in range(3)]


def print_laukumu():
    print("+---+---+---+")
    for i in range(3):
        print("| ", end="")
        for j in range(3):
            print(laukums[i][j], end=" | ")
        print("\n+---+---+---+")


def parbauda_uzvarētāju():
    
    for i in range(3):
        if laukums[i][0] == laukums[i][1] == laukums[i][2] != ' ':
            return True
        if laukums[0][i] == laukums[1][i] == laukums[2][i] != ' ':
            return True
    
    if laukums[0][0] == laukums[1][1] == laukums[2][2] != ' ':
        return True
    if laukums[0][2] == laukums[1][1] == laukums[2][0] != ' ':
        return True
    return False


def parbauda_neizšķirtu():
    for row in laukums:
        for cell in row:
            if cell == ' ': 
                return False
    return True


def spele(): 
    Pašraizējais_spēlētājs = 'X' 
    while True:
        print_laukumu()
        while True:
            try:
                row = int(input(f'Spēlētāj {Pašraizējais_spēlētājs}, ievadi rindu (1-3): ')) - 1
                col = int(input(f'spēlētāj {Pašraizējais_spēlētājs}, ievadi colonu  (1-3): ')) - 1
                if 0 <= row < 3 and 0 <= col < 3 and laukums[row][col] == ' ':
                    break
                else:
                    print('Nepareiza ievade. Mēģini velrais.')
            except ValueError:
                print('Nepareiza ievade. Ieraksti ciparu.')

        
        laukums[row][col] = Pašraizējais_spēlētājs

       
        if parbauda_uzvarētāju():
            print_laukumu()
            print(f'Spēlētājs {Pašraizējais_spēlētājs} uzvar!')
            break

       
        if parbauda_neizšķirtu():
            print_laukumu()
            print("Neizšķirts!")
            break

        
        Pašraizējais_spēlētājs = 'O' if Pašraizējais_spēlētājs == 'X' else 'X'


spele()
