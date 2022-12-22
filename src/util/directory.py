"""
package util;

-> directory.py
-> Anurag Tewary
-> 12 December, 2022

	* Contains functions for initializing directories.
	* Creation of Year (Event) / Date (Day) directories.
"""

import os
from pathlib import Path

from unittest import TestCase
import unittest as StartUnitTests


class DirManager(object):
	"""
	DirManager will be a parent utility, and will
	help in managing all Directory movement.
	"""

	instances: dict[Path, object] = {}

	def __new__(cls, year: int, path: Path = Path('.')):
		path = cls.getYearDirectoryPath(Path, year)

		if path in cls.instances:
			return cls.instances[path] 
		else:
			return super().__new__(cls)

	def __init__(self, path: Path('.')):
		self.path = path
		DirManager.instances[path] = self

	@staticmethod
	def getYearDirectoryPath(self, path: Path | str, year: int):
		pass

		# If the last part is an int, and it is equal to year,
		# treat it as the directory, Otherwise append.
		
	def createDayDirectory(self, parent: Path = None):
		pass


#################################################################################
#                                    TESTING                                    #
#################################################################################

class DirManagerTesting(TestCase):

	# Test 1: assert that directories created with the same path are equal.
	def testEquality(self):
		inst1: DirManager = DirManager('./abc/2023')
		inst2: DirManager = DirManager('./abc/2023')
		self.assertEqual(inst1, inst2)

	# Test 2: assert that directories created with different paths are inequal.
	def testInEquality(self):
		inst1: DirManager = DirManager('./abc/2023')
		inst2: DirManager = DirManager('./abc/2021')
		self.assertNotEqual(inst1, inst2)


if __name__ == '__main__':
	# StartUnitTests.main()
	print(Path('abc').is_dir())
	