'''
    ax²+bx+c=0

    Possiveis entradas: x²; 5x²; -x²; -5x²; x²-3x+7; x²+7; x²+3x; -x²+7; -x²-3x
'''
import TADEq2g
import unittest

class TestTADEq2gInputs(unittest.TestCase):

    def test_umTermoSemCoeficiente(self):
        self.assertEqual(TADEq2g.cria('x^2'), {'A': 1})

    def test_umTermoComCoeficiente(self):
        self.assertEqual(TADEq2g.cria('5x^2'), {'A': 5})

    def test_umTermoSemCoeficienteNegativo(self):
        self.assertEqual(TADEq2g.cria('-x^2'), {'A': -1})

    def test_umTermoComCoeficienteNegativo(self):
        self.assertEqual(TADEq2g.cria('-5x^2'), {'A': -5})

    def test_doisTermosA_SemCoeficienteB_ComCoeficiente(self):
        self.assertEqual(TADEq2g.cria('x^2+3x'), {'A': 1, 'B': 3})



if __name__ == "__main__":
    unittest.main()