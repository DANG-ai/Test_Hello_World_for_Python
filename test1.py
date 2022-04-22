
import datetime
import pandas as pd
from pandas import DataFrame as df
from matplotlib import pyplot, style

def input_values ():
    answer1 = int(input("Press 1 to enter Income\nPress 2 to enter Expense\n "))
    if answer1 == 1:
        date = str(input('Enter Date (YYYY,MM,DD) (you can skip this step if the date is today) \n'))
        try:
            year, month, day = map(int, date.split(','))
            print(day)
            date = datetime.date(year, month, day)
        except :
            date = datetime.date.today()
        while True:
            income = int(input("Enter your income for today if any \n"))
            description = str(input("Enter Description (Optional) \n"))
            tracker(date,income,0,description)
            period = str(input("Enter 1 to go back\nEnter 2 to Quit \nEnter any key to keep going \n"))
            if period == "1":
                input_values()
            elif period == "2":
                exit()
            else :
                pass
    elif answer1 == 2:
        date = str(input('Enter Date (YYYY,MM,DD) (you can skip this step if the date is today) \n'))
        try:
            year,month,day=map(int,date.split(','))
            print(day)
            date = datetime.date(year,month,day)
        except :
            date = datetime.date.today()
        while True:
            expense = int(input("Enter your expense for today if any: \n"))
            description = str(input("Enter Description (Optional): \n"))
            tracker(date,0,expense,description)
            period = str(input("Enter 1 to go back \nEnter 2 to Quit \nEnter any key to keep going \n"))
            if period == "1":
                input_values()
            elif period == "2":
                exit()
            else :
                pass
    else :
        print("Please enter a valid input.")
        input_values()

def tracker(date = datetime.date.today() ,income = 0, expense = 0,description=" "):
    data = {
    'Date':date,
    'Description':description,
    'Income':income,
    'Expenses':expense
    }
    database = df.from_dict(data, orient='index')
    database = database.transpose()
    decide = 'a'
    check = False
    date = str(date)
    year, month, day = map(int, date.split('-'))
    curr_month = month_tracker(month)
    if checkIf(curr_month):
        decide = 'w'
        check = True
    database.to_csv(f'{curr_month}.csv', mode = decide, header=check, index = False)
    Balance_get(date, curr_month)


def month_tracker(month):
    monthlist = {
        1 : 'January',
        2 : 'February',
        3 :'March',
        4 :'April',
        5 :'May',
        6 :'June',
        7 :'July',
        8 :'August',
        9 :'September',
        10 :'October',
        11 :'November',
        12 :'December',
    }
    return monthlist.get(month,1)

def checkIf(month):
    try :
        df = pd.read_csv(f'{month}.csv')
        return df.empty
    except :
        return True


def Balance_get(date=datetime.date.today(), curr_month='January'):
    Bal = []
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    get = pd.read_csv(f'{curr_month}.csv', index_col='Date')
    get.dropna(inplace=True)
    Balance = (get['Income'].sum() - get['Expenses'].sum())
    for month in months[0:months.index(curr_month) + 1]:
        try:
            got = pd.read_csv(f'{month}.csv', index_col='Date')
            got.dropna(inplace=True)
            Bal.append(got['Income'].sum() - got['Expenses'].sum())
        except FileNotFoundError:
            pass
    bal = sum(Bal)
    print(bal)
    print(
        f'Total Balance as on {datetime.date.today()} : {bal}\nBalance for {curr_month} : {Balance}\nIncome for {curr_month}: {get["Income"].sum()}\nExpense for {curr_month} : {get["Expenses"].sum()}')

def total_balance_get():
    Bal = []
    date=datetime.date.today()
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    year,month,date = map(int,str(date).split('-'))
    curr_month = month_tracker(month)
    print(curr_month,month)
    get = pd.read_csv(f'{curr_month}.csv', index_col='Date')
    get.dropna(inplace=True)
    Balance = (get['Income'].sum() - get['Expenses'].sum())
    for month in months[0:months.index(curr_month)+1]:
        try:
            got = pd.read_csv(f'{month}.csv',index_col='Date')
            got.dropna(inplace=True)
            inc = got['Income'].sum()
            exp = got['Expenses'].sum()
            lab = inc - exp
            Bal.append(lab)
            print(f'      {month.upper()}                   ')
            print(f'Balance for {month} : {lab}\nIncome for {month} : {inc}\nExpense for {month} : {exp}')
        except FileNotFoundError:
            pass
    bal = sum(Bal)
    print(f'Total Balance as on {datetime.date.today()} : {bal}\n')


def chart():
    names = list(map(lambda x: month_tracker(x), range(1, 13)))
    month = []
    income = []
    expense = []
    for names in names:
        try:
            get = pd.read_csv(f'{names}.csv', index_col='Date')
            income.append(get['Income'].sum())
            expense.append(get['Expenses'].sum())
            month.append(names)
        except FileNotFoundError:
            pass

    detail = df({
        'Income': income,
        'Expense': expense}, index=month)
    style.use('fivethirtyeight')
    columns = ['Income', 'Expenses']
    detail.plot.bar(rot=0)
    a = str(datetime.date.today())
    year, month, day = map(int, a.split('-'))
    pyplot.title(f"Report For {year}")
    pyplot.show()


while True:
    message = int(input(
        "Enter 1 to add details\nEnter 2 to see a graphical representation of your statements\nEnter 3 to get monthwise Income-Expense details\nEnter any other key to exit the program : --> "))
    if message == 1:
        input_values()
    elif message == 2:
        try:
            chart()
        except:
            print("No Data to Plot. Make sure that you have entered Income-Expense Details.")
    elif message == 3:
        try:

            total_balance_get()
        except:
            print('No Data to Show. Make sure that you have entered Income-Expense Details')
    else:
        break