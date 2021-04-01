import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.emp = Employee('Test', 'Person', 50000, 1998)
    
    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp.email, 'Test.Person@email.com')
        
        self.emp.first = 'Test2'
        self.assertEqual(self.emp.email, 'Test2.Person@email.com')

    def test_age(self):
        self.assertEqual(self.emp.age, 23)
        
        del self.emp.age
        self.assertIsNone(self.emp.age)
        
    def test_instance(self):
        self.assertIsInstance(self.emp, Employee)

if __name__ == '__main__':
    unittest.main()