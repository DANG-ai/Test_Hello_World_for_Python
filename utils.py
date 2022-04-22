from matplotlib import pyplot as plt
import pandas as pd


class IERS:
    def __init__(self, df, prt=False):
        # init IERS
        self.__star_sen = '\n-----Welcome to Income and Expenditure Recording System------\n'
        if prt:
            print(self.__star_sen)
        self.data = df
        self.test_flag = 1
        self.sum_ei = 0

    def __get_sum(self, df):
        # calculate the sum of all data
        self.sum_ei = df['Amount'].sum()
        return 1

    def cal_sum(self, ret, prt=False):
        # record sum
        self.__get_sum(self.data)
        df = pd.DataFrame(columns=['ALL Income'])
        df.loc[0] = self.sum_ei
        df.to_csv('all income.csv', index=0)
        if prt:
            print('------------------------Sum of Income and Expenditure--------------------')
            print(df.head())
            print('--------------------------------End--------------------------------------')
        return ret

    def update(self, con_list):
        # add new row
        num = self.data.shape[0]
        self.data.loc[num] = con_list
        return 1

    def plot(self, figsize, show=False, save=False):
        # plot the bar
        try:
            vc = self.data['Category'].value_counts()
            names = list(vc.index)
            if show or save:
                plt.figure(figsize=figsize)
                color = ['red','black','peru','orchid','deepskyblue']
                plt.bar(list(range(len(names))), list(vc), color=color)
                plt.xticks(list(range(len(names))), names)
                plt.xlabel('Category Name')
                plt.ylabel('Count')
                plt.title('Category Counts Bar Figure')
                plt.legend()
                if save:
                    plt.savefig('Category.png')
                if show:
                    plt.show()
        except:
            return 0
        return 1

    def save_data(self, ret, prt=False):
        # save csv and print data
        self.cal_sum(1, prt)
        self.data.to_csv('Income and Expenditure Recording.csv', index=0)
        return ret


def get_input(iclass):
    while True:
        message = int(input(
            "Enter 1 to add info to dataframe\nEnter 2 to see a graphical representation of category and save it\nEnter 3 to save all data and print the sum of Income and Expenditure Recording\nEnter any other key to exit the program : --> "))

        # for different input
        if message == 1:
            new = []
            answer1 = int(input("Press 1 to enter Income | Press 2 to enter Expenditure\n "))
            new.append(str(input('Enter Date YYYY.MM.DD\n')))
            if answer1 == 1:
                new.append('income')
                new.append(float(input("Enter your income\n")))
            else:
                new.append('expenditure')
                new.append(-float(input("Enter your expenditure\n")))
            new.append(str(input('Enter Category\n')))
            iclass.update(new)
        elif message == 2:
            try:
                iclass.plot((30, 20), save=True, show=True)
            except:
                print("No Data to Plot. Make sure that you have entered Income-Expense Details.")
        elif message == 3:
            try:
                iclass.save_data(1, prt=True)
            except:
                print('No Data to Save. Make sure that you have entered Income-Expense Details')
        else:
            break


def test():
    df = pd.DataFrame(columns=['Date', 'Expenditure and income', 'Amount', 'Category'])
    df.loc[0] = ['2022.1.5', 'income', 150, 'Normal']
    test_object = IERS(df)

    # test get sum
    assert test_object.cal_sum(1) == 1

    # test update
    assert test_object.update(['2022.1.6', 'expenditure', 100, 'Payment']) == 1

    # test plot
    assert test_object.plot((10, 10)) == 1

    # test save data
    assert test_object.save_data(1) == 1

    return True

