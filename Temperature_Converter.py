def celsius_to_fahrenheit(celsius):
    return(celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9 / 5) - 459.67

#User input
current_scale = input("Enter the current temperature scale (C, F, K) > ").upper()
target_scale = input("Enter the target temperature scale (C, F, K) > ").upper()
temperature = float(input("Enter the temperature to convert > "))

#Perform conversion
if current_scale == target_scale:
    print(f"The temperature is the same in both scales: {temperature}{current_scale}")
elif current_scale == "C" and target_scale == "F":
    print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(temperature)} F")
elif current_scale == "F" and target_scale == "C":
    print(f"Temperature in Celsius: {fahrenheit_to_celsius(temperature)} C")
elif current_scale == "C" and target_scale == "K":
    print(f"Temperature in Kelvin: {celsius_to_kelvin(temperature)} K")
elif current_scale == "K" and target_scale == "C":
    print(f"Temperature in Celsius: {kelvin_to_celsius(temperature)} C")
elif current_scale == "F" and target_scale == "K":
    print(f"Temperature in Kelvin: {fahrenheit_to_kelvin(temperature)} K")
elif current_scale == "K" and target_scale == "F":
    print(f"Temperature in Kelvin: {kelvin_to_fahrenheit(temperature)} F")
else:
    print("Invalid input. Please ensure you choose C, F, or K for both scales.")