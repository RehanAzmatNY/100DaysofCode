import random as _random


class random:
	"""Useful random-value helpers for the exercise."""

	@staticmethod
	def randint(start, end):
		"""Return a random integer between start and end, inclusive."""
		return _random.randint(start, end)

	@staticmethod
	def choice(values):
		"""Return one randomly selected item from values."""
		return _random.choice(values)


random_integer = random.randint(1, 10)
print(random_integer)
