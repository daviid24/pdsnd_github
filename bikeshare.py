import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = ''
    city_name = ['chicago','new york city','washington']
    
    while city not in city_name:
        city = str(input('Would you like to see data for Chicago, New York City, or Washington?\n')).lower()
        if city not in city:
            print ('invalid option, please try again')
            
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = ''
    month_name = ['all','january','february','march','april','may','june']
    while month not in month_name:
        month = str(input('Filter the data by month: All, January, February, March, April, May or June\n')).lower()
        if month not in month_name:
            print ('invalid option, please try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    day_name = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    while day not in day_name:
        day = str(input('Filter the data by day: All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n')).lower()
        if day not in day_name:
            print ('invalid option, please try again')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    month_name = {1:'January',
                  2:'February',
                  3:'March',
                  4:'April',
                  5:'May',
                  6:'June'}
    
    most_common_month = df['month'].value_counts().head(1).index[0]
    print('Most common month:', month_name[most_common_month])    

    # TO DO: display the most common day of week

    most_common_day_of_week = df['day_of_week'].value_counts().head(1).index[0]
    print('Most common day of week:', most_common_day_of_week)    

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().head(1).index[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    most_common_start_station = df['Start Station'].value_counts().head(1).index[0]
    print('Most commonly used start station:', most_common_start_station) 


    # TO DO: display most commonly used end station

    most_common_end_station = df['End Station'].value_counts().head(1).index[0]
    print('Most commonly used end station:', most_common_end_station) 

    # TO DO: display most frequent combination of start station and end station trip
    
    df['most_common_combination'] = df['Start Station'] + ' - ' + df['End Station']
    most_common_combination = df['most_common_combination'].value_counts().head(1).index[0]
    print('Most frequent combination of start station and end station trip:', most_common_combination) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('Total travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = pd.DataFrame(df['User Type'].value_counts())
    print(user_types)

    # TO DO: Display counts of gender

    try:
        gender = pd.DataFrame(df['Gender'].value_counts())
        print(gender)
    except:
        print('gender not avaliable')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        print('Earliest year of birth:', df['Birth Year'].min())
        print('Most recent year of birth:', df['Birth Year'].max())

        most_common_year_of_birth = df['Birth Year'].value_counts().head(1).index[0]
        print('Most common year of birth:', most_common_year_of_birth)
    except:
        print('bith year not avaliable')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def show_individual_data(df):

    see_data = str(input('\nWould you like to see the first 5 rows? Enter yes or no.\n')).lower()
    if see_data == 'yes':
        row = 0
        while True:
            for i in range(row,row + 5):
                print(df.iloc[i,:])
            row = row + 5
            restart = str(input('\nWould you like to see the next 5 rows? Enter yes or no.\n')).lower()
            if restart.lower() != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_individual_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


# Run main function
if __name__ == "__main__":
	main()
