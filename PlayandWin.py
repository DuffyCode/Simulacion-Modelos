import random

#constanstes
MAX_AMOUNT = 500
MIN_AMOUNT = 0

def startGame():
    initialMoney = validatorData("Capital inicial (minimo 100 - maximo 499):", 100, 499)
    minBet = validatorData(f"Apuesta minima (minimo 50 - maximo {initialMoney} ):", 50, initialMoney)

    inGame(initialMoney, minBet)

def validatorData(prompt, min, max):
    #Valida que el prompt sea un valor numerico valido.
    while True:
        try:
            value = int(input(prompt))
            if min <= value <= max:
                return value
            else:
                print(f'Valor fuera del rango establecido {min} - {max}!')
        except ValueError:
            print('Numero invalido!')

def inGame(initialMoney, minBet):
    
    earnedMoney = 0
    lostMoney = 0
    timesLoss = 0
    timesPlay = 0
    timesWon = 0

    #Valida que el jugador a un tenga dinero.
    #Valida que no haya alcanzado el limite maximo de ganancias.
    while MIN_AMOUNT < initialMoney and earnedMoney < MAX_AMOUNT:
        number = random.randint(1, 6)
        result = numberResult(number)

        if result:
            earnedMoney += minBet
            initialMoney += minBet
            timesWon += 1
        else:
            lostMoney += minBet
            initialMoney -= minBet
            timesLoss += 1

        timesPlay += 1

    endGame(initialMoney, earnedMoney, lostMoney, timesLoss, timesPlay, timesWon)

def numberResult(number):
    #valida si es par o impar
    return number %2 == 0

def endGame(initialMoney, earnedMoney, lostMoney, timesLoss, timesPlay, timesWon):
    #resultados de la partida
    if initialMoney <= 0:
        print(f'HAS PERDIDO TODO AMIGO...! DEBES {initialMoney}')
    
    if earnedMoney >= MAX_AMOUNT:
        print(f'LIMITE DE GANANCIAS POR PARTIDA ALCANZADO EN HORA BUENA...! ACUMULASTE {earnedMoney}')

    print(f'Ganacias: {(initialMoney + earnedMoney) - lostMoney}, Perdidas: {lostMoney}') 
    print(f'Victorias: {timesWon}, ({timesWon/timesPlay*100:.2f}%)')
    print(f'Derrotas: {timesLoss}, ({timesLoss/timesPlay*100:.2f}%)')
    print(f'Rondas: {timesPlay}')

if __name__ == "__main__":
    startGame()