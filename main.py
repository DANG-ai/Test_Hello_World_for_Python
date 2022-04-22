from utils import IERS, get_input, test
import pandas as pd


if __name__ == '__main__':
    # test
    test()

    # main
    df = pd.DataFrame(columns=['Date', 'Expenditure and income', 'Amount', 'Category'])
    iclass = IERS(df, prt=True)
    get_input(iclass)




