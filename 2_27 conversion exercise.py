
floatNum = 23.2345346746

intNum = int(floatNum)

print(type(intNum))
print(intNum)

print(int("678  "))
print(type(int("678  ")))
print( )

intNum = 56
float1 = float(intNum)
print(type(float1))
print(float1)
print( )

str1 = "24.3443434"
float2 = float(str1)
print(type(float2))
print(float2)
print( )

print("exercise: change , to .")

str_value = "24,3443434"
# Replace comma with dot
str_value = str_value.replace(",", ".")
print(" changed , to .",str_value)
# Convert to float
float_value = float(str_value)
print(type(float_value))  # Output: <class 'float'>
print(float_value)        # Output: 24.3443434

print( "Wartość float1: " + str(float1) )

