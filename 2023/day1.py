import re
from aocd import get_data
def calibrate_1(text):
    text_by_line = text.split("\n")
    summed_value = 0

    for line in text_by_line:
        first_digit = ""
        last_digit = ""
        for x in line:
            if x.isnumeric():
                if first_digit == "":
                    first_digit = x
                last_digit = x
              
        summed_value += int(first_digit + last_digit)
    return summed_value
    
def calibrate_2(text):
    numbers_by_letter = {
        "^one.*": "1",
        "^two.*": "2",
        "^three.*": "3",
        "^four.*": "4",
        "^five.*": "5",
        "^six.*": "6",
        "^seven.*": "7",
        "^eight.*": "8",
        "^nine.*": "9"
    }
    text_by_line = text.split("\n")
    summed_value = 0

    for line in text_by_line:
        first_digit = ""
        last_digit = ""
        #slightly naive solution using regex
        for i in range(len(line)):
            if line[i].isnumeric():
                if first_digit == "":
                    first_digit = line[i]
                last_digit = line[i]
            else:
                for key, value in numbers_by_letter.items():
                    new_first_letter = re.sub(key, value, line[i:])[0]
                    if new_first_letter.isnumeric():
                        if first_digit == "":
                            first_digit = new_first_letter
                        last_digit = new_first_letter
                        break

        summed_value += int(first_digit + last_digit)
    return summed_value

calibration_data = get_data(day=1, year=2023)