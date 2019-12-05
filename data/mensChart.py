import csv 
import matplotlib.pyplot as plt

# pie chart for men's curling medal colours (gold, silver, bronze)
# arrays for each color

golds = []
silvers = []

categories = []

with open('mensChart.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			# parse that first row of text data out of the file
			categories.append(row)
			line_count += 1 
		else:
			if row[7] == "Gold":
				print("Won gold!")
				golds.append(row[7])

			if row[7] == "Silver":
				print("Won silver!")
				silvers.append(row[7])

			line_count += 1

print("gold medals: ", len(golds))
print("silver medals: ", len(silvers))

# plot a pie chart!
labels = ("Gold", "Silver")
# sizes are how many and how large the slices of the pie chart will be
sizes = [len(golds), len(silvers)]
colors = ['gold', 'silver']
explode = (0.12, 0.12)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medals Earned By Men In Curling")
plt.xlabel("Medals since 1998")
plt.show()