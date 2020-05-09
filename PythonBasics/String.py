str = "Ashutosh Singh "
str1 = "QA.Manager"
str2 = "Ashutosh"
str3 = " spaceCheck  "

print(str[1])
print(str[0:8])  # If you want substring in python
print(str + str1)  # if want to concatenate two string
print(str2 in str)  # Substring check # Return true or false

var = str1.split(".")  # How to split string
print(var)
print(var[1])

# strip is like trim
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())