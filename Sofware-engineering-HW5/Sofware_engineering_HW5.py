import sys,re
while True:
    while True:    
        day=input(u"Enter Weekday(1) or Holidays (2) : ")
        if re.match('[1-2]{1}',day) is None:
            print("Input Error")
            break
        time=input(u"Enter the noon(1) or night (2) :")
        if re.match('[1-2]{1}',time) is None:
            print("Input Error")
            break
        num_aduit=input(u"Enter the numner of aduit(1-999) :")
        if re.match('[1-9]{3}',num_aduit) is None:
            print("Input Error")
            break
        num_child=input(u"Enter the numner of child(1-999) :")
        if re.match('[1-9]{3}',num_child) is None:
            print("Input Error")
            break
