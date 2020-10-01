# Human Readable Duration Format
#
# 4 kyu


def format_duration(s):
    if s < 0:
        return "now"

    counter = 0
    temp = s
    b = 1

    while temp > 1:
        if counter <= 1:
            temp = temp / 60
            counter += 1
        elif counter == 2:
            temp /= 24
            counter += 1

        elif counter == 3:
            temp /= 365
            counter += 1

    while b != 0:
        if counter == 1 and b == 1:
            secs = s
        if counter == 2:
            if s % 60 == 0:
                mins = s / 60
                mins = int(mins)

            else:
                mins = int(s / 60)
                secs = int((s % 60))
                b = 0
        if counter == 3:
            if s % 3600 == 0:
                hrs = s / 3600
                mins = int(mins)

            else:
                hrs = int(s / 3600)
                print(s % 3600)
                mins = int((s % 3600))
                counter = 2

    return "{},{},{}".format(hrs, mins,secs)


print(format_duration(3800))
