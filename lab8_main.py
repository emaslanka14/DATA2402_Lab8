import pandas as pd # 1. Import pandas

def task1_load_explore():
    filename = 'labor.csv'

    # 2. load csv
    data = pd.read_csv(filename)

    #3. print first 5 rows
    print('====================== First five rows ======================\n', data.head())
    print('\n')

    # 4. Display columns, dimensions and data types
    print('====================== Data dimensions, column names and data types ======================\n')
    data.info()
    print('\n')

    # 5. Select column as a series
    wage_increase_first_year = pd.Series(data['wage-increase-first-year']) 
    print('\n====================== Wage increase first year column as a series ======================\n', wage_increase_first_year)

    # 6. Return the dataframe
    return data

def task2_access_data(df):
    # 1. Select column as series
    wage_increase_first_year = pd.Series(df['wage-increase-first-year'])

    # 2. Retrive first value with .iloc and .loc
    print('====================== First value with .iloc and .loc ======================\n')
    print(df.iloc[0, 1])
    print(df.loc[0, 'wage-increase-first-year'])
    print('\n')

    # 3. Display first 5 rows with .iloc
    print('====================== First 5 rows with .iloc ======================\n')
    print(df.iloc[0:5, :])
    print('\n')

    # 4. Select wage increase columns
    print('====================== Wage increase columns ======================\n')
    print(df.loc[:, 'wage-increase-first-year'])
    print(df.loc[:, 'wage-increase-second-year'])
    print('\n')

    # 5. Retrieve specific value with .loc
    print('====================== Specific value with .loc ======================\n')
    print(df.loc[5, 'wage-increase-second-year'])
    print('\n')

    # 6. Select multiple rows and columns with .iloc and .loc
    print('====================== Multiple rows and columns with .iloc and .loc ======================\n')
    print(df.iloc[5:10, 1:4])
    print('\n')
    print(df.loc[5:9, 'working-hours':'standby-pay'])

def task3_filter_data(df):
    # 1. Select all disputes with a good outcome
    print('====================== Select all disputes with a good outcome ======================\n')
    good_outcomes = df[df['class'] == 'good']
    print(good_outcomes)
    print('\n')

    # 2. Select all disputes with a bad outcome
    print('====================== Select all disputes with a bad outcome ======================\n')
    bad_outcomes = df[df['class'] == 'bad']
    print(bad_outcomes)
    print('\n')

    #3. Select disputes where wage-increase-first-year > 2.5
    large_wage_increase = df[df['wage-increase-first-year'] > 2.5]
    print('====================== Disputes with large wage increase ======================\n')
    print(large_wage_increase)
    print('\n')

    # 4. Select disputes where statutory-holidays > 10
    stat_holidays = df[df['statutory-holidays'] > 10]
    print('====================== Disputes with many statutory holidays ======================\n')
    print(stat_holidays)
    print('\n')

    # 5. Select disputes meeting multiple conditions
    print('====================== Disputes meeting multiple conditions ======================\n')
    print(df[(df['wage-increase-first-year'] > 2.5) & (df['statutory-holidays'] > 10)])
    print('\n')

    # 6. Calculate average of wage-increase-first-year
    print('====================== Average wage increase ======================\n')
    print(df['wage-increase-first-year'].mean().round(2))
    print('\n')

    # 7. Calculate maximum wage-increase-first-year
    print('====================== Maximum wage increase ======================\n')
    print(df['wage-increase-first-year'].max())
    print('\n')

def main():
 
    data = task1_load_explore()

    task2_access_data(data)

    task3_filter_data(data)


if __name__ == "__main__":
    main()






    