# from datetime import datetime, timedelta
#
# current_date = datetime.now()
# date_list = [current_date + timedelta(days=i) for i in range(5)]
#
# print(date_list)
from datetime import datetime
date1 = datetime(2022, 3, 1)
date2 = datetime(2022, 3, 15)

if date1 < date2:
    print('Дата 1 передує даті 2.')
elif date1 > date2:
    print('Дата 1 слідує даті 2')
else:
    print('Дати рівні')




