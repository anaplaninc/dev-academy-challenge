import random
going = True


class player():
    #Create player state
    #set players name
    def __init__(self, name):
        self.unheld = 0
        self.score = 0
        self.endturn = True
        self.name = name
    #roll
    #automatically toggles endturn flag if landed on a one
    def roll(self):
        num = random.randint(1,6)
        if num == 1:
            self.unheld = 0
            self.endturn = True
            print("uh oh!!! you rolled a 1! your turn has ended")
            print("\n")
        else:
            self.unheld += num
        return num

    #rolls then asks if the player wants a reroll
    #if the player initially rolls a one, end the turn
    def ask(self):
        print("it is " + self.name + "'s go!")
        self.num = self.roll()
        if self.endturn:
            return None
        print("you rolled a " + str(self.num) + ", your current un-held score is: " +  str(self.unheld) + ", total score: " + str(self.score))
        inp = input("do you want to roll again: y/n: ")
        if inp.lower() == "y":
            self.endturn = False
        elif inp.lower() == "n":
            self.score += self.unheld
            self.unheld = 0
            self.endturn = True
            print(self.name + "'s turn has ended")
            print("\n")
        else:
            print("Not a valid input, your turn will be ended")
            self.score += self.unheld
            self.unheld = 0
            self.endturn = True
            print(self.name + "'s turn has ended")
            print("\n")
    
    #called for each players "go"
    #ends when flag is set
    def go(self):
        self.endturn = False
        while self.endturn == False:
            self.ask()


#setup player instances
replay = True
while replay:
    p1name = input("player 1 name? ")
    p2name = input("player 2 name? ")
    p1 = player(p1name)
    p2 = player(p2name)
    
    #loop till done
    #not sure if should allow the player to reroll if they already would win, decided to keep it in becasue it could be a fun taunt for a player to use against the other player
    while p1.score < 100 and p2.score < 100:
        p1.go()
        p2.go()
        #displays game state every turn
        print("\n ---------------------- \n")
        print("CURRENT PLAYER SCORES \n "+ p1.name +": " + str(p1.score) + ", " + p2.name + ": " + str(p2.score))
        print("\n ---------------------- \n")
    
    
    if p1.score > p2.score:
        print("PLAYER 1 WINS")
    else:
        print("PLAYER 2 WINS")
    
    if input("replay? y/n: ").lower() == 'n':
        replay = False
