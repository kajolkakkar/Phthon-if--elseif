total=0
average=0.0
counter=0

print "Enter the grade and (press -1 to quit)"
grade=int(raw_input("Enter the specific garde you got"))
while grade !=-1:
	total=total+grade
	counter=counter+1
	print "Enter the grade and (press -1 to quit)"
	grade=int(raw_input("Enter the specific garde you got"))
	
	
average=total/counter
print "The total average is",average

if average<20:
    print "F"
elif 20<average<40:
    print "D"
elif  40<average<60:
    print "C"

elif 60<average<80:
    print "B"

elif average>80:
    print "A"
