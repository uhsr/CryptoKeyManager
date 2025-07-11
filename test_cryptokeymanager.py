# test_cryptokeymanager.py
"""
Tests for CryptoKeyManager module.
"""

import unittest
from cryptokeymanager import CryptoKeyManager

class TestCryptoKeyManager(unittest.TestCase):
    """Test cases for CryptoKeyManager class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoKeyManager()
        self.assertIsInstance(instance, CryptoKeyManager)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoKeyManager()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
