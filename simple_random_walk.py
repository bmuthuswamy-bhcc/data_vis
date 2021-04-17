import matplotlib.pyplot as plt

from random_walk import RandomWalk


def main():
	rw = RandomWalk()
	rw.fill_walk()

	plt.style.use('classic')
	fig, ax = plt.subplots()

	ax.scatter(rw.x_values, rw.y_values, s = 15)

	plt.show()


if __name__ == '__main__':
	main()