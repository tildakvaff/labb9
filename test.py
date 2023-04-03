#unittest för labb 8


import unittest

from s3 import *


class SyntaxTest(unittest.TestCase):


#SAMPLE 1
    def test1(self):
        self.assertEqual(dela_upp_molekyl("Na"), "Formeln är syntaktiskt korrekt")

    def test2(self):
        self.assertEqual(dela_upp_molekyl("H2O"), "Formeln är syntaktiskt korrekt")

    def test3(self):
        self.assertEqual(dela_upp_molekyl("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")

    def test4(self):
        self.assertEqual(dela_upp_molekyl("Na332"), "Formeln är syntaktiskt korrekt")

#SAMPLE 2


    def test5(self):
        self.assertEqual(dela_upp_molekyl("C(Xx4)5"), "Okänd atom vid radslutet 4)5")

    def test6(self):
        self.assertEqual(dela_upp_molekyl("C(OH4)C"), "Saknad siffra vid radslutet C")


    def test7(self):
        self.assertEqual(dela_upp_molekyl("C(OH4C"), "Saknad högerparentes vid radslutet ")


    def test8(self):
        self.assertEqual(dela_upp_molekyl("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")

    def test9(self):
        self.assertEqual(dela_upp_molekyl("H0"), "För litet tal vid radslutet ")

    def test10(self):
        self.assertEqual(dela_upp_molekyl("H1C"), "För litet tal vid radslutet C")

    def test11(self):
        self.assertEqual(dela_upp_molekyl("H02C"), "För litet tal vid radslutet 2C")

    def test12(self):
        self.assertEqual(dela_upp_molekyl("Nacl"), "Saknad stor bokstav vid radslutet cl")

    def test13(self):
        self.assertEqual(dela_upp_molekyl("a"), "Saknad stor bokstav vid radslutet a")
    
    def test14(self):
        self.assertEqual(dela_upp_molekyl("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")

    def test15(self):
        self.assertEqual(dela_upp_molekyl(")"), "Felaktig gruppstart vid radslutet )")

    def test16(self):
        self.assertEqual(dela_upp_molekyl("2"), "Felaktig gruppstart vid radslutet 2")




if __name__ == '__main__':
    unittest.main()