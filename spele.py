#Šī rindiņa inicializē 3x3 režģi, ko sauc par laukumu, un katra šūna tiek inicializēta ar atstarpi.
laukums = [[' ' for _ in range(3)] for _ in range(3)]

#šī rinda definē funkciju ar nosaukumu print_laukumu(), ko izmanto, lai vizuālā attēlojumā izdrukātu pašreizējo režģa stāvokli.
def print_laukumu():
    #šī līnija drukā režģa augšējo apmali.
    print("+---+---+---+")
    #Šī rinda uzsāk atkārtojuma struktūru, kas atkārtojas katrā režģa rindā.
    for i in range(3):
        # šī rinda drukā vertikālo apmali katras rindas sākumā, nepārejot uz nākamo rindiņu.
        print("| ", end="")
        #Šī rinda uzsāk atkārtojuma struktūru, kas atkārtojas katrā pašreizējās rindas šūnā.
        for j in range(3):
        # šajā rindā tiek izdrukāts pašreizējās šūnas saturs, kam seko vertikāla apmale un atstarpe.
            print(laukums[i][j], end=" | ")
        #Šī līnija drukā vertikālo apmali katras rindas beigās un pāriet uz nākamo rindu, kam seko horizontālā apmale, kas atdala rindas.
        print("\n+---+---+---+")

#šī rinda definē funkciju ar nosaukumu parbauda_uzvarētāju(), kas pārbauda uzvarētāju, pārbaudot režģa rindas, kolonnas un diagonāles.
def parbauda_uzvarētāju():
    #Šī rinda uzsāk atkārtojuma struktūru, kas atkārtojas katrā režģa rindā.
    for i in range(3):
        #Šī rinda pārbauda, ​​vai visas trīs pašreizējās rindas šūnas ir vienādas un nav tukšas.
        if laukums[i][0] == laukums[i][1] == laukums[i][2] != ' ':
            #Šī rinda atgriež True, ja ir izpildīts uzvaras nosacījums.
            return True
        #Šī rinda pārbauda, ​​vai visas trīs pašreizējās kolonnas šūnas ir vienādas un nav tukšas.
        if laukums[0][i] == laukums[1][i] == laukums[2][i] != ' ':
            #Šī rinda atgriež True, ja ir izpildīts uzvaras nosacījums.
            return True
    #Šī rinda pārbauda, ​​vai visas trīs šūnas diagonālē no augšējās kreisās puses uz apakšējo labo pusi ir vienādas un nav tukšas.
    if laukums[0][0] == laukums[1][1] == laukums[2][2] != ' ':
       #Šī rinda atgriež True, ja ir izpildīts uzvaras nosacījums.
        return True
    #Šī rinda pārbauda, ​​vai visas trīs šūnas diagonālē no augšējās labās puses uz apakšējo kreiso ir vienādas un nav tukšas.
    if laukums[0][2] == laukums[1][1] == laukums[2][0] != ' ':
        #Šī rinda atgriež True, ja ir izpildīts uzvaras nosacījums.
        return True
    #Šī rinda atgriež False, ja nav izpildīts neviens uzvaras nosacījums.
    return False

#Šī rinda definē funkciju parbauda_neizšķirtu(), kas pārbauda, ​​vai režģī nav palikušas tukšas šūnas.
def parbauda_neizšķirtu():
    #Šī rinda uzsāk atkārtojuma struktūru, kas atkārtojas katrā režģa rindā.
    for row in laukums:
        #Šī rinda uzsāk atkārtojuma struktūru, kas atkārtojas katrā pašreizējās rindas šūnā.
        for cell in row:
            #Šī rinda pārbauda, ​​vai pašreizējā šūna ir tukša.
            if cell == ' ': 
                #Šī rinda atgriež False, ja ir vismaz viena tukša šūna.
                return False
     #Šī rinda atgriež True, ja visas šūnas ir aizpildītas, norādot neizšķirtu.       
    return True

#Šī rinda definē funkciju ar nosaukumu spele(), kas aptver visu spēles loģiku.
def spele(): 
    #Šī rinda inicializē mainīgo Pašraizējais_spēlētājs uz 'X', norādot pašreizējo spēlētāju
    Pašraizējais_spēlētājs = 'X' 
    #šī rinda sāk bezgalīgu spēles atkārtojuma struktūru.
    while True:
        #Šajā rindā tiek izdrukāts pašreizējais režģa stāvoklis.
        print_laukumu()
        #šī rinda sāk bezgalīgu atkārtojuma struktūru spēlētāju ievades ņemšanai.
        while True:
            try:
                #Šī rinda liek pašreizējam spēlētājam ievadīt rindas numuru.
                row = int(input(f'Spēlētāj {Pašraizējais_spēlētājs}, ievadi rindu (1-3): ')) - 1
                # Šī rinda liek pašreizējam spēlētājam ievadīt kolonnas numuru.
                col = int(input(f'spēlētāj {Pašraizējais_spēlētājs}, ievadi colonu  (1-3): ')) - 1
                #Šī rinda pārbauda, ​​vai ievades rinda un kolonna ir iespējams un vai atlasītā šūna ir tukša.
                if 0 <= row < 3 and 0 <= col < 3 and laukums[row][col] == ' ':
                    #Šī līnija iziet no ievades cilpas, ja tiek nodrošināta derīga ievade.
                    break
                #Šī rinda tiek izpildīta, ja ievade nav derīga.
                else:
                    #Šajā rindā tiek izdrukāts ziņojums, kas norāda uz nederīgu ievadi.
                    print('Nepareiza ievade. Mēģini velrais.')
                    #Šī rinda apstrādā izņēmumu, ja ievadi nevar pārvērst par veselu skaitli.
            except ValueError:
                #Šajā rindiņā tiek izdrukāts ziņojums, kas norāda, ka ievadei jābūt ciparam.
                print('Nepareiza ievade. Ieraksti ciparu.')

        #Šī rinda atjaunina atlasīto šūnu ar pašreizējā spēlētāja simbolu.
        laukums[row][col] = Pašraizējais_spēlētājs

       #Šī rinda pārbauda, ​​vai ir uzvarētājs.
        if parbauda_uzvarētāju():
            #Šajā rindā tiek izdrukāts pašreizējais režģa stāvoklis.
            print_laukumu()
            #Šajā rindā tiek izdrukāts ziņojums, kurā tiek paziņots uzvarētājsju.
            print(f'Spēlētājs {Pašraizējais_spēlētājs} uzvar!')
           # Šī līnija iziet no ievades cilpas.
            break

       #Šī līnija pārbauda, ​​vai spēle ir neizšķirta.
        if parbauda_neizšķirtu():
           #Šajā rindā tiek izdrukāts pašreizējais režģa stāvoklis.
            print_laukumu()
            #šajā rindā tiek izdrukāts ziņojums, kas norāda uz neizšķirtu.
            print("Neizšķirts!")
            #Šī līnija iziet no ievades cilpas.
            break

        #šī rinda samaina pašreizējo spēlētāju nākamajam gājienam.
        Pašraizējais_spēlētājs = 'O' if Pašraizējais_spēlētājs == 'X' else 'X'

#Šī līnija sāk spēli.
spele()
