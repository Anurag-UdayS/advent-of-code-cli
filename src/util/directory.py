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

import unittest as UnitTests

class DirManager(object):
	"""
	DirManager will be a parent utility, and will
	help in managing all Directory movement.
	"""

	instances: dict[Path, object] = {}

	def __new__(cls, year: int, path: Path = Path.cwd()):
		path = cls.getYearDirectoryPath(path, year)

		if path in cls.instances:
			return cls.instances[path]
		else:
			return super().__new__(cls)

	def __init__(self, year: int, path: Path = Path.cwd()):
		path = DirManager.getYearDirectoryPath(path, year)
		self.path = path
		self.year = year
		DirManager.instances[path] = self

	@staticmethod
	def getYearDirectoryPath(path: Path | str, year: int) -> Path:
		if (type(path) is str):
			path = Path(path)

		# Raise an error if a file is passed.
		if (path.is_file()):
			# error
			return None

		directory: str = path.parts[-1]
		root: str = path.parts[0]

		# If path has no prefix, or is relative to cwd,
		# Replace Path(.) with Path(CWD)
		# Test that 1st char is not /
		if (root[0] == '.'):
			path = Path.cwd() / path.relative_to('.')
		elif (root[0] != '/'):
			path = Path.cwd() / path

		# If the last part is an int, and it is equal to year,
		# treat it as the directory, Otherwise append.
		if (not directory.isdigit() or int(directory) != year):
			path = path.joinpath(str(year))

		return path


	def build(self):
		pass

	def createDayDirectory(self, parent: Path = None):
		pass


#################################################################################
#                                    TESTING                                    #
#################################################################################

class DirManagerTesting(UnitTests.TestCase):

	# Test 1: assert that directories created with the same path are equal.
	def testEquality(self):
		dir1: DirManager = DirManager(2023, './test/2023')
		dir2: DirManager = DirManager(2023, './test/2023')
		self.assertEqual(dir1, dir2)

	# Test 2: assert that directories created with different paths are inequal.
	def testInEquality(self):
		dir1: DirManager = DirManager(2023, './test/2023')
		dir2: DirManager = DirManager(2021, './test/2021')
		self.assertNotEqual(dir1, dir2)

	# Test 3: select path through different directives.
	def testDifferentSelectionWays(self):
		dir1: DirManager = DirManager(2023, './test')
		dir2: DirManager = DirManager(2023, './test/2023')
		dir3: DirManager = DirManager(2023, 'test')
		self.assertEqual(dir1, dir2)
		self.assertEqual(dir2, dir3)



if __name__ == '__main__':

	UnitTests.main()
	# print(Path('./abc/2023'))
