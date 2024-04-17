import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Shubham', 'Singh', 50000)
        emp_2 = Employee('Rahul', 'Singh', 60000)

        self.assertEqual(emp_1.email, 'Shubham@gmail.com')
        self.assertEqual(emp_2.email, 'Rahul@gmail.com')

        emp_1.first = 'Akshay'
        emp_2.first = 'Tejas'

        self.assertEqual(emp_1.email, 'Akshay@gmail.com')
        self.assertEqual(emp_2.email, 'Tejas@gmail.com')

    def test_fullname(self):
        emp_1 = Employee('Shubham', 'Singh', 50000)
        emp_2 = Employee('Rahul', 'Singh', 60000)

        self.assertEqual(emp_1.fullname, 'Shubham Singh')
        self.assertEqual(emp_2.fullname, 'Rahul Singh')

        emp_1.first = 'Dheeraj'
        emp_2.first = 'Mohit'

        self.assertEqual(emp_1.fullname, 'Dheeraj Singh')
        self.assertEqual(emp_2.fullname, 'Mohit Singh')

    def test_apply_raise(self):
        emp_1 = Employee('Shubham', 'Singh', 50000)
        emp_2 = Employee('Rahul', 'Singh', 60000)

        self.assertEqual(emp_1.apply_raise(), 55000)
        self.assertEqual(emp_2.apply_raise(), 66000)


if __name__ == '__main__':
    unittest.main()
