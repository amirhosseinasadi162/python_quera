def calculate_floor(string):
    try:
        if len(string) != 4 or set(string) - set(['U', 'D']):
            raise ValueError("please enter U & D and string length 4")
        h = 0
        for i in string:
            if i == "U":
                h += 1
            elif i == "D":
                h -= 1
        return h
    except ValueError as error:
        print(error)
   
print(calculate_floor("DDDD"))
print(calculate_floor("UUDD"))