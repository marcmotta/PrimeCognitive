# test_primecognitive.py
"""
Tests for PrimeCognitive module.
"""

import unittest
from primecognitive import PrimeCognitive

class TestPrimeCognitive(unittest.TestCase):
    """Test cases for PrimeCognitive class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeCognitive()
        self.assertIsInstance(instance, PrimeCognitive)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeCognitive()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
