STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

length_name = 0

for names in STATE_NAMES.keys():
    if len(names) > length_name:
        length_name = len(names)

state = str(input("Enter short state: ")).upper()
while state != "":
    if state in STATE_NAMES:
        print("{} is {}".format(state, STATE_NAMES[state]))
    else:
        print("Invalid short state")
    state = input("Enter short state: ")
for abbreviation, name in STATE_NAMES.items():
    print("{:{}} is {}".format(abbreviation, length_name, name))
