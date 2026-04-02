
def c_to_f(temp):
    return (temp * 9/5) + 32

celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
fahrenheit_temps = list(map(c_to_f, celsius_temps))
print(fahrenheit_temps)

fahrenheit_temps = list(map(lambda temp: (temp * 9/5) + 32  , celsius_temps))
print(fahrenheit_temps)
