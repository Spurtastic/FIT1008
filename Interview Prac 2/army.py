"""
The below is created for the creation of an army elements. It has the Soldier, Archer and cavalry classes that inherit from a 
a fighter class with the abstract method defend.


"""

__author__ = "Ashwin Sarith"

class Fighter():
    

    def __init__(self, life: int, experience: int):
        """ Initialise life and experience of the fighter in question
        """
        self.life = life
        self.experience = experience
    
    def is_alive(self):
        """  Checks if the fighter is alive via a boolean 
        :pre: The fighter is alive
        :post: The fighter will be hurt and
        :complexity: Best and worst case is both O(1)

        """
        if self.__life>0:
            return True 
        return False

    def lose_life(self, lost_life: int):
        self.__life -= lost_life

    def get_life(self):
        return self.__life

    def gain_experience(self, gained_experience: int):
        self.__experience +=gained_experience

    def get_experience(self):
        return self.__experience

    def get_speed(self):
        return self.__speed
        
    def get_cost(self):
        return self.__cost

    def get_attack_damage(self):
        return self.__damage

    def defend(self, damage: int):
        pass
        

    def get_unit_type(self):
        return self.unit_type 


    def __str__(self):
        val= self.unit_type +"'s life ="+str(self.life)+" experience = "+str(self.experience)+"\n" 
        return val



# a soldier has {x}
# 3 life        
# 0 XP
# 1+ XP speed
# 1+ XP damage 
# if the damage recieved on this trooper is greater than the experience then the trooper will lose 1 life
# it costs 1 dollar



class Soldier(Fighter):
    life = 0
    experience = 0
    unit_type = "Soldier"
    cost = 1

    def __init__(self):
        self.experience= 0
        self.life      = 3


    def get_life(self):
        return self.__life

    def get_experience(self):
        return self.__experience

    def get_unit_type(self):
        return self.__unit_type


    def defend(self, damage: int):
        if damage>self.experience:
            self.life-=1
    
    def __str__(self):
        val= self.unit_type +"'s life = "+str(self.life)+" and experience = "+str(self.experience) 
        return val




"======================Archer====================================="

# an Archer has 
# 3 life
# 0 XP
# 3 speed
# 1+ XP damage 
#-1 life
# it costs 2 dollars

class Archer(Fighter):
    def __init__(self, life:int, experience: int) -> None:
        self.__life = 3
        self.__experience = 0  

    def defend(self, damage: int) -> None:
        if damage>0:
            self.life-=1

    def cost(self)-> int:
        return 2
"======================/====================================="
# a Cavalry has 
# 4 life
# 0 XP
# 2 speed
# 2*XP +1 damage 
# if the damage recieved on this trooper is greater than experience//2 then the trooper will lose 1 life
# it costs 3 dollars

class Cavalry(Fighter):
    def __init__(self, life:int, experience: int) -> None:
        self.__life = 4
        self.__experience = 0

    def defend(self, damage: int) -> None:
        if damage > self.experience//2:
            self.life-=1

    def cost(self)-> int:
        return 3



      

    

