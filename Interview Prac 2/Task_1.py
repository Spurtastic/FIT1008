
class Fighter():
    
    def __init__(self, life: int, experience: int) -> None:
        self.__life = 100
        self.__experience = 0



    def is_alive(self) -> bool:
        # here the basic concept is to ensure that the fighter is alive
        if self.__life==0:
            return True 
        return False

    def lose_life(self, lost_life: int) -> None:
        self.__life -= lost_life


    def get_life(self) -> int:
        return self.__life

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
        if damage>0:
            pass
        

    def get_unit_type(self) -> str:
        pass

    def __str__(self) -> str:
        pass
