import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_excel('Base4.xlsx', header = 0)

all = pd.DataFrame(columns = ['unsullen', 'produced', 'defects', 'percentage', 'supplier']) #по всем поставикам
harpy = pd.DataFrame(columns = ['unsullen', 'produced', 'defects', 'percentage'])
westeros = pd.DataFrame(columns = ['unsullen', 'produced', 'defects', 'percentage'])
print('Base')
print(base)

unsullen = base['unsullen.id'].unique()
all.unsullen = unsullen
j = 0
print(len(all))
f = 0
for i in range (0, len(all)):
    produced = 0
    defects = 0
    if f == 0 and base.supplier[j] == 'westeros.inc':
        f = 1
    all.supplier[i] = base.supplier[j]
    while j < len(base) and base['unsullen.id'][j] == all.unsullen[i]:
        produced = produced + base.produced[j]
        defects = defects + base.defects[j]
        j += 1
    all.produced[i] = produced
    all.defects[i] = defects
    percentage = int(100 * defects/ produced) # в целых процентах доля сломанного
    all.percentage[i] = percentage
    new_row = {'unsullen': all.unsullen[i] , 'produced': produced , 'defects': defects, 'percentage' : percentage}
    if f == 0:
        harpy = harpy.append(new_row, ignore_index = True)
    else:
        westeros = westeros.append(new_row, ignore_index = True)
sum = pd.DataFrame(columns = ['supplier', 'produced', 'defects', 'percentage'])
produced = 0
defects = 0
for i in range (0, len(harpy)):
    produced = produced + harpy.produced[i]
    defects = defects + harpy.defects[i]
    percentage = int(100 * defects / produced)
new_row = {'supplier' : 'harpy.co' , 'produced': produced , 'defects': defects, 'percentage' : percentage}
sum = sum.append(new_row, ignore_index = True)
produced = 0
defects = 0
for i in range (0, len(westeros)):
    produced = produced + westeros.produced[i]
    defects = defects + westeros.defects[i]
    percentage = int(100 * defects / produced)
new_row = {'supplier' : 'wesreros.inc' , 'produced': produced , 'defects': defects, 'percentage' : percentage}
sum = sum.append(new_row, ignore_index = True)
print('all')
print(all)
print('harpy.co')
print(harpy)
print('westeros.inc')
print(westeros)
print('Сводка по всему')
print(sum)

fig1 =plt.figure(1, figsize=(10,3))
ax1 = fig1.subplots(ncols = 2)
x = harpy['unsullen'].values
y1 = harpy['produced'].values
y2 = harpy['defects'].values
ax1[0].bar(x,y1)
ax1[0].bar(x,y2)
ax1[0].title.set_text('harpy.co')
x = westeros['unsullen'].values
y1 = westeros['produced'].values
y2 = westeros['defects'].values
ax1[1].bar(x,y1)
ax1[1].bar(x,y2)
ax1[1].title.set_text('westeros.inc')
plt.savefig('both.png')

fig2 =plt.figure(2, figsize=(10,3))
ax2 = fig2.subplots()
x = sum['supplier'].values
y1 = sum['produced'].values
y2 = sum['defects'].values
ax2.bar(x,y1)
ax2.bar(x,y2)
plt.savefig('sum.png')