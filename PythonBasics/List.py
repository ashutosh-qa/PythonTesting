#List is the data type that allow multiple values and have different data types, it is the same as the array in C/C++

values=[1, 2, "Ashutosh", 4, 5]

print(values[0])  #priniting values at 0th List
print(values[2])  #priniting values at 2nd List
print(values[-1])  #priting values at last list
print(values[1:4])  #priting range between 1-4th list

#Insert values in list
values.insert(3, "Singh")
print(values)

#Append values in list
values.append("last value")
print(values)

#Update Value in list
values[2]="ASHUTOSH"
print(values)

#Delete value in list
del values[0]
print(values)

# TUPLE - same as LIST data type, but immutable, That means data in a tuple is write protected.
val=(1, 2, "Ashutosh", 4, 5)
print(val)
print(val[1])

