import sys,re
week_price_aduit=268
week_price_child=120
holiday_price_aduit=368
holiday_price_child=150
holiday_bonus=1.1

def input_data():
    while True:    
        day=input(u"Enter Weekday(1) or Holidays (2) : ")
        if re.match('[1-2]{1}',day) is None:
            print("Input Error")
            break
        time=input(u"Enter the noon(1) or night (2) :")
        if re.match('[1-2]{1}',time) is None:
            print("Input Error")
            break
        num_aduit=input(u"Enter the numner of aduit(0-999) :")
        if re.match('[0-9]{1,3}',num_aduit) is None:
            print("Input Error")
            break
        num_child=input(u"Enter the numner of child(0-999) :")
        if re.match('[0-9]{1,3}',num_child) is None:
            print("Input Error")
            break
        return int(day),int(time),int(num_aduit),int(num_child)

def calc_discount(num_aduit,num_child):
    people_discount=int((num_aduit+num_child)/3)
    people_count=num_aduit+num_child
    if num_child > people_discount:
        num_child-=people_discount
    else:
        people_discount-=num_child
        num_child=0
        num_aduit-=people_discount
    return num_aduit,num_child,people_count

while True:
    day,time,num_aduit,num_child=input_data()
    if day==1 and time==1:
        num_aduit,num_child,people_count=calc_discount(num_aduit,num_child)
        money=(week_price_aduit*num_aduit+num_child*week_price_child)

    if day==2 or time==2:
        num_aduit,num_child,people_count=calc_discount(num_aduit,num_child)

        money=(holiday_price_aduit*num_aduit+num_child*holiday_price_child)*holiday_bonus

    if (people_count)>=10:
        money=money*0.95
    print(round(money))