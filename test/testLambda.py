#!/usr/bin/env python3

import unittest
import time
from awslambda.lambda_function import lambda_handler

class TestLambda(unittest.TestCase):
     def testCorrectTime(self):
        self.assertEqual(lambda_handler('',''), {'timestamp': int(round(time.time())), 'message': 'Automation for the people'})
if __name__ == '__main__':
    unittest.main()