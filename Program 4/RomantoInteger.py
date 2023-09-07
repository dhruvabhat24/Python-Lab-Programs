def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for i in range(len(s) - 1, -1, -1):
        current_value = roman_dict[s[i]]
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
            prev_value = current_value
    return result

roman_numeral = input("Enter the roman numerical value: ")
integer_value = roman_to_int(roman_numeral)
print("The integer value of {} is: {}".format(roman_numeral, integer_value))