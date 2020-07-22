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
    city = input("Please provide if you would like to review chicago, washington or new york city:")
    while city not in CITY_DATA:
        print('Invalid City')
        city = input("Please provide if you would like to review chicago, washington or new york city:")



    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('Please provide the month: ')
    while month not in month_list:
        print('invalid month')
        month = input('Please provide the month: ')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input('Please provide the day: ')
    while day not in day_list:
        print('invalid day')
        month = input('Please provide the day: ')
        break

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    df['month']=df['Start Time'].dt.month
    most_common_month_index = df['month'].mode()[0] - 1
    most_common_month = months[most_common_month_index]
    print('The most common month', most_common_month)


    # TO DO: display the most common day of week
    df['day_of_the_week']= df['Start Time'].dt.weekday_name
    common_day_of_the_week = df['day_of_the_week'].mode()[0]
    print('The most common day of the week', common_day_of_the_week)


    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour', common_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is ', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used End station is ', end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['station combination'] = df['Start Station'] + '-' + df['End Station']
    frequent_combination = df['station combination'].mode().values[0]
    print('The most frequent combination of start station and end station trip', frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total time travelled is', total_travel_time)




    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The count of the different user types are ', user_types)


    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('The count of the different genders are ', gender_count)
    except:
        print("Washington does not have any data pertaining to gender.")



    # TO DO: Display earliest, most recent, and most common year of birth

    # Display the earliest Birth year
    try:
        Year_of_Birth_earliest = int(df['Birth Year'].min())
        print('The earliest year of birth is ', Year_of_Birth_earliest)
    except:
        print("Earliest Birth Year: Washington does not have any data pertaining to Birth Year.")


    # Display the most recent Birth year
    try:
        Year_of_Birth_recent = int(df['Birth Year'].max())
        print('The most recent year of birth is ', Year_of_Birth_recent)
    except:
        print("Most recent Year: Washington does not have any data pertaining to Birth Year.")


    # Display the most common Birth Year
    try:
        Year_of_Birth_common = int(df['Birth Year'].mode().values[0])
        print('The most common year of birth is ', Year_of_Birth_common)
    except:
        print("Most Common Birth year: Washington does not have any data pertaining to Birth Year.")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

  # TO DO: Display 5 lines of raw data as the user requests
def raw_data(df):
    """Displays raw data on bikeshare users."""

    print('\nProviding raw data...\n')
    start_time = time.time()
    raw_data = input("Would you like to view raw data? If so, please enter yes or no: ")
    counter = 0
    if raw_data == "yes":

        print(df[counter:5])
        while raw_data == 'yes':
           raw_data = input('Was the data sufficient for your review? would you like to see more? If so, enter yes or no: ')
           if raw_data == 'yes':
                counter += 5
                print(df[counter:counter+5])
           else:
               break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
