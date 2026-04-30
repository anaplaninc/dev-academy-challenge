import pytermgui as ptg

CONFIG = """
config:
    InputField:
        styles:
            prompt: dim italic
            cursor: '@72'
    Label:
        styles:
            value: dim bold

    Window:
        styles:
            border: '60'
            corner: '60'

    Container:
        styles:
            border: '96'
            corner: '96'
"""

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
    
    #called for each players "go"
    #ends when flag is set
    def go(self):
        self.endturn = False
        while self.endturn == False:
            self.ask()


#setup player instances
#p1name = input("player 1 name? ")
#p2name = input("player 2 name? ")
#loop till done
#not sure if should allow the player to reroll if they already would win, decided to keep it in becasue it could be a fun taunt for a player to use against the other player
#while p1.score < 100 and p2.score < 100:
#    p1.go()
#    p2.go()
#    #displays game state every turn
#    print("\n ---------------------- \n")
#    print("CURRENT PLAYER SCORES \n "+ p1.name +": " + str(p1.score) + ", " + p2.name + ": " + str(p2.score))
#    print("\n ---------------------- \n")


OUTPUT = {}


def submit(manager: ptg.WindowManager, window: ptg.Window) -> None:
    for widget in window:
        if isinstance(widget, ptg.InputField):
            OUTPUT[widget.prompt] = widget.value
            continue

        if isinstance(widget, ptg.Container):
            label, field = iter(widget)
            OUTPUT[label.value] = field.value

    manager.stop()

with ptg.YamlLoader() as loader:
    loader.load(CONFIG)

with ptg.WindowManager() as manager:
    window = (
        ptg.Window(
            "",
            ptg.InputField("PLAYER 1", prompt="Name: "),
            "",
            "",
            ["Submit", lambda *_: submit(manager, window)],
            width=60,
            box="DOUBLE",
        )
        .set_title("[210 bold]New contact")
        .center()
    )

    manager.add(window)


p1 = player(OUTPUT["Name: "])
print(p1.name)
#p2 = player(p2name)


OUTPUT = {}

with ptg.YamlLoader() as loader:
    loader.load(CONFIG)

with ptg.WindowManager() as manager:
    window = (
        ptg.Window(
            "",
            ptg.InputField("PLAYER 2", prompt="Name: "),
            "",
            "",
            ["Submit", lambda *_: submit(manager, window)],
            width=60,
            box="DOUBLE",
        )
        .set_title("Player 1 name choice")
        .center()
    )

    manager.add(window)

window.select(1)

p2 = player(OUTPUT["Name: "])
print(p2.name)
exit()
#p2 = player(p2name)




#while p1.score < 100 and p2.score < 100:
#    p1.go()
#    p2.go()
#    #displays game state every turn
#    print("\n ---------------------- \n")
#    print("CURRENT PLAYER SCORES \n "+ p1.name +": " + str(p1.score) + ", " + p2.name + ": " + str(p2.score))
#    print("\n ---------------------- \n")
#
#
#
#if p1.score > p2.score:
#    print("PLAYER 1 WINS")
#else:
#    print("PLAYER 2 WINS")


