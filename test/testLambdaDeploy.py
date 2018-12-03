#!/usr/bin/env python3

import unittest
import time
from deploy.deployLambda import getS3BucketFromParamsList

class TestLambdaGetParamsFile(unittest.TestCase):
    def testSingleParamParse(self):
        self.assertTrue(getS3BucketFromParamsList(['S3Bucket=mybucket'])== 'mybucket')

    def testMultiParamParse(self):
        self.assertTrue(getS3BucketFromParamsList(['S3Bucket=mybucket', 'StackName=fakestack']) == 'mybucket')

if __name__ == '__main__':
    unittest.main()