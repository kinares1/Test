def celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = []
    for celsius in celsius_list:
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_list.append(fahrenheit)
    return fahrenheit_list


