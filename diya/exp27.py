string = input("Enter a string:")

if string.endswith('ing'):
    string = string + 'ly'
    print("Modified string:",string)
else:
    string = string + 'ing'
    print("Modified string:",string)