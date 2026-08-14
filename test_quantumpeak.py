# test_quantumpeak.py
"""
Tests for QuantumPeak module.
"""

import unittest
from quantumpeak import QuantumPeak

class TestQuantumPeak(unittest.TestCase):
    """Test cases for QuantumPeak class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumPeak()
        self.assertIsInstance(instance, QuantumPeak)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumPeak()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
