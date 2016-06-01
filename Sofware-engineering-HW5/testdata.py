import Sofware_engineering_HW5
#data=day,time,num_aduit,num_child
#測資為不同時段的資料，全部大人、全部小孩、大人比較還多且10位、小孩比大人多且10位以上
#金額為四捨五入
data1=[[1,1,3,0],[1,1,0,3],[1,1,7,3],[1,1,3,8]]
data2=[[1,2,3,0],[1,2,0,3],[1,2,7,3],[1,2,3,8]]
data3=[[2,2,3,0],[2,2,0,3],[2,2,7,3],[2,2,3,8]]

print ("here is data1 result:"+str(data1))
for i in data1:
    money=Sofware_engineering_HW5.calc_money(i[0],i[1],i[2],i[3])
    print(round(money))
print ("here is data2 result:"+str(data2))
for i in data2:
    money=Sofware_engineering_HW5.calc_money(i[0],i[1],i[2],i[3])
    print(round(money))
print ("here is data3 result:"+str(data3))
for i in data3:
    money=Sofware_engineering_HW5.calc_money(i[0],i[1],i[2],i[3])
    print(round(money))