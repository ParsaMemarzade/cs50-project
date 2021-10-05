import csv
from sklearn import tree
import mysql.connector

cnx = mysql.connector.connect(user='', password='',
                               host='127.0.0.1',
                               database='')
cursor=cnx.cursor()


inp=[]
price=[]

with open ('price.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        inp.append(line[0:3])
        price.append(int(line[3]))

for i in range(len(price)):
    inp[i][0] = int(inp[i][0])
    inp[i][1] = int(inp[i][1])
    inp[i][2] = int(inp[i][2])

for i in range(len(inp)):
        cursor.execute('INSERT INTO laptop VALUES(%i, %i, %i, %i)'%(inp[i][0],inp[i][1],inp[i][2],price[i]))
 
tree1 = tree.DecisionTreeClassifier()
tree1 = tree1.fit(inp, price)

new_one=[]
print('Brand (hp, mac, acer, asus, del) : ',end='')
new_one.append(input())
print('Graphic : ',end='')
new_one.append(int(input()))
print('RAM : ',end='')
new_one.append(int(input()))
print('serie of CPU : ',end='')
new_one.append(int(input()))

a=[new_one[1:]]
answer = tree1.predict(a)
price_new = int(answer[0])

print('Predicted Price is : ',end='')

if new_one[0]=='hp':
    price_new = price_new + (price_new*1.3) // 10
    print(price_new)
    
elif new_one[0]=='mac':
    price_new = price_new + (price_new*2) // 10
    print(price_new)
    
elif new_one[0]=='asus':
    price_new = price_new + (price_new*1.7) // 10
    print(price_new)
    
elif new_one[0]=='dell':
    price_new = price_new + (price_new*1.5) // 10
    print(price_new)
    
elif new_one[0]=='acer':
    price_new = price_new + (price_new*1.1) // 10
    print(price_new)
    
    
