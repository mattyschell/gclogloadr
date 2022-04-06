import os
import unittest
import pathlib
import filecmp

import logconverter


class GcLogLoadrTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.testdirectory = os.path.join(pathlib.Path(__file__).parent
                                         ,'test')

        self.testlog = os.path.join(self.testdirectory
                                   ,'test.log')
        self.testexp = os.path.join(self.testdirectory
                                   ,'test_expected.sql')
        self.testsql = os.path.join(self.testdirectory
                                   ,'test.sql')

    @classmethod
    def tearDownClass(self):

        try:
            pass
            os.remove(self.testsql)
        except:
            pass
    
    def test_asameasiteverwas(self):

        self.conversionmgr = logconverter.DmlConverter(self.testlog
                                                      ,self.testsql)

        self.conversionmgr.convert()

        self.assertTrue(filecmp.cmp(self.testexp
                                   ,self.testsql))
    

    
if __name__ == '__main__':
    unittest.main()