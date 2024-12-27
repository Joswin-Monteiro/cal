import argparse

zellers_week_to_week = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    0: 6,
}

month = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def zellers_congruence(q:int, m:int, year: int) -> int:
    # m is the month (3 = March, 4 = April, 5 = May, ..., 14 = February)
    if m < 3:
        m += 12
        year -= 1
        
    # K the year of the century ( year mod 100 {\displaystyle year{\bmod {1}}00}).
    k = year % 100
    #J is the zero-based century (actually ⌊ y e a r / 100 ⌋ {\displaystyle \lfloor year/100\rfloor }) For example, the zero-based centuries for 1995 and 2000 are 19 and 20 respectively (not to be confused with the common ordinal century enumeration which indicates 20th for both cases).
    j = year // 100

    # return h which is the day in zellers_congruence
    # h: 0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday
    # q is day of month
    # h = (day + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) - 2 * J) % 7
    return int((q + (13 * (m+1))//5+ k + (k//4) + (j//4) - 2*j) % 7)

def display_cal(day:int, mon:int, year:int):
    week_of_date = zellers_congruence(day, mon, year)
    space = zellers_week_to_week[week_of_date]
    print(f"     {month[mon]} {year}    ")
    print("Su  Mo  Tu  We  Th  Fr  Sa")

    if year % 4 == 0 and mon == 2:
        max_date = 29
    elif mon == 2:
        max_date = 28
    elif mon in [1, 3, 5, 7, 8, 10, 12]:
        max_date = 31
    else:
        max_date = 30
    
    date = 1
    counter = 1
    for i in range(1 ,36):
        if space > 0:
            print("    ", end="")
            space -= 1
            continue
        if date == max_date:
            print(f"{date:02}")
            break
        if i % 7 == 0:
            print(f"{date:02}")
        else:
            print(f"{date:02} ", end=" ")
        date += 1

def main():
    parser = argparse.ArgumentParser(description="Calendar cli program using python")
    parser.add_argument("month", type=int, help="The month(1-12)")
    parser.add_argument("year", type=int, help="The year(e.g, 2024)")
    
    args = parser.parse_args()
    display_cal(1, args.month, args.year)

if __name__ == "__main__":
    main()
