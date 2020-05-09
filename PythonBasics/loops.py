# If else condition

greeting = "Good Morning"

if greeting == "Morning":
    print("Condition matach")
else:
    print("Condition do not macth")

print("if code executed successfully")
print("------------------------------")


# For Loop
obj = [1, 2, 3, 4, 5]
for i in obj:
   print(i)
   print(i*2)
print("------------------------------")

# Sum of first natural numbers 1+2+3+4+5=15
# range(i, j) -> i to j-1
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)
print("------------------------------")

#By default, increment is 1, below way to update increment by 2
for k in range(1, 10, 2):
    print(k)
print("------------------------------")

#We can also skip initial index, it will automatically initiate from 0
for m in range(5):
    print(m)

#### While loop
print("-----------WHILE LOOP-------------------")
x=5
while x > 1:
    print(x)
    x = x - 1
print("-----------WHILE LOOP code executed------")

#### If in While loop
x=5
while x > 1:
    if x != 3:
        print(x)
    x = x - 1
print("-----------IF WHILE LOOP code executed------")

#### break and continue in While loop
x=5
while x > 1:
    if x == 4:
        x = x - 1
        continue #once control will continue from here, it will not go to below code, and will start from begining
    if x == 2:
        break
    print(x)
    x = x - 1
print("-----------Break - Continue - IF WHILE LOOP code executed------")
