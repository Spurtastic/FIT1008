"""
Testing file for Question 4 of Interview Prac 2

__author__ = "Maria Garcia de la Banda"
__edited__ = "Ben Di Stefano"
"""

import unittest
from army import Archer, Soldier, Cavalry, Army
from battle import Battle


class TestTask4(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = "+str(len(self.verificationErrors)))

    def test___conduct_combat(self):
        t1 = Army()
        t2 = Army()
        battle = Battle()
        formation = 0 

        # Test if combat is conducted correctly and returns appropriate result for empty p1 army and all Archer p2 army
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 0, 0, 0, formation)
        t2._Army__assign_army("", 0, 10, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2, "Gladiatorial 0,0,0 0,10,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # your tests for __conduct_combat go here
        t1._Army__assign_army("", 1, 0, 0, formation)

        t2._Army__assign_army("", 0, 1, 0, formation)
        battle._Battle__conduct_combat(t1, t2, formation)

        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 0, "Gladiatorial 1,0,0 0,1,0 failed")
            self.assertEqual(str(t2.force), "Archer's life = 1 and experience = 1", msg="String test 1,1,1 failed")

        except AssertionError as e:
            self.verificationErrors.append(str(e))

        t1._Army__assign_army("", 7, 4, 3, formation)
        t2._Army__assign_army("", 8, 5, 3, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2, "Gladiatorial 7,4,5,8,5,3failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask4)
    unittest.TextTestRunner(verbosity=0).run(suite)
