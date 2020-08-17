import unittest

from main import generate_password, validate, generate_forth_random_positions

class TestGeneratePassword(unittest.TestCase):

    def test_random_numbers_generation(self):
        """
        Test that return a list with 4 elements
        """
        random_numbers = generate_forth_random_positions(16)
        self.assertEqual(len(random_numbers), 4)
    
    def test_validation(self):
        """
        Test that the password generated is always secure
        """
        password = generate_password()
        result = validate(password)
        self.assertTrue(result)

    def test_that_always_return_secure_password(self):
        """
        Test that ALL the passwords generated are always secure
        """
        passwords = []
        for i in range(5000):
            pwd = generate_password()
            result = validate(pwd)
            passwords.append(result)
        
        print(passwords)
        validation = len(set(passwords)) == 1
        self.assertTrue(validation)

if __name__ == '__main__':
    unittest.main()