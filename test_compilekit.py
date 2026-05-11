# test_compilekit.py
"""
Tests for CompileKit module.
"""

import unittest
from compilekit import CompileKit

class TestCompileKit(unittest.TestCase):
    """Test cases for CompileKit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CompileKit()
        self.assertIsInstance(instance, CompileKit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CompileKit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
