import re
import unittest

def validate_email(email):
    """
    Validates an email address based on format and valid providers.
    
    Args:
        email (str): The email address to be validated.
        
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Regular expression to validate email format
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(yahoo|gmail|outlook)\.com$'
    
    # Check for valid format and valid email providers
    if re.match(email_regex, email):
        return True
    else:
        return False

class TestEmailValidation(unittest.TestCase):

    def test_valid_emails(self):
        """Test valid email addresses."""
        self.assertTrue(validate_email('aavash.bhattarai@gmail.com'))
        self.assertTrue(validate_email('ram_bahadur@yahoo.com'))
        self.assertTrue(validate_email('bipin.karki@outlook.com'))

    def test_invalid_emails(self):
        """Test invalid email addresses."""
        self.assertFalse(validate_email('invalid.email.com'))
        self.assertFalse(validate_email('user@yopmail.com'))
        self.assertFalse(validate_email('test@gmail.com '))
        self.assertFalse(validate_email('john.doe@gmail'))

if __name__ == '__main__':
    unittest.main()
