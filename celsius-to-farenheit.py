def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit


#celsius_value = 32  # Example temperature in Celsius
#celsius_value = int(input(("enter value of celsius")))

# if question is asking to input value , then use - input(int(celius_value)) , and comment line 7

fahrenheit_value = celsius_to_fahrenheit(celsius_value)

print(f"{celsius_value}°C is equal to {fahrenheit_value}°F")
