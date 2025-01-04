#Import
import unittest
import os

#Functions to be tested
def checkInputFile():
    curr_dir = os.getcwd()
    if os.curr_dir.exists("testcenterdata.xlsx"):
        return True
    else:
        return False

#Testing section

class TestFunction(unittest.TestCase):
    
    def test_filename(self):
        result = checkInputFile()
        self.assertEqual(result,True)

#Mandatory to be run
if __name__ == '__main__':
    unittest.main()