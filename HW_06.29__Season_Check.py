# Rakib ul Hasan    (roll- 23)
# github- rakibninja33


def check_season():
    while True:

        xw = input("Enter Month in numeric form: ")
        if xw == "done":
            break

        try:
            mw = int(xw)
            if mw in [3, 4, 5, 6]:
                print("The season is ", "Summer")
            elif mw in [7, 8, 9, 10]:
                print("The season is ", "Monsoon")
            elif mw in [1, 2, 11, 12]:
                print("The season is ", "Winter")
            else:
                print("Invalid Input")

        except:
            print("Invalid Input")



check_season()