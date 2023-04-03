from unittest import TestCase, main
from .env/calculator import Calculator

class TestCalculatrice(TestCase):

#region Tests - BDD - Addition, Soustraction, Multiplication, Division, Calcul d'un pourcentage
    def test_add_two_numbers(self):
        self.assertEqual(Calculator.calculate("2+2"), 4)

    def test_substract_two_numbers(self):
        self.assertEqual(Calculator.calculate("2-2"), 0)

    def test_multiply_two_numbers(self):
        self.assertEqual(Calculator.calculate("2*2"), 4)

    def test_divide_two_numbers(self):
        self.assertEqual(Calculator.calculate("8/2"), 4)

    def test_divide_by_zero(self):
        self.assertEqual(Calculator.calculate("8/0"), "Division par zéro impossible")

    def test_add_two_numbers_with_spaces(self):
        self.assertEqual(Calculator.calculate("2 + 2"), 4)

    def test_substract_two_numbers_with_spaces(self):
        self.assertEqual(Calculator.calculate("2 - 2"), 0)

    def test_multiply_two_numbers_with_spaces(self):
        self.assertEqual(Calculator.calculate("2 * 2"), 4)

    def test_divide_two_numbers_with_spaces(self):
        self.assertEqual(Calculator.calculate("8 / 2"), 4)

    def test_divide_by_zero_with_spaces(self):
        self.assertEqual(Calculator.calculate("8 / 0"), "Division par zéro impossible")

    def test_add_three_numbers(self):
        self.assertEqual(Calculator.calculate("2+4+5"), 11)

    def test_substract_three_numbers(self):
        self.assertEqual(Calculator.calculate("2-4-5"), -7)

    def test_multiply_three_numbers(self):
        self.assertEqual(Calculator.calculate("2*4*5"), 40)

    def test_divide_three_numbers(self):
        self.assertEqual(Calculator.calculate("8/4/2"), 1)

    def test_add_a_number_to_a_multiplication(self):
        self.assertEqual(Calculator.calculate("2+4*5"), 22)

    def test_add_a_number_to_a_division(self):
        self.assertEqual(Calculator.calculate("2+8/4"), 4)

    def test_substract_a_number_to_a_multiplication(self):
        self.assertEqual(Calculator.calculate("2-4*5"), -18)

    def test_substract_a_number_to_a_division(self):
        self.assertEqual(Calculator.calculate("2-8/4"), 0)

    def test_add_a_number_to_an_addition(self):
        self.assertEqual(Calculator.calculate("2+(4+5)"), 11)

    def test_add_a_number_to_a_substraction(self):
        self.assertEqual(Calculator.calculate("2+(4-5)"), 1)

    def test_substract_a_number_to_an_addition(self):
        self.assertEqual(Calculator.calculate("2-(4+5)"), -7)

    def test_substract_a_number_to_a_substraction(self):
        self.assertEqual(Calculator.calculate("2-(4-5)"), 3)

    def test_multiply_a_number_to_an_addition(self):
        self.assertEqual(Calculator.calculate("2*(4+5)"), 18)

    def test_multiply_a_number_to_a_substraction(self):
        self.assertEqual(Calculator.calculate("2*(4-5)"), -2)

    def test_divide_a_number_to_an_addition(self):
        self.assertEqual(Calculator.calculate("2/(4+5)"), 0.2222222222222222)

    def test_divide_a_number_to_a_substraction(self):
        self.assertEqual(Calculator.calculate("2/(4-5)"), -2)  

    def test_add_none_to_none(self):
        with self.assertRaises(IndexError):
            Calculator.calculate("None + None")
#endregion

#region Tests - BDD - Puissance/carré d'un nombre et racine carré 
    def test_number_with_power(self):
        self.assertEqual(Calculator.calculate("8^2"), 64)

    def test_number_with_power_and_spaces(self):
        self.assertEqual(Calculator.calculate("8 ^ 2"), 64)

    def test_number_with_power_and_spaces_and_addition(self):
        self.assertEqual(Calculator.calculate("8 ^ 2 + 2"), 66)

    def test_number_with_power_and_spaces_and_substraction(self):
        self.assertEqual(Calculator.calculate("8 ^ 2 - 2"), 62)
    
    def test_number_with_power_and_spaces_and_multiplication(self):
        self.assertEqual(Calculator.calculate("8 ^ 2 * 2"), 128)

    def test_number_with_power_and_spaces_and_division(self):
        self.assertEqual(Calculator.calculate("8 ^ 2 / 2"), 32)

    def test_number_with_power_and_additional_priority(self):
        self.assertEqual(Calculator.calculate("8 ^ 2 + (2 + 2)"), 68)
    
    def test_number_with_power_and_substraction_priority(self):
        self.assertEqual(Calculator.calculate("8 ^ 2 - (2 + 2)"), 60)

    def test_percentage_two_numbers(self):
        self.assertEqual(Calculator.calculate("80%50"), 40)

    def test_percentage_two_numbers_with_spaces(self):
        self.assertEqual(Calculator.calculate("60 % 2"), 1.2)

    def test_percentage_two_numbers_with_spaces_and_addition(self):
        self.assertEqual(Calculator.calculate("60 % 20 + 2"), 14)
    
    def test_percentage_two_numbers_with_spaces_and_substraction(self):
        self.assertEqual(Calculator.calculate("60 % 20 - 2"), 10)

    def test_squareroot_in_addition(self):
        self.assertEqual(Calculator.calculate("2+√4"), 4)

    def test_squareroot_in_substraction(self):
        self.assertEqual(Calculator.calculate("2-√4"), 0)
    
#endregion

main()  
