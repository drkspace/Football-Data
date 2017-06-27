import nflgame
import nflgame.update_sched
import csv

#Get the position of the ball start (1-99)
def get_play_yards(p):
    yrdln = p.data['yrdln'].split()
    
    team = p.team
    if len(yrdln) is 1:
        return 50
    play_yards = int(yrdln[1])
    if team == yrdln[0]:
        play_yards=100-play_yards
    return play_yards

#Calculate the plays at and the touchdown at each yard
def total_touchdowns(first_year=2009, final_year=2016):

    ten_total_data=[]
    for i in range(1,100):
                ten_total_data.append([0,0])

    for years in range(first_year, final_year+1):
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

def total_touchdown_types(first_year=2009, final_year=2016):
   
    ten_total_data=[[0,0,0,0,0] for i in range(100)]
    #for i in range(1,100):
    #            ten_total_data.append([0,0])

    for years in range(first_year, final_year+1):
        print "Starting year {}".format(years)
        
        rushing_touchdown_yards = []
        passing_touchdown_yards = []
        rushing_yards = []
        passing_yards = []
        all_yards = []
 
        for wk in range(1,17+1):
            print "Gathering week {} games, this may take a second".format(wk)
            print type(years)
            print type(wk)
            games = nflgame.games(year=years,week=wk)
            print "Done gathering week {} games".format(wk)
            plays = nflgame.combine_plays(games)

            for p in plays:
                if p.data['yrdln'] != '' and p.data['yrdln'] != None and p.data['note'] != 'XP' and p.data['note'] != 'XPM':
                    yards = get_play_yards(p)
                    all_yards.append(yards)
                    if 'pass' in p.desc.lower() or 'sacked' in p.desc.lower():
                        passing_yards.append(yards)
                        if p.touchdown is True:
                            passing_touchdown_yards.append(yards)

                    #/r/programminghorror
                    elif 'up the middle' in p.desc.lower() or 'left end' in p.desc.lower() or 'right end' in p.desc.lower() or 'right guard' in p.desc.lower() or 'right tackle' in p.desc.lower() or 'left guard' in p.desc.lower() or 'left tackle' in p.desc.lower():
                        rushing_yards.append(yards)
                        if p.touchdown is True:
                            rushing_touchdown_yards.append(yards)
                    else:
                        pass
                    

        total_data=[[0,0,0,0,0] for i in range(99)]
        #for i in range(1,100):
        #        total_data.append([0,0])
        for i in all_yards:
            total_data[i-1][0]+=1
            ten_total_data[i-1][0]+=1

        for i in passing_yards:
            total_data[i-1][1]+=1
            ten_total_data[i-1][1]+=1

        for i in passing_touchdown_yards:
            total_data[i-1][2]+=1
            ten_total_data[i-1][2]+=1

        for i in rushing_yards:
            total_data[i-1][3]+=1
            ten_total_data[i-1][3]+=1

        for i in rushing_touchdown_yards:
            total_data[i-1][4]+=1
            ten_total_data[i-1][4]+=1


       # for i in range(len(total_data)):
        #    print "{} yards: All Plays: {} Touchdowns: {}".format(i+1, total_data[i][0],total_data[i][1])

        file = "{}.csv".format(years)
        with open(file, 'wb') as f:
            writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Yard Line", "Number of Plays", "Passing Plays", "Passing Touchdowns", "Rushing Plays", "Rushing Touchdowns"])
            yard = 1
            for i in total_data:
                writer.writerow([yard, i[0], i[1], i[2], i[3], i[4]])
                yard+=1
 
               
    with open("2009_2016.csv", 'wb') as f:
            writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Yard Line", "Number of Plays", "Passing Plays", "Passing Touchdowns", "Rushing Plays", "Rushing Touchdowns"])
            yard = 1
            for i in ten_total_data:
                writer.writerow([yard, i[0], i[1], i[2], i[3], i[4]])
                yard+=1


