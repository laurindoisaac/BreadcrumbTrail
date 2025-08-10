# test_breadcrumbtrail.py
"""
Tests for BreadcrumbTrail module.
"""

import unittest
from breadcrumbtrail import BreadcrumbTrail

class TestBreadcrumbTrail(unittest.TestCase):
    """Test cases for BreadcrumbTrail class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BreadcrumbTrail()
        self.assertIsInstance(instance, BreadcrumbTrail)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BreadcrumbTrail()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
