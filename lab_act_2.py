x = 300

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

diff1 = abs(num1 - x)
diff2 = abs(num2 - x)
diff3 = abs(num3 - x)

closest = num1

if diff2 < abs(closest - x):
    closest = num2

if diff3 < abs(closest - x):
    closest = num3

print("Closest number to", x, "is", closest)