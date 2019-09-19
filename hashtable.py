from collections import defaultdict, Counter

#Instead of throwing an error for non-existent values, defaultdict takes a list and creates the values for us.
#It has to be imported via collections 
hash1 = defaultdict(list)

hash1['Angelo'] = "Calhoun"
hash1["Cuchulainn"] = "FFXIII"
print hash1['Angelo']

#prints entire dictionary
print Counter(hash1)

#prints ever letter in the key, the string is an iterable.
for key in hash1.keys():
	print Counter(key)

#Lists elements in arbitrary order, if element is less than 0, it'll ignore it. 
a = Counter(hash1["Cuchulainn"])
print list(a.elements())

'''
hash2 = {
	"Marco":"Polo",
	"Michael": "Jordan",
	"Tokyo": "Ghoul"
}

def add_to_Hash(key, value):
	if value not in hash2:
		hash2[value] = key
		print hash2
	return 

add_to_Hash("carlo", "carrera")
'''
