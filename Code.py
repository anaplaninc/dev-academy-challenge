
import random


#player class
class player():

    def __innit__(self,heldscore,unheldscore,name):
        self.name = name
        self.heldscore = heldscore
        self.unheldscore = unheldscore

    def updateScore(self, addition):
        self.score += addition
        
    def updateUnheldscore(self, addition):
        self.unheldscore += addition


class Game():

    def __innit__(self,currentPlayer,diceSize):
        self.currentPlayer = currentPlayer
        self.diceSize = diceSize
        self.winner = None

    
    def roll (player: player) -> int:
            try:
                rollInput = str(input(("Player 1 Press enter to roll")))
            except:
                print("Input Error")
            if rollInput == "":
                print ("Rolling")
                player.updateUnheldscore.updateScore(random.randint(1, self.diceSize))
                break  

    def checkWinner():
        if player.score > 100:
            return player
        else:
            return None
                

    
rolling = True



def Gameloop():

    #this needs input validation
    player1Name = str(input(("Input Player 1 Name (Enter for default)")))
    player2Name = str(input(("Input Player 2 Name (Enter for default))")))

    #default options for player names
    if player1Name.strip() == "":
        Player1 = player(0,0,"Player 1")
    else:
        Player1 = player(0,0,player1Name)


    if player2Name.strip() == "":
        Player2 = player(0,0,"Player 2")
    else:
        Player2 = player(0,0,player1Name)


    diceSize = int(input(("Please Input how large the die should be")))

    Game = Game(Player1,diceSize)

    while Game.Winner == None:

        Game.roll()
        Game.checkWinner()

        holdInput = str(input(("Hold or Roll again (H/R)")))
        if holdInput == "H":
            player.updateScore(player.updateUnheldscore)
            break
        elif holdInput == "R":
            print ("Rolling")
            Game.roll()
            Game.checkWinner()



    

