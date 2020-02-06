"""Beregning av sannsynligheter basert på ordnet/uordnet utvalg og med/uten tilbakelegging."""

from math import factorial

# Funksjoner
def ordnet_med_komb(numAlt, numValg):
    return numAlt ** numValg
def ordnet_uten_komb(numAlt, numValg):
    return factorial(numAlt)/factorial(numAlt-numValg)
def uordnet_uten_komb(numAlt, numValg):
    return factorial(numAlt)/(factorial(numValg)*factorial(numAlt-numValg))
def bayes(A, B, BA):
    AB = float(BA) * float(A) / float(B)
    return AB

# Main
boolean = True
while boolean:
    command = input('Bayes eller valg?: ')
    if command == 'valg':
        orden = input('Er valget ordnet eller uordnet?: ')
        tilbakelegging = input('Er valget med eller uten tilbakelegging?: ')
        numAlt = int(input('Skriv inn antall alternativer: '))
        numValg = int(input('Skriv inn antall utvalg: '))

        if orden == 'ordnet' and tilbakelegging == 'med':
            ordmed = ordnet_med_komb(numAlt, numValg)
            print ("Antall kombinasjoner er: " + str(ordmed))
        elif orden == 'ordnet' and tilbakelegging == 'uten':
            if numAlt != 0:
                ordnetUten = ordnet_uten_komb(numAlt, numValg)
                print ("Antall permutasjoner er " + str(ordnetUten))
            else:
                print (1 / factorial(numAlt - numValg))
        elif orden == 'uordnet' and tilbakelegging == 'med':
            print ("Dette alternativet er foreløpig utilgjengelig.")
        elif orden == 'uordnet' and tilbakelegging == 'uten':
            uordnetUten = uordnet_uten_komb(numAlt, numValg)
            print ("Antall kombinasjoner er " + str(uordnetUten))
        else:
            print ('Vennligst skriv inn enten "ordnet" eller "uordnet" i det første alternativet, '
            '"med" eller "uten" i det andre, '
            'og reelle tall i det tredje og fjerde.')
    elif command == 'bayes':
        a_input = input("Enter P(A): ")
        b_input = input("Enter P(B): ")
        ba_input = input("Enter P(B|A): ")
        output = bayes(a_input, b_input, ba_input)
        output_perc = output * 100

        print("P(A|B) is %.2f or %.2f"  %(output, output_perc), "%")
    elif command == 'exit':
        boolean = False