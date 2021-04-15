def romanToInt(s: str) -> int:

    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    int_value = roman_dict[s[-1]]

    for i in range(len(s)-1):
        if roman_dict[s[i]] < roman_dict[s[i+1]]:
            int_value -= roman_dict[s[i]]
        else:
            value = roman_dict[s[i]]
            int_value += value
            print(int_value)

    return int_value


print(romanToInt("XXI"))

