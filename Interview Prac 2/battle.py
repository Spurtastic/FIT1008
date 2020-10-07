
"====================== task 4 ============================="
from army import Army
from abc import ABC, abstractmethod
class Battle():
    
    def gladiatorial_combat(self, player_one: str, player_two: str):
        player_one_army = Army
        player_one_army.choose_army(player_one_army, "Player 1", 0)
        player_one = player_one_army.name
        player_two_army = Army
        player_two_army.choose_army(player_two_army,"Player 2", 0)
        player_two = player_two_army.name

        
        self.player_one = player_one
        self.player_two = player_two

        self.__conduct_combat(self,player_one_army,player_two_army,0)

   


       

    def __conduct_combat(self, army1: Army, army2: Army, formation: int):

        if formation == 0:
           U1 = army1.pop()
           U2 = army2.pop()
           
        print("\nplayer 1 = "+self.player_one)
        print("player 2 = "+self.player_two)

import sys
class Test(ABC):
    def test_function(self):
        sys.stdin = open("tester.txt")
        Battle.gladiatorial_combat(Battle, "", "")
    def setup_method(self):
        self.orig_stdin = sys.stdin

    def teardown_method(self):
        sys.stdin = self.orig_stdin


if __name__ == "__main__":
    Test.test_function(Battle)