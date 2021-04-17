from random import choice

class RandomWalk:
	"""A class to generate random walks.
	A random walk is a path that has no clear direction
	but the path is determined by a series of random decisions,
	each decision is left entirely to chance.  Example: a confused
	ant taking every step in a random direction.
	Random walks have applications in nature, physics, biology, chemistry
	and economics.  So, random walk simulations are useful in many real world
	scenarios.
	"""

	def __init__(self, num_points = 5000):
		"""Initialize attributes of a walk."""
		self.num_points = num_points

		# All walks start at (0,0)
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""Calculate all the points in a walk."""

		# Keep taking steps until the walk reaches the desired length.
		while len(self.x_values) < self.num_points:

			# Decide which direction to go and how far to go in that direction.
			x_direction = choice([1, -1])
			x_distance = choice([1,2,3,4])
			x_step = x_direction * x_distance

			y_direction = choice([1,-1])
			y_distance = choice([1,2,3,4])
			y_step = y_direction * y_distance

			# Calculate the new position
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)

			