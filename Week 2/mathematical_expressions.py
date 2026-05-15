# Fahrenheit to Celsius Converter
 
# Step 1: Ask the user to enter a temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
 
# Step 2: Apply the conversion formula
#         (Fahrenheit - 32) * 5 / 9
celsius = (fahrenheit - 32) * 5 / 9
 
# Step 3: Display the result to 1 decimal place
print("The temperature in Celsius is:", round(celsius, 1))