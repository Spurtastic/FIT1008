

class Fighter():
    
    def __init__(self, life: int, experience: int) -> None:
        self.life = life
        self.experience = experience

    def is_alive(self) -> bool:
        # here the basic concept is to ensure that the fighter is alive
        if self.__life==0:
            return True 
        return False

    def lose_life(self, lost_life: int) -> None:
        pass
        # self.__life -= lost_life

    
    #This will be made an abstract class
    def get_life(self) -> int:
        pass
        # return self.__life

    def gain_experience(self, gained_experience: int) -> None:
        self.__experience +=gained_experience

    def get_experience(self) -> int:
        return self.__experience

    def get_speed(self) -> int:
        return self.__speed
        
    def get_cost(self) -> int:
        return self.__cost

    def get_attack_damage(self) -> int:
        return self.__damage

    def defend(self, damage: int) -> None:
        pass
        

    def get_unit_type(self) -> str:
        return self.unit_type 


    def __str__(self) -> str:
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
    def __init__(self, life: int, experience: int) -> None:
        self.__life = 3
        self.__experience = 0
        self.__unit_type = "Soldier"
    def get_life(self)-> int:
        return self.__life

    def get_experience(self) -> int:
        return self.__experience

    def get_unit_type(self) -> str:
        return self.__unit_type


    def defend(self, damage: int) -> None:
        if damage>self.experience:
            self.life-=1

    def cost(self)-> int:
        return 1
    
    def __str__(self) -> str:
        val= self.__unit_type +"'s life ="+str(self.life)+" experience = "+str(self.experience)+"\n" 
        return val

    

t2 = Soldier()
print(str(t2))


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



      

    

