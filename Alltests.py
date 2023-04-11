import unittest
from main import EmailExtractorTestCase

class AllTests(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        self.addTests(unittest.makeSuite(EmailExtractorTestCase))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    all_tests = AllTests()
    runner.run(all_tests)