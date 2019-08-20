import unittest
from spider import *

class testmyrogram(unittest.TestCase):


    def test_status_code(self):
        self.assertEqual(r.status_code, 200 )

    def test_mobile_agent(self):
        result = headers
        self.assertTrue(result == {'User-Agent':'Mobile'} )

    def test_website_header(self):
        h.header = ('\t',x,".",h.headers[x])
        self.assertTrue(h.headers != h.header)

if __name__=='__main__':
    unittest.main()
