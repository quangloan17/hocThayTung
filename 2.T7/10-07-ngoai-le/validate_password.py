import unittest
    #TODO - Mk >=6 Kí tự
    #     - Mk chứa chữ cái
    #     - Mk chứa chữ số
def validate(password):
    if len(password) < 6: return False
    if all(not c.isalpha() for c in password):
        return False
    if all(not c.isdigit() for c in password):
        return False
    return True

class TestPasswword(unittest.TestCase):
    def test_short_pass(self):
        self.assertFalse(validate('abc12'))

    def test_no_alpha(self):
        self.assertFalse(validate('123456'))

    def test_no_digit(self):
        self.assertFalse(validate('abcdef'))
        
    def test_ok(self):
        self.assertTrue(validate('abc123'))
    
unittest.main()