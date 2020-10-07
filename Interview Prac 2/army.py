"""
The below is created for the creation of an army elements. It has the Soldier, Archer and cavalry classes that inherit from a 
a fighter class with the abstract method defend.


"""

__author__ = "Ashwin Sarith"


# implemented classes and their methods below here
from abc import ABC, abstractmethod
from queue_adt import CircularQueue
from stack_adt import ArrayStack

class Fighter(ABC):

    def __init__(self, life: int, experience: int):
        """ Initialise life and experience of the fighter in 
        
        :pre: life and experience must be >= 0 
        :return: None
        """
        self.life = life
        self.experience = experience
        assert self.life >= 0 , " life cant be negative"
        assert self.experience >= 0 , "experience cant be negative"
           

    
    def is_alive(self):
        """  Checks if the fighter is alive via a boolean 
        :return: Boolean
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
        self.lost_life = lost_life
        if lost_life<=0:
            raise ValueError("Needs to be a positive value")
        else:
            self.life = self.life - self.lost_life
            
        
    
    def gain_experience(self, gained_experience: int):
        """Unit experience increased  by the value gained_experience

        :pre: gained_experience >= 0
        :post: experience added and greater
        :param gained_experience: The experience to be added to fighter's experience
        :return: the integer value for lifge of the fighter"""
        
        if gained_experience<=0:
            raise ValueError("Experience cannot be negative")
        else:
            self.experience += gained_experience


    def get_life(self):
        """returns the fighters life

        :return: the integer value for life of the fighter"""
        return self.life


    def get_experience(self):
        """returns fighters experience

        :return: the integer value for experience of the fighter"""
        return self.experience

        
    def get_cost(self):
        """returns fighters cost

        :return: the integer value for cost of the fighter"""
        return self.cost

    def get_attack_damage(self):
        """returns attack damage

        :return: the int value for damage with respect to the experience.
        """
        self.damage = 1 + self.experience
        return self.damage
    
    def get_unit_type(self):
        """returns the string unit type
        
        :return: str unit_type
        """
        return self.unit_type 

    @abstractmethod
    def get_speed(self):
        """is an abstract method"""
        pass
    
    @abstractmethod
    def defend(self, damage: int):
        """is an abstract method"""
        pass

    def __str__(self):
        """just for the classes description"""
        val= self.unit_type +"'s life = "+str(self.life)+" and experience = "+str(self.experience)
        return val
        

"====================== Task 2 ====================================="

class Soldier(Fighter):
    unit_type = "Soldier"
    cost = 1
    
    def __init__(self):
        """retrieves init method from Fighter and is initialised with the fighters value
        
        :return: None
        """
        super().__init__(3,0)
    
    def get_speed(self):
        """returns the speed of a soldier with respect to its experience
        
        :returns: integer value for speed
        """
        return 1 + self.experience

    def defend(self, damage: int):
        """ A method to invoke defense with damage as input
        :param damage: is the integer for damage thats inflicted on the unit
        :returns: None
        """
        if damage>self.experience:
           self.life -= 1








class Archer(Fighter):

    unit_type = "Archer"
    cost = 2

    def __init__(self):
        """retrieves init method from Fighter and is initialised with the fighters value
        
        :return: None
        """
        super().__init__(3,0)
             
    def get_speed(self):
        """returns the speed of a soldier with respect to its experience
        
        :returns: integer value for speed
        """
        return 3

    def defend(self, damage: int):
        """ A method to invoke defense with damage as input
        :param damage: is the integer for damage thats inflicted on the unit
        :returns: None
        """
        if damage>0:
            self.life -=1





class Cavalry(Fighter):
    unit_type = "Cavalry"
    cost = 3

    def __init__(self):
        """retrieves init method from Fighter and is initialised with the fighters value
        
        :return: None
        """
        super().__init__(4,0)

    def get_speed(self):
        """returns the speed of a soldier with respect to its experience
        
        :returns: integer value for speed
        """
        self.speed = 2
        return self.speed

    def get_attack_damage(self):
        """Used to retrieve the attack damage for a class
        :returns: damage scaled to unit experience """
        self.attack = (2*self.experience) + 1 
        return self.attack

    def defend(self, damage: int):
        if damage>(self.experience)//2:
            self.life -=1


"====================== Task 3 ====================================="
class Army(Soldier, Archer, Cavalry, ABC):
    
    def __init__(self):
        " first we initialise the names and the fighting force0"
        self.name = None
        self.force = None

    def __correct_army_given(self, soldiers:int, archers:int, cavaliers:int):
        s = Soldier()
        a = Archer()
        c = Cavalry()
        
        total_cost = (s.cost*soldiers) + (a.cost*archers) + (c.cost*cavaliers)


        if soldiers >= 0 and archers >= 0 and cavaliers >=0 and total_cost <=30:
            return True
        else:
            return False
         
    
    def __assign_army(self, name:str, sold: int, arch: int, cav:int, formation: int):      

        if formation == 0:
            stack_size = sold + arch + cav
            force = ArrayStack(stack_size)
            #Soldier
            s = Soldier()
            #Archer
            a = Archer()
            #Cavalry
            c = Cavalry()
            
            index = 0
            while index != sold:
                force.push(s)
                index+=1  
            
            index = 0
            while index != arch:
                force.push(a)
                index+=1
            
            index = 0       
            while index != cav:
                force.push(c)
                index+=1
            self.force = force
            self.name = name
        else: 
            queue_size = sold +arch +cav
            force = CircularQueue(queue_size)

            s = Soldier()
            a = Archer()
            c = Cavalry()
            
            index = 0
            while index != sold:
                force.append(s)
                index+=1
            index = 0
            while index != arch:
                force.append(a)
                index+=1
            
            index = 0
            while index != cav:
                force.append(c)
                index+=1
            self.force = force
            self.name =  name



    def choose_army(self, name:str, formation:int):
        """
        docstring
        """ 
        self.name = name 
        x = 1
        SAC = []
        while x<4:
            if x == 1:
                SAC.append(int(input("Player "+self.name+" Number of Soldiers? ")))
                x+=1
            elif x == 2:
                SAC.append(int(input("Player "+self.name+" Number of Archers? ")))
                x+=1
            elif x == 3:
                SAC.append(int(input("Player "+self.name+" Number of Cavalry men? ")))
                x+=1
            else:
                x+=1
        Soldiers = SAC[0]
        Archers = SAC[1]
        Cavalries = SAC[2]
        
        if self.__correct_army_given(Soldiers, Archers, Cavalries) is True:
            self.__assign_army( self.name, Soldiers, Archers, Cavalries, formation)
            
    
    def __str__(self) -> str:
        return str(self.force)







      

    

