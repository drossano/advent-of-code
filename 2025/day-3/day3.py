def get_batteries_from_file(file_name):
    joltages = []
    with open(file_name, "r") as banks:
        for bank in banks:
            joltages.append(list(bank.strip()))
    return joltages


# iterate through each joltage list
# find max that's not the last number
def get_first_max(joltage_list):
    first_max_pos = joltage_list.index(max(joltage_list[:-1]))

    return joltage_list.pop(first_max_pos)


# remove that max and store it
# get next max, can be last number
# store and join
# add each joined number

battery_1 = get_batteries_from_file("2025/day-3/input.txt")[0]
print(battery_1)
print(get_first_max(battery_1))
print(battery_1)
