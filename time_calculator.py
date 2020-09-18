def add_time(start, duration, day='None'):
    start_h = int(start.split(':')[0])
    start_m = int(start.split(':')[1].split()[0])
    meridiem = start.split(':')[1].split()[1]

    addedh = int(duration.split(':')[0])
    addedm = int(duration.split(':')[1].split()[0])

    newminute = start_m + addedm

    if newminute > 59:
        newminute = newminute - 60
        addedh = addedh + 1

    ndays = 0
    while addedh >= 24:
        ndays = ndays + 1
        addedh = addedh - 24

    if addedh == 12:
        newh = start_h
        if meridiem == "PM":
            print("Heeeeello")
            ndays = ndays + 1
            meridiem = "AM"
        else:
            meridiem = "PM"
    if addedh > 12:
        addedh = addedh - 12
        newh = start_h + addedh
        if newh < 12:
            if meridiem == "PM":
                ndays = ndays + 1
                meridiem = "AM"
            else:
                meridiem = "PM"

        if newh == 12:
            ndays = ndays + 1

        if newh > 12:
            newh = newh - 12
            if meridiem == "PM":
                ndays = ndays + 1
                meridiem = "AM"
            else:
                meridiem = "PM"

    if addedh < 12:
        if start_h == 12:
            start_h = 0
            newh = start_h + addedh
        else:
            newh = start_h + addedh
        if newh == 12:
            if meridiem == "PM":
                ndays = ndays + 1
                meridiem = "AM"
            else:
                meridiem = "PM"

        if newh > 12:
            newh = newh - 12
            if meridiem == "PM":
                ndays = ndays + 1
                meridiem = "AM"
            else:
                meridiem = "PM"

    daysoftheweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday",
                     "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    stringh = str(newh)

    if newminute < 10:
        stringm = "0" + str(newminute)
    else:
        stringm = str(newminute)

    auxndays = ndays
    if day != "None":
        y = day.lower().capitalize()
        indexa = daysoftheweek.index(y)

        if ndays == 0:
            new_time = stringh + ":" + stringm + " " + meridiem + ", " + daysoftheweek[indexa]
        elif ndays <= 7:
            newindex = indexa + ndays
            if ndays == 1:
                new_time = stringh + ":" + stringm + " " + meridiem + ", " + daysoftheweek[newindex] + " (next day)"
            else:
                new_time = stringh + ":" + stringm + " " + meridiem + ", " + daysoftheweek[newindex] + " (" + str(
                    auxndays) + " days later)"
        elif ndays > 7:
            while ndays > 7:
                ndays = ndays - 7
            newindex = indexa + ndays
            new_time = stringh + ":" + stringm + " " + meridiem + ", " + daysoftheweek[newindex] + " (" + str(
                auxndays) + " days later)"
    else:
        if ndays == 0:
            new_time = stringh + ":" + stringm + " " + meridiem
        elif ndays <= 7:
            if ndays == 1:
                new_time = stringh + ":" + stringm + " " + meridiem + " (next day)"
            else:
                new_time = stringh + ":" + stringm + " " + meridiem + " (" + str(auxndays) + " days later)"
        elif ndays > 7:
            while ndays > 7:
                ndays = ndays - 7
            new_time = stringh + ":" + stringm + " " + meridiem + " (" + str(auxndays) + " days later)"

    return new_time