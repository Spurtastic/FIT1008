
class Fighter():
    
    def __init__(self, life: int, experience: int) -> None:
        self.__life = 100
        self.__experience = 0


    def is_alive(self) -> bool:
        # here the basic concept is to ensure that the fighter is alive testing kraken
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
        pass

    def get_cost(self) -> int:
        pass

    def get_attack_damage(self) -> int:
        pass

    def defend(self, damage: int) -> None:
        pass

    def get_unit_type(self) -> str:
        pass

    def __str__(self) -> str:
        pass