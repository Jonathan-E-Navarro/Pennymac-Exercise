import sys
filename = 'w_data (5).dat'
lines = tuple(open(filename, 'r'))
min_spread = sys.maxsize
min_day = 0 

for line in lines[6:-2]:
	row = line.split()
	day = row[0]
	max_temp = row[1] if "*" not in row[1] else row[1][:-2]
	min_temp = row[2] if "*" not in row[2] else row[2][:-2]

	difference = abs(int(max_temp)-int(min_temp))
	if difference < min_spread:
		min_spread = difference
		min_day = day

print("day with minimum temp spread: ",min_day)


