#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):

	if __name__ == '__main__':
	    fptr = open(os.environ['OUTPUT_PATH'], 'w')

	    ar_count = int(input())

	    ar = list(map(int, input().rstrip().split()))

	    result = aVeryBigSum(ar)

	    fptr.write(str(result) + '\n')

	    fptr.close()

	print(result)

aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])