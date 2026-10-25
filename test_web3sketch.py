# test_web3sketch.py
"""
Tests for Web3Sketch module.
"""

import unittest
from web3sketch import Web3Sketch

class TestWeb3Sketch(unittest.TestCase):
    """Test cases for Web3Sketch class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Sketch()
        self.assertIsInstance(instance, Web3Sketch)

    def test_run_method(self):
        """Test the run method."""
        instance = Web3Sketch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
