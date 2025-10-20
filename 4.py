def celsius_a_fahrenheit_DAAC(celsius_DAAC):
    return (celsius_DAAC * 9/5) + 32

def fahrenheit_a_celsius_DAAC(fahrenheit_DAAC):
    return (fahrenheit_DAAC - 32) * 5/9

def celsius_a_kelvin_DAAC(celsius_DAAC):
    return celsius_DAAC + 273.15

def kelvin_a_celsius_DAAC(kelvin_DAAC):
    return kelvin_DAAC - 273.15

temp_c_DAAC = 25
print(f"{temp_c_DAAC}°C = {celsius_a_fahrenheit_DAAC(temp_c_DAAC)}°F")
print(f"{temp_c_DAAC}°C = {celsius_a_kelvin_DAAC(temp_c_DAAC)}K")
temp_f_DAAC = 77
print(f"{temp_f_DAAC}°F = {fahrenheit_a_celsius_DAAC(temp_f_DAAC)}°C")
temp_k_DAAC = 300
print(f"{temp_k_DAAC}K = {kelvin_a_celsius_DAAC(temp_k_DAAC)}°C")