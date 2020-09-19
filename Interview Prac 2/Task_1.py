class Fighter():
    
    def __init__(self, life: int, experience: int) -> None:
        self.life = 100
        self.experience = 0
        return life,

    def is_alive(self) -> bool:
        pass

    def lose_life(self, lost_life: int) -> None:
        pass

    def get_life(self) -> int:
        pass

    def gain_experience(self, gained_experience: int) -> None:
        pass

    def get_experience(self) -> int:
        pass

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