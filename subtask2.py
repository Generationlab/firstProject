count=0
summation=0
minimum=0
mean=0

entry = [4,5,18,1,-1] #value of the list
count=len(entry)
count_upd=count-1
print("The total number of elements in the list are",count_upd)#printing the number of elements the list without -1

entry.sort() #sorting the list
entry.pop(0) #updating the entry list with removing -1

summation=sum(entry) #using the sum command to sum all elements in the list
print("The sum of all values in the list is",summation) #printing the value of summation

minimum = min(entry)
print("The minimum value of all the elements in the list is",minimum)

mean = summation/count_upd
print("The mean value of the elements in the list is",mean)
#It looks like I have learned how to use git today
