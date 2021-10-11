kluizen = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
beschisckbareKluizen = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
jaLijst = ['ja', 'js', 'yes', 'yep']
codes = open('codes.txt', 'w')


def toon_aantal_kluizen_vrij():
    print(beschisckbareKluizen)
    print('er zijn ' + str(len(beschisckbareKluizen)) + ' beschikbaar')


def nieuwe_kluis():
    code = ''
    codeopenen = open('codes.txt', 'a')

    if len(beschisckbareKluizen) != 0 and len(beschisckbareKluizen) != 1:
        print(beschisckbareKluizen)
        kluis = input('welke van de beschikbare kluizen wilt u?: ')

        if kluis in beschisckbareKluizen:

            # while loop om een geldige code te krijgen van de gebruiker
            while len(code) < 4:
                code = input('voer een code in voor je kluis: ')
                if len(code) >= 4:
                    print('kluis ' + kluis + ' is gehuurd.')
                    codeopenen.write('\nkluis ' + kluis + ' heeft als code ' + code + '\n' +
                                     kluis + ' ' + code)
                    beschisckbareKluizen.remove(kluis)

                else:
                    print('code is te kort')

        elif kluis not in beschisckbareKluizen:
            print('kluis ' + kluis + ' is niet beschikbaar')

    elif len(beschisckbareKluizen) == 1:

        ja_nee = input('kluis ' + beschisckbareKluizen[0] + ' is de enigste beschikbare wilt u deze kluis huren?: ')
        if ja_nee == 'ja':

            # while loop om een geldige code te krijgen van de gebruiker
            while len(code) < 4:
                code = 'voer een code in voor je kluis: '
                if len(code) >= 4:
                    print('kluis ' + str(beschisckbareKluizen[0]) + ' is gehuurd.')
                    codeopenen.write('\nkluis ' + str(beschisckbareKluizen[0]) + ' heeft als code ' + code + '\n' +
                                     str(beschisckbareKluizen[0]) + ' ' + code)
                    beschisckbareKluizen.clear()

                else:
                    print('code is te kort')

        else:
            print('er wordt geen kluis gehuurd')

    else:
        print('er zijn helaas geen kluizen beschikbaar op dit moment.')


def kluis_openen():
    kluis = input('welke kluis heeft u?: ')
    correct = 'onjuist antwoord'
    if kluis not in beschisckbareKluizen:
        code = input('wat is de code die u voor deze kluis heeft opgegeven?: ')

        for lines in open('codes.txt', 'r').read().splitlines():

            if (kluis + ' ' + code) == str(lines):
                print('correcte combinatie de kluis wordt geopend')
                correct = ''
    else:
        print('deze kluis is nog niet bezet.')

    print(correct)


def kluis_teruggeven():
    print('nog niet aan begonnen man')


keuze = ''
while keuze != '5':

    keuze = input(
        '''    1: Ik wil weten hoeveel kluizen er nog vrij zijn 
    2: Ik wil een nieuwe kluis 
    3: Ik wil even iets uit mijn kluis halen 
    4: Ik geef mijn kluis terug
    5: ik wil stoppen 
       voer een nummer in:''')

    if keuze == '1':
        toon_aantal_kluizen_vrij()
    elif keuze == '2':
        nieuwe_kluis()
    elif keuze == '3':
        kluis_openen()
    elif keuze == '4':
        kluis_teruggeven()
    elif keuze == '5':
        pass
    else:
        print('ongeldig antwoord')
