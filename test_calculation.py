import unittest
import calculation

class TestCalculation(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        print('\nsetUpClass')
    
    @classmethod
    def tearDownClass(self):
        print('\ntearDownClass')
    
    def setUp(self):
        print('\nsetUp')
    
    def tearDown(self):
        print('tearDown')
    
    def test_add(self):
        print('test_add')
        self.assertEqual(calculation.add(10, 5), 15)
        self.assertEqual(calculation.add(-1, 1), 0)
        self.assertEqual(calculation.add(-2, -2), -4)
        
    def test_subtract(self):
        print('test_subtract')
        self.assertEqual(calculation.subtract(10, 5), 5)
        self.assertEqual(calculation.subtract(-1, 1), -2)
        self.assertEqual(calculation.subtract(-2, -2), 0)
        
        
    def test_multiply(self):
        print('test_multiply')
        self.assertEqual(calculation.multiply(10, 5), 50)
        self.assertEqual(calculation.multiply(-1, 1), -1)
        self.assertEqual(calculation.multiply(-2, -2), 4)
        
        
    def test_divide(self):
        print('test_divide')
        self.assertEqual(calculation.divide(10, 5), 2)
        self.assertEqual(calculation.divide(-1, 1), -1)
        self.assertEqual(calculation.divide(-2, -2), 1)
        
        self.assertRaises(ValueError, calculation.divide, 10, 0)
        
        with  self.assertRaises(ValueError):
            calculation.divide(10, 0)

if __name__ == '__main__':
    unittest.main()