from datetime import date
import sys
import inflect

s=inflect.engine()

def main():
  try:
      year,month,day=input("input birth_day").split("-")
  except ValueError :
     sys.exit("invalid date")
  minutes_inlife(year,month,day)
def  minutes_inlife(year,month,day):
   try:
      dt=date(int(year),int(month),int(day))
      td=date.today()
      difference=td-dt
      minute=int(difference.total_seconds()/60)
      min=s.number_to_words(minute, andword="")
      print(min.capitalize())


   except ValueError:
      return"Value error"






if __name__ == "__main__":
    main()