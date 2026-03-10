set1={1,3,5,7,9,} #creating set
set1.add(11)        #adding element       
print (set1)        #printing set with added element
set2={2,4,6,8,10}        # creating another set
union= set1.union(set2)        # operation:- union
intersection=set1.intersection(set2)        #operation:- intersection
difference=set1.difference(set2)        #operation:- Operation:- DIfference
print(f"The union is {union} ,the intersection is {intersection} and the difference is {difference}.")
