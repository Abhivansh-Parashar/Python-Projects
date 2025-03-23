import pandas as pd
import random
list1=[]
a=list1
list2=[]
b=list2
list3=[]
c=list3
for i in range(5):
    a.append(random.randrange(300,500))
    b.append(round(random.uniform(10,50),2))
    c.append(chr(random.randrange(65,65+26)))


df=pd.DataFrame({"Marks_500":a,"Decimal":b})
df.index=c
#print(df)
print(df.loc["X","Marks_500"])