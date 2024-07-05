countrycapital={"india":"new delhi","luxebourg":"luxembourg city","malta":"valletta"}
print(type(countrycapital))
print(countrycapital)
#retrieve item
print(countrycapital["malta"])
#get keys
print(countrycapital.keys())
#get values
print(countrycapital.values())
#get items
print(countrycapital.items())
#retrive each item
for c in countrycapital:
    print(c,countrycapital[c])
#adding items
countrycapital["germany"]="bern"
print(countrycapital)
#updating and changing
countrycapital["germany"]="berlin"
print(countrycapital)
#deleting
del countrycapital["germany"]
print(countrycapital)
# presents
print("india" in countrycapital)
print("india" not in countrycapital)
print("new delhi" in countrycapital)