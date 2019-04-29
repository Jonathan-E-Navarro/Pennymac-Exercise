'''
Parses textfile, isolates important pieces of information,
then uses them to calculate and keep track of the minimum
difference in amount of goals a team has had for and against them.
''' 
import sys
filename = 'soccer.dat'
lines = tuple(open(filename, 'r'))
min_difference = sys.maxsize
end_team = ""

for line in lines:
	row = line.split()
	if len(row)==10:
		team = row[1]
		goals_for = row[6]
		goals_against = row[8]
		difference = abs(int(goals_for)-int(goals_against))
		if difference < min_difference:
			min_difference = difference
			end_team = team 

print("team with smallest difference: ",end_team)



