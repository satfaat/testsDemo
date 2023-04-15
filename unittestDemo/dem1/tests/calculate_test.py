import unittest

from calc.calculate import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self) -> None:
        self.assertEqual(4, self.calc.add(2, 2))


if __name__ == '__main__':
    unittest.main()
