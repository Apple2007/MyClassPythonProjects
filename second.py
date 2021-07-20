# Variable Types
intvariable = -100
print(intvariable)
floatvariable = -100.10
print(floatvariable)
stringvariable = "Hello"
print(stringvariable)
booleanvariable = True
print(booleanvariable)
# Convert Variable Types to Other Types
exampleVariablenumber = 757.4
print(int(exampleVariablenumber))
print(float(exampleVariablenumber))
print(str(exampleVariablenumber))
print(bool(exampleVariablenumber))
# Conditional Statements
if exampleVariablenumber > 758:
    print("The number is positive")
else:
    print("The number is negative")
# Elif
if exampleVariablenumber == 758:
    print("The number is equal to variable")
elif exampleVariablenumber > 757:
    print("The number is neutral")
else:
    print("The number is negative")
# Comparison Operators
if exampleVariablenumber == 758:
    print("The number is equal to variable")
elif exampleVariablenumber > 757:
    print("The number is neutral")
elif exampleVariablenumber < 757:
    print("The number is negative")
else:
    print("The number is positive")
# And, Or, Not
if exampleVariablenumber == 758 and exampleVariablenumber > 757:
    print("The number is equal to variable")
elif exampleVariablenumber > 757 and exampleVariablenumber < 757:
    print("The number is neutral")
elif exampleVariablenumber < 757 and exampleVariablenumber > 757:
    print("The number is negative")
elif exampleVariablenumber == 758 or exampleVariablenumber < 757:
    print("The number is positive")
else:
    print("The number is negative")
# 