import calendar
import sys


def main():
    for r in sys.argv[1:]:
        input_date=r.split("-")
        our_day=(calendar.weekday(int(input_date[0]),int(input_date[1]),int(input_date[2])))
        print((calendar.day_name[our_day]))
        
if __name__ == "__main__":
    main()
