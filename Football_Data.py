import nflgame
import csv

def get_play_yards(play):
    yrdln = p.data['yrdln'].split()
    team = p.team
    if len(yrdln) is 1:
        return 50
    play_yards = int(yrdln[1])
    if team == yrdln[0]:
        play_yards=100-play_yards
    return play_yards

ten_total_data=[]
for i in range(1,100):
            ten_total_data.append([0,0])

for years in range(2009,2017):
    print "Starting year {}".format(years)
    touchdown_yards=[]
    all_yards=[]
 
    for wk in range(1,17+1):
        print "Gathering week {} games, this may take a second".format(wk)
        games = nflgame.games(year=years,week=wk)
        print "Done gathering week {} games".format(wk)
        plays = nflgame.combine_plays(games)

        for p in plays:
            if p.data['yrdln'] != '' and p.data['yrdln'] != None and p.data['note'] != 'XP' and p.data['note'] != 'XPM':
                yards = get_play_yards(p)
                all_yards.append(yards)
                if p.touchdown is True:
                    touchdown_yards.append(yards)

    total_data=[]
    for i in range(1,100):
            total_data.append([0,0])
    for i in all_yards:
        total_data[i-1][0]+=1
        ten_total_data[i-1][0]+=1

    for i in touchdown_yards:
        total_data[i-1][1]+=1
        ten_total_data[i-1][1]+=1

    for i in range(len(total_data)):
        print "{} yards: All Plays: {} Touchdowns: {}".format(i+1, total_data[i][0],total_data[i][1])

    file = "{}.csv".format(years)
    with open(file, 'wb') as f:
            writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Yard Line", "Number of Plays", "Touchdowns"])
            yard = 1
            for i in total_data:
                writer.writerow([yard, i[0], i[1]])
                yard+=1
 
               
with open("2009_2016.csv", 'wb') as f:
            writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Yard Line", "Number of Plays", "Touchdowns"])
            yard = 1
            for i in ten_total_data:
                writer.writerow([yard, i[0], i[1]])
                yard+=1