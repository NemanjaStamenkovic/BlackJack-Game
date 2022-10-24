import random
import os
clear = lambda: os.system('cls')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

gameIsFinished = False




def playGame():
    def drawCard():
        return random.randint(0, 12)
    
    playerCards = []
    computerCards = []

    def getPlayerCards():
        playerCards.append(cards[drawCard()])
        playerCards.append(cards[drawCard()])

    def getComputerCards():
        computerCards.append(cards[drawCard()])
        computerCards.append(cards[drawCard()])

    getPlayerCards()
    getComputerCards()
    playerScore = playerCards[0] + playerCards[1]
    computerScore = computerCards[0] + computerCards[1]
    print(f"Player Cards: {playerCards}")
    print(f"Computer Cards: {computerCards[0]}")
    if playerScore < 17:
        newCard = input("Type 'y' to get new card or 'n' to pass: ")
        if newCard == "y":
            playerCards.append(cards[drawCard()])
            playerScore = playerCards[0] + playerCards[1]+ playerCards[2]
            print(f"Your final Hand: {playerCards}, your final score: {playerScore}")
            print(f"Computer's final hand: {computerCards}, computer's final score: {computerScore}")
            if playerScore > computerScore and playerScore <= 21:
                print("You Win!!")
            elif playerScore > computerScore and playerScore > 21:
                print("You Loose!")
            elif computerScore > playerScore and computerScore > 21:
                print("You win")
            else: 
                print("You Loose!")
        else:
            print(f"Your final Hand: {playerCards}, your final score: {playerScore}")
            print(f"Computer's final hand: {computerCards}, computer's final score: {computerScore}")
            if playerScore > computerScore and playerScore <= 21:
                print("You Win!!")
            elif playerScore > computerScore and playerScore > 21:
                print("You Loose!")
            elif computerScore > playerScore and computerScore > 21:
                print("You win")
            else: 
                print("You Loose!")
    else: 
         newCard = input("Type 'y' to get new card or 'n' to pass: ")
         if newCard == "y":
            playerCards.append(cards[drawCard()])
            playerScore = playerCards[0] + playerCards[1]+ playerCards[2]
            print(f"Your final Hand: {playerCards}, your final score: {playerScore}")
            print(f"Computer's final hand: {computerCards}, computer's final score: {computerScore}")
            if playerScore > computerScore and playerScore <= 21:
                print("You Win!!")
            elif playerScore > computerScore and playerScore > 21:
                print("You Loose!")
            elif computerScore > playerScore and computerScore > 21:
                print("You win")
            else: 
                print("You Loose!")
         else:
            print(f"Your final Hand: {playerCards}, your final score: {playerScore}")
            print(f"Computer's final hand: {computerCards}, computer's final score: {computerScore}")
            if playerScore > computerScore and playerScore <= 21:
                print("You Win!!")
            elif playerScore > computerScore and playerScore > 21:
                print("You Loose!")
            elif computerScore > playerScore and computerScore > 21:
                print("You win")
            else: 
                print("You Loose!")


    

    

while not gameIsFinished:
    newGames = input("Play y/n?: ")
    if newGames == "y":
        clear()
        playGame()
    else:
        gameIsFinished = True

    
