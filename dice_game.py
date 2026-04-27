from random import randint

class Player:
    
    def __init__(self, name, score,turn,hold):
        self.name = name
        self.score = score
        self.turn = turn
        self.hold = hold
          
        def get_name(self, name):
            name = intput("what is your name: ")
            return name
            
        def get_turn(self, Player_turn):
            if Player_turn:
                return True
                
        def get_hold(self, hold):
            
            hold = input("Do you wnat to Hold [Y/N]: ")
            if hold == "Y":
                return True
            else:
                return False
            
        def get_score(self,num_score):
            score += num_score
            return score 

class Dice:
    def __init__(self, sides = 1, roll_dice):
        self.sides = sides
        self.roll_dice = self.roll_dice
        
    
    def roll_dice(self, roll):
        roll =randint(1,6)
        roll_result.append(roll)
        print(f'you rolled a {roll}')
        return roll_result
            

        
class Score:
    def __init__(self, current_score, total_score):
        self.current_score = current_score
        self.total_score = total_score
        
        
    def get_current_score(self, hold, score ):
        current_score = 0 
        if hold:
            self.current_score = score
        return current_score
        
    
    def get_total_score(self, current_score,total_score):
        total_score = []  
        if hold:
            total_score.append(score) 
        return total_score
        
        
        
        
        
        
        

class main:
    def __init__(self, Player, Dice, Score):
        pass
    
    print("Welocome to the dice rolling game")
    

    
    
    
    