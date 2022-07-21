import time
import pandas as pd
import numpy as np
#---------------------------------------------------------------------------------------------------------------------
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#---------------------------------------------------------------------------------------------------------------------
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
    city = city.lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Invalid Input. Please enter the name of city again.\n')
        city = city.lower()

    # get user input for month (all, january, february, ... , june)
    month = input('Would you like to see data for which month? Type \'all\' for applying no month filter.\n')
    month = month.lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('Invalid Input. Please enter again.\n')
        month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Woukld you like to see data for which day? Type \'all\' for applying no day filter.\n')
    day = day.lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('Invalid Input. Please enter again.\n')
        day = day.lower()

    print('-'*40)
    return city, month, day
#---------------------------------------------------------------------------------------------------------------------
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
    df['day_of_week'] = df['Start Time'].dt.day_name()


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
#---------------------------------------------------------------------------------------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Start Month:', popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    popular_day = df['day'].mode()[0]
    print('Most Frequent Start Day of Week:', popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#---------------------------------------------------------------------------------------------------------------------
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination_station = (df.groupby(['Start Station', 'End Station']).size().idxmax())
    print('Most Frequent Combination of Start Station and End Station Trip:', popular_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#---------------------------------------------------------------------------------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#---------------------------------------------------------------------------------------------------------------------
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Number of Subscriber:', df['User Type'].value_counts()[0])
    print('Number of Customer:', df['User Type'].value_counts()[1])

    # TO DO: Display counts of gender
    print('Number of Male:', df['Gender'].value_counts()[0])
    print('Number of Female:', df['Gender'].value_counts()[1])

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Earliest Year of Birth', int(df['Birth Year'].min()))
    print('Most Recent Year of Birth', int(df['Birth Year'].max()))
    print('Most Common Year of Birth', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#---------------------------------------------------------------------------------------------------------------------
def display_data(df):
    """Display user data """
    pd.set_option('display.max_columns',200)

    view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no?\n')
    if view_data.lower() == 'yes':
        start_loc = 0
        while True:
             print(df.iloc[start_loc : start_loc + 5,:])
             start_loc += 5
             view_display = input("Do you wish to continue? Enter yes or no?\n")
             if view_display.lower() == 'yes':
                    print(df.iloc[start_loc : start_loc + 5,:])
             else:
                break
#---------------------------------------------------------------------------------------------------------------------
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
