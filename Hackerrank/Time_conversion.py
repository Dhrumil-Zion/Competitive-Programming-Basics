def timeConversion(s):
    date = s.split(":")
    if date[2][2:] == "AM":
        if date[0] == "12":
            return ("00:{}:{}".format(date[1],date[2][:2]))
        else:
            return ("{}:{}:{}".format(date[0],date[1],date[2][:2]))
    if date[2][2:] == "PM":
        if date[0] == "12":
            return ("{}:{}:{}".format(date[0],date[1],date[2][:2]))
        else:
            return ("{}:{}:{}".format((12 + int(date[0])),date[1],date[2][:2]))   