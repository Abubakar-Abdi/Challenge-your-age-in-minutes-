from seasons import  minutes_inlife

def main():
   test1()
   test2()

def test1():
    assert minutes_inlife(2022,5,24)=="Five hundred twenty-five thousand, six hundred"
    assert minutes_inlife(2022,5,24)=="One million, fifty-one thousand, two hundred"

def test2():
    assert minutes_inlife(1,23,2022)==" nvalid date"




if __name__ == "__main__":
    main()