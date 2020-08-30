

from openpyxl import load_workbook as lw
from tqdm import tqdm
from time import sleep
from prettytable import PrettyTable

table = PrettyTable()
table.align = 'l'

workbook = lw(filename= 'data.xlsx')

sheet = workbook.active
sheet.title = 'haha'


print()
pbar = tqdm(total=100)
pbar.set_description("Working... ")
is_field = True


record = []
sums = []

for value in sheet.iter_rows(min_row=1,max_row=30,min_col=2,max_col=8,values_only=True):
    pass
    # record.append(value)
    if(is_field):
        table.field_names = value
        is_field = False
    elif (value[0] is None):
        pass
    else:
        record = value[1:7]
        sums.append(sum(record))
        table.add_row(value)

    sleep(0.1)
    pbar.update(100/30)
pbar.close()

table.add_column("Total", sums)

# print (sums)

# print(*record,sep='\n')
print()
print(table)


workbook.save(filename='data.xlsx')




