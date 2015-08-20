__author__ = 'solomina'

drinks = ["tea", "juice", "coffee", "water", "vodka"]
print drinks
# Sort and print the latest letters
#print map(lambda a: a[-1] + " from " + a, sorted(drinks))
# Sort by the latest symbol and print sorted list
#print [i[::-1] for i in sorted(map(lambda a: a[::-1], drinks))]

people = ["Smith John", "Smith Jim", "Taker Mary", "Taker D", "Hart Jane", "ddd"]
sort_people = []
for name in people:
    print name
    sort_people.append((name.split()[1] + " " + name.split()[0], name))
    # print sorted(sort_people)
#sort_peoples = [(name.split()[1] + " " + name.split()[0], name) for name in peoples if name.split() == 2]
print sorted(sort_people)