#!/usr/bin/env python3
import sys
from pathlib import Path
import unittest
import itertools, re
import colorama

sys.path.insert(0, str(Path(__file__).parent.parent))

from collections import OrderedDict

dict = OrderedDict

import ProbSetAbs
from ProbSetAbs import getAllBackends


class Tests(unittest.TestCase):
	def testInsertAndCheck(self):
		count = 100
		errorRate = 0.001
		for B in getAllBackends():
			with self.subTest(backend=B):
				b = B(count, errorRate)

				with self.subTest(check="insertion"):
					self.assertFalse(b.check(b"a" * 100))
					b.add(b"a" * 100)
					self.assertTrue(b.check(b"a" * 100))

				with self.subTest(check="non-inserted"):
					self.assertFalse(b.check(b"b" * 100))

	def testInsertAndSerialize(self):
		count = 100
		errorRate = 0.001
		for B in getAllBackends():
			with self.subTest(backend=B):
				b = B(count, errorRate)
				b.add(b"a" * 100)
				bb = bytes(b)
	
				b = B(count, errorRate)
				b.load(bb)
				self.assertTrue(b.check(b"a" * 100))

if __name__ == "__main__":
	unittest.main()
