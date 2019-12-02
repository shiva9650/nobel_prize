import json

with open('C:/Users/Shiva Shantha Mani/Downloads/prize.json') as f:
   data = json.loads(f.read())

###### 1st #######
print("Enter first name")
fname = input()

print("Enter surname")
sname = input()

l = len(data['prizes'])
for x in range(l):
   d1 = data['prizes'][x]['laureates']
   for y in range(len(d1)):
    d2 = d1[y]['firstname']
    d3 = d1[y]['surname']
    if d2 == fname and d3 == sname:
	    print(d1[y])

###### 2nd ######
print("Enter year")
year = int(input())

for x in range(l):
	d4 = int(data['prizes'][x]['year'])
	d5 = data['prizes'][x]['laureates']
	if year == d4:
	  for y in range(len(d5)):
	    print(d5[y]['firstname'],d5[y]['surname'])
	
###### 3rd #######	
print("Enter category")
category = input()  
print("Enter year")
year1 = int(input())

for x in range(l):
	d6 = int(data['prizes'][x]['year'])
	d7 = data['prizes'][x]['category']
	d5 = data['prizes'][x]['laureates']
	if year1 == d6 and d7 == category:
	  for y in range(len(d5)):
	    print(d6,d7,d5[y]['firstname'],d5[y]['surname'])

###### 4th ######		
print("Enter category")
category = input()  
print("Enter year")
year2 = int(input())
list =[]

for x in range(l):
	d8 = int(data['prizes'][x]['year'])
	d9 = data['prizes'][x]['category']
	d5 = data['prizes'][x]['laureates']
	#print(d6)
	if year2 == d8 and d9 == category:
	  for y in range(len(d5)):
	    name = d5[y]['firstname']+' '+d5[y]['surname']
	    list.append(name)
		
list.sort()
for x in range(len(list)):
    print(list[x])
	
