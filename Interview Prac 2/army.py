"""
The below is created for the creation of an army elements. It has the Soldier, Archer and cavalry classes that inherit from a 
a fighter class with the abstract method defend.


"""

__author__ = ""


# implemented classes and their methods below here
class Fighter():
    # Initialised common values for the subclasses
    life = 3
    experience = 0
    damage = 0

    def __init__(self, life: int, experience: int):
        """ Initialise life and experience of the fighter in 
        
        :pre: life and experience must be >= 0 
        :post: Values cannot be modified here
        :return: None
        """
        self.life = life
        self.experience = experience
    
    def is_alive(self):
        """  Checks if the fighter is alive via a boolean 
        :return: None
        :complexity: Best and worst case is both O(1)
        """
        if self.life>0:
            return True 
        return False

    def lose_life(self, lost_life: int):
        """Here health deduction is implemented, lost life will be a result of damage
        
        :param lost_life: life to be deducted from the life of the specific fighter
        :return: None
        """
        self.life -= lost_life

    
    def gain_experience(self, gained_experience: int):
        """Unit experience increased  by the value gained_experience

        :pre: gained_experience >= 0
        :post: experience added and greater
        :param gained_experience: The experience to be added to fighter's experience
        :return: the integer value for lifge of the fighter"""
        self.experience +=gained_experience

    def get_life(self):
        """returns the fighters life

        :return: the integer value for life of the fighter"""
        return self.life


    def get_experience(self):
        """returns fighters experience

        :return: the integer value for experience of the fighter"""
        return self.experience

    def get_speed(self):
        """returns fighters speed but is an abstract method

        :return: None"""
        pass
        
    def get_cost(self):
        """returns fighters cost

        :return: the integer value for cost of the fighter"""
        return self.cost

    def get_attack_damage(self):
        self.damage = 1 + self.experience
        return self.damage

    def defend(self, damage: int):
        pass
        

    def get_unit_type(self):
        return self.unit_type 


    def __str__(self):
        val= self.unit_type +"'s life = "+str(self.life)+" experience = "+str(self.experience)+"\n" 
        return val

"======================Soldier====================================="

class Soldier(Fighter):
    unit_type = "Soldier"
    cost = 1
    def __init__(self):
        self.life    
        self.experience 
    
    def get_speed(self):
        return 1 + self.experience

    def defend(self, damage: int):
        if damage>self.experience:
            self.lose_life()

            
    





"======================Archer====================================="



class Archer(Fighter):
    # life = 0
    # experience = 0
    unit_type = "Archer"
    cost = 2


    def __init__(self):
        self.experience 
        self.life      
    
    def get_speed(self):
        return 3

    def defend(self, damage: int):
        if damage>0:
            self.lose_life()
    


"======================Cavalry====================================="

class Cavalry(Fighter):
    unit_type = "Cavalry"
    cost = 3

    def __init__(self):
        self.experience
        self.life       = 4

    def get_speed(self):
        return 2

    def get_attack_damage(self):
        return 2*self.experience + 1 

    def defend(self, damage: int):
        if damage>self.experience//2:
            self.lose_life



def main():
    #testing speed

    # s1 = Soldier()
    # print(s1.get_attack_damage())
    # s2 = Archer()
    # print(s2.get_attack_damage())
    # s3 = Cavalry()
    # print(s3.get_attack_damage())

    # s1 = Soldier()
    # print(s1.get_life())
    # s2 = Archer()
    # print(s2.get_life())
    # s3 = Cavalry()
    # print(s3.get_life())
    
    # s1 = Soldier()
    # print(s1.get_experience())
    # s2 = Archer()
    # print(s2.get_experience())
    # s3 = Cavalry()
    # print(s3.get_experience())
    
    s1 = Soldier()
    print(str(s1))
    
    s2 = Archer()
    print(str(s2))

    s3 = Cavalry()
    print(str(s3))
    

if __name__ == "__main__":
    main()



# Future implmentations

# class Army:


      

    

