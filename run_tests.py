"""Test runner for RPS World."""

import unittest
import sys
import os

# Set environment variable for headless pygame
os.environ['SDL_VIDEODRIVER'] = 'dummy'

# Discover and run tests
loader = unittest.TestLoader()
start_dir = 'tests'
suite = loader.discover(start_dir, pattern='test_*.py')

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Exit with appropriate code
sys.exit(0 if result.wasSuccessful() else 1)

