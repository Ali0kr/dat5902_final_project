#Import
import unittest
import os

#Functions to be tested
#Checks if the correct file exists within the repository
def checkInputFile():
    current_dir = os.getcwd()
    if os.path.exists(current_dir+'/testcenterdata.xlsx'):
        return True
    else:
        return False

#Checks if the file is the correct size - ensures data is the same
def checkFileSize():
    current_dir = os.getcwd()
    file_dir = current_dir+'/testcenterdata.xlsx'
    if os.stat(file_dir).st_size == 3958123:
        return True
    else:
        return False

#Testing section

class TestFunction(unittest.TestCase):
    
    def test_filename(self):
        result = checkInputFile()
        self.assertEqual(result,True)
        
    def test_filesize(self):
        result = checkFileSize()
        self.assertEqual(result,True)

#Mandatory to be run
if __name__ == '__main__':
    unittest.main()