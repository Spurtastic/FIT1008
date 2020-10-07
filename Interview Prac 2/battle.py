
"====================== task 4 ============================="
from army import*
from abc import ABC, abstractmethod
from stack_adt import ArrayStack
class Battle():
    
    def gladiatorial_combat(self, player_one: str, player_two: str):
        
        self.player_one = player_one
        self.player_two = player_two

        player_one_army = Army()
        player_two_army = Army()
        


        self.__conduct_combat(player_one_army,player_two_army,0)

   


       

    def __conduct_combat(self, army1: Army, army2: Army, formation: int):
        if formation == 0:
            
            # while the armies are not empty
            while not (army1.force.is_empty() & army2.force.is_empty()):      
                u1 = army1.force.pop()
                u2 = army2.force.pop()

            # the unit thats the fastest attacks first
                if u1.get_speed() > u2.get_speed():
                    u2.defend(u1.get_attack_damage())
                    if u2.is_alive():
                        u1.defend(u2.get_attack_damage())
                elif u2.get_speed() > u1.get_speed():
                    u1.defend(u2.get_attack_damage())
                    if u1.is_alive():
                        u2.defend(u1.get_attack_damage())

            # if both are the same speed then both attack each other
                elif u2.get_speed() == u1.get_speed():
                    u1.defend(u2.get_attack_damage())
                    u2.defend(u1.get_attack_damage())

            # if one of them is dead then the surviving one gets experience
                if u1.is_alive() and not u2.is_alive():
                    u1.gain_experience(1)
                    army1.force.push(u1)
            # vice versa
                elif not u1.is_alive() and u2.is_alive():
                    u2.gain_experience(1)
                    army2.force.push(u2)

            # if both are alive after the fight
                elif u1.is_alive() and u2.is_alive():
                    u1.gain_experience(1)
                    print(u1)
                    u2.gain_experience(1)
                    print(u2)
                    army1.force.push(u1)
                    army2.force.push(u2)

            # if at least one of the armies are empty then end the code
                if army1.force.is_empty() or army2.force.is_empty():
                    if army1.force.is_empty():
                        ret = (f"Player {army1.name} won!")
                        return 1
                    else:
                        ret = (f"Player {army2.name} won!")
                        print(ret)
                        return 2
                elif army1.force.is_empty() and army2.force.is_empty():
                    return 0
                
def main():
    t1 = Army()
    t2 = Army()
    battle = Battle()
    formation = 0

    # Test if combat is conducted correctly and returns appropriate result for empty p1 army and all Archer p2 army
    # Assumes __assign_army is working correctly
    print(t1._Army__assign_army("", 0, 0, 0, formation))
    t2._Army__assign_army("", 0, 10, 0, formation)

if __name__ == "__main__":

    main()
               
 