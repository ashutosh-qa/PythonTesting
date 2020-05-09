# Lets say
ItemsInCart = 0

# Now add two items in cart

if ItemsInCart != 2:
    #raise Exception("Products cart not matching with count")
    pass

# assert(ItemsInCart == 2)

# raise and assert are two ways to validate conditions


# Try # Except - This is use where sometimes popup coming but its not certain,
# so even if popup will not come, script will not fail and it will continue

try:
    with open('noname.txt', 'r') as reader:
        reader.read()

# except:
#   print("Seems something failed in try block")

except Exception as e:
    print(e)


try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Cleaning up records or cookies")

# finally always use with try, except
# Somehow if script fail after creating records, so can put record delete code in finally block in last
# so it will cleanup data cretaed data through failed scripts