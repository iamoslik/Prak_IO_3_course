import numpy as np
import pandas as pd

sell = pd.read_csv('MS-b1-sell.csv')
supply = pd.read_csv('MS-b1-supply.csv')
inv = pd.read_csv('MS-b1-inventory.csv')

res1 = pd.DataFrame(columns = ['date', 'apple', 'pen'])
dates = sell.date.unique()
res1.date = dates
res2 = pd.DataFrame(columns = ['date', 'apple', 'pen'])
res2.date = inv.date

i = 0
j = 0
a_sum = 0
p_sum = 0
l = len(res1)
i_max = len(supply)
j_max = len(sell)
a_sell = 0
p_sell = 0
z = 0
z_max = len(inv)

b_apple = [[0, 0], [0, 0], [0, 0]]
b_pen = [[0, 0], [0, 0], [0, 0]]
w_apple = [[0, 0], [0, 0], [0, 0]]
w_pen = [[0, 0], [0, 0], [0, 0]]

for k in range(0 , l):
    while i < i_max and supply.date[i] == res1.date[k] :
        a_sum = a_sum + supply.apple[i]
        p_sum = p_sum + supply.pen[i]
        i+=1
    while  j < j_max and sell.date[j] == res1.date[k]:
        if sell.sku_num[j][6] == 'a':
            a_sum -= 1
            a_sell += 1
        if sell.sku_num[j][6] == 'p':
            p_sum -= 1
            p_sell += 1
        j+=1

    if k == l-1 or res1.date[k][5:7] != res1.date[k+1][5:7]:
        if a_sell > b_apple[2][1]:
            if a_sell > b_apple[1][1]:
                if a_sell > b_apple[0][1]:
                    b_apple[2] = b_apple[1]
                    b_apple[1] = b_apple[0]
                    b_apple[0] = [res1.date[k][0:7], a_sell]
                else:
                    b_apple[2] = b_apple[1]
                    b_apple[1] = [res1.date[k][0:7], a_sell]
            else:
                b_apple[2] = [res1.date[k][0:7], a_sell]
        if p_sell > b_pen[2][1]:
            if p_sell > b_pen[1][1]:
                if p_sell > b_pen[0][1]:
                    b_pen[2] = b_pen[1]
                    b_pen[1] = b_pen[0]
                    b_pen[0] = [res1.date[k][0:7], p_sell]
                else:
                    b_pen[2] = b_pen[1]
                    b_pen[1] = [res1.date[k][0:7], p_sell]
            else:
                 b_pen[2] = [res1.date[k][0:7], p_sell]
        
        a_sell = 0
        p_sell = 0

        res2.apple[z] = a_sum - inv.apple[z]
        res2.pen[z] = p_sum - inv.pen[z]

        a_sum = inv.apple[z]
        p_sum = inv.pen[z]
        
        if res2.apple[z] > w_apple[2][1]:
            if res2.apple[z] > w_apple[1][1]:
                if res2.apple[z] > w_apple[0][1]:
                    w_apple[2] = w_apple[1]
                    w_apple[1] = w_apple[0]
                    w_apple[0] = [res2.date[z][0:7], res2.apple[z]]
                else:
                    w_apple[2] = w_apple[1]
                    w_apple[1] = [res2.date[z][0:7], res2.apple[z]]
            else:
                w_apple[2] = [res2.date[z][0:7], res2.apple[z]]
        if res2.pen[z] > w_pen[2][1]:
            if res2.pen[z] > w_pen[1][1]:
                if res2.pen[z] > w_pen[0][1]:
                    w_pen[2] = w_pen[1]
                    w_pen[1] = w_pen[0]
                    w_pen[0] = [res2.date[z][0:7], res2.pen[z]]
                else:
                    w_pen[2] = w_pen[1]
                    w_pen[1] = [res2.date[z][0:7], res2.pen[z]]
            else:
                w_pen[2] = [res2.date[z][0:7], res2.pen[z]]
        z+=1
    res1.apple[k] = a_sum
    res1.pen[k] = p_sum

res1.to_csv('daily1.csv', index = False)
res2.to_csv('steal1.csv', index = False)

print("Состояние склада на каждый день")
print(pd.read_csv('daily1.csv'))
print("Best in apple sellings:")
print(b_apple[0][0], ' : ', b_apple[0][1])
print(b_apple[1][0], ' : ', b_apple[1][1])
print(b_apple[2][0], ' : ', b_apple[2][1])
print("Best in pen sellings:")
print(b_pen[0][0], ' : ', b_pen[0][1])
print(b_pen[1][0], ' : ', b_pen[1][1])
print(b_pen[2][0], ' : ', b_pen[2][1])
print()
print("Месячные данные о количестве сворованного товара")
print(pd.read_csv('steal1.csv'))
print("Worst in apple steal:")
print(w_apple[0][0], ' : ', w_apple[0][1])
print(w_apple[1][0], ' : ', w_apple[1][1])
print(w_apple[2][0], ' : ', w_apple[2][1])
print("Worst in pen steal:")
print(w_pen[0][0], ' : ', w_pen[0][1])
print(w_pen[1][0], ' : ', w_pen[1][1])
print(w_pen[2][0], ' : ', w_pen[2][1])