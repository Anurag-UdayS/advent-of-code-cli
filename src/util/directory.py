""" 
package util;

-> directory.py
-> Anurag Tewary
-> 12 December, 2022

	* Contains functions for initializing directories.
	* Creation of Year (Event) / Date (Day) directories.
"""

#DEFINE Path str
Path = str

class DirManager():
	"""DirManager will be a parent utility, and will help in managing all Directory movement."""
	def __init__(self: DirManager, path: Path):
		self.path = path

	@staticmethod
	def createYearDirectory(year: int, parent: Path = '.') -> DirManager:
		pass

	def createDayDirectory(self: DirManager, parent: Path = self.path, ):
		pass


#################################################
#                    TESTING                    #
#################################################

if __name__ == '__main__':
	pass