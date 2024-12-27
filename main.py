import argparse

week = {
    0: "Saturday",
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
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
    # print(f"Day: {day}, month:{m}, k:{k}, j:{j}")
    week_of_date = zellers_congruence(day, mon, year)
    print(week[week_of_date])

def main():
    parser = argparse.ArgumentParser(description="Calendar cli program using python")
    parser.add_argument("day", type=int, help="The day to highlight (1-31)")
    parser.add_argument("month", type=int, help="The month(1-12)")
    parser.add_argument("year", type=int, help="The year(e.g, 2024)")
    
    args = parser.parse_args()
    display_cal(args.day, args.month, args.year)

if __name__ == "__main__":
    main()
