import pandas as pd # 1. Import pandas

def task1_load_explore():
    filename = 'labor.csv'

    # 2. load csv
    data = pd.read_csv(filename)

    #3. print first 5 rows
    #print('---First five rows---\n', data.head())

    # 4. Display columns, dimensions and data types
    #print('\n---Data dimensions, column names and data types---\n')
    #data.info()

    # 5. Select column as a series
    wage_increase_first_year = pd.Series(data['wage-increase-first-year']) 
    #print('\n---Wage increase first year column as a series---\n', wage_increase_first_year)

    # 6. Return the dataframe
    return data

def task2_access_data(df):
    # 1. Select column as series
    wage_increase_first_year = pd.Series(df['wage-increase-first-year'])

    # 2. Retrive first value with .iloc and .loc
    print(df.iloc[0, 1])
    print(df.loc[0, 'wage-increase-first-year'])

    # 3. Display first 5 rows with .iloc
    print(df.iloc[0:5, :])

    # 4. Select wage increase columns
    print(df.loc[:, 'wage-increase-first-year'])
    print(df.loc[:, 'wage-increase-second-year'])

    # 5. Retrieve specific value with .loc
    print(df.loc[5, 'wage-increase-second-year'])

    # 6. Select multiple rows and columns with .iloc and .loc
    print(df.iloc[5:10, 1:4])

    print(df.loc[5:9, 'working-hours':'standby-pay'])

def task3_filter_data(df):
    # 1. Select all disputes with a good outcome
    good_outcomes = df[df['class'] == 'good']
    print(good_outcomes)

    # 2. Select all disputes with a bad outcome
    bad_outcomes = df[df['class'] == 'bad']
    print(bad_outcomes)

    #3. Select disputes where wage-increase-first-year > 2.5
    large_wage_increase = df[df['wage-increase-first-year'] > 2.5]
    print(large_wage_increase)

    # 4. Select disputes where statutory-holidays > 10
    stat_holidays = df[df['statutory-holidays'] > 10]
    print(stat_holidays)

    # 5. Select disputes meeting multiple conditions
    print(df[(df['wage-increase-first-year'] > 2.5) & (df['statutory-holidays'] > 10)])

    # 6. Calculate average of wage-increase-first-year
    print(df['wage-increase-first-year'].mean().round(2))

    # 7. Calculate maximum wage-increase-first-year
    print(df['wage-increase-first-year'].max())


def main():
 
    data = task1_load_explore()

    task2_access_data(data)

    task3_filter_data(data)

main()






    