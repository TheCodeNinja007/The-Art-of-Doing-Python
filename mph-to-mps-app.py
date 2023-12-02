# Miles Per Hour to Meters Per Second Conversion App

# Welcome message
print("Welcome to the Miles Per Hour to Meters Per Second Conversion App!")
mph = int(input("Enter the value you want to convert: "))

# mps = mph / 2.237
mps = mph * 0.4474
mps = round(mps, 2)
print(f"Your speed in meter per second is: {mps}")
