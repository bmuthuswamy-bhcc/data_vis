import matplotlib.pyplot as plt

def main():
	x_values = range(1,100)
	y_values = [x**2 for x in x_values]

	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	ax.plot(x_values, y_values, linewidth = 3)
	ax.set_title("Square Numbers", fontsize = 24)
	ax.set_xlabel("Value", fontsize=14)
	ax.set_ylabel("Square of Value", fontsize=14)

	# set size of tick labels
	ax.tick_params(axis='both', labelsize=14)

	#plt.show()
	plt.savefig('squares_plot.png', bbox_inches='tight')

if __name__ == "__main__":
	main()