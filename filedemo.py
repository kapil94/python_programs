import csv

with open('Productivitychart.csv','r') as file:
	reader=csv.reader(file,delimiter='\t')
	for row in reader:
		print(row)
