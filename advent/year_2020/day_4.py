from advent.runner import register
import re

@register(4, 2020, 1, True)
def passport_1(split_text):
    fields = [
        ("byr", r"byr:([\d\w#]+)"),
        ("iyr", r"iyr:([\d\w#]+)"),
        ("eyr", r"eyr:([\d\w#]+)"),
        ("hgt", r"hgt:([\d\w#]+)"),
        ("hcl", r"hcl:([\d\w#]+)"),
        ("ecl", r"ecl:([\d\w#]+)"),
        ("pid", r"pid:([\d\w#]+)"),
        ("cid", r"cid:([\d\w#]+)")
    ]

    passports = [{"cid": ""}]

    for line in split_text:
        if len(line) != 0:
            for field in fields:
                match = re.search(field[1], line)
                if match is not None:
                    passports[-1][field[0]] = match.group(1)
        else:
            passports.append({"cid": ""})

    valid_count = 0
    for passport in passports:
        if len(passport) == 8:
            valid_count += 1

    return valid_count

@register(4, 2020, 2, True)
def passport_2(split_text):
    fields = [
        ("byr", r"byr:(\d{4})", 1920, 2002),
        ("iyr", r"iyr:(\d{4})", 2010, 2020),
        ("eyr", r"eyr:(\d{4})", 2020, 2030),
        ("hgt", r"hgt:(\d+)cm", 150, 193),
        ("hgt", r"hgt:(\d+)in", 59, 76),
        ("hcl", r"hcl:(#[0-9a-f]{6})"),
        ("ecl", r"ecl:(amb|blu|brn|gry|grn|hzl|oth)"),
        ("pid", r"pid:(\d{9})(\D|$)"),
    ]

    passports = [{}]

    for line in split_text:
        if len(line) != 0:
            for field in fields:
                match = re.search(field[1], line)
                if match is not None:
                    if field[0] in passports[-1]:
                        del passports[-1][field[0]]
                    elif len(field) == 4:
                        value = int(match.group(1))
                        if value >= field[2] and value <= field[3]:
                            passports[-1][field[0]] = value
                    else:
                        passports[-1][field[0]] = match.group(1)
        else:
            passports.append({})

    valid_count = 0
    for passport in passports:
        if len(passport) == 7:
            valid_count += 1

    return valid_count
