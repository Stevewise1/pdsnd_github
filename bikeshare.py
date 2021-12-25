#Import libraries
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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

    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= ''
    while city != 'all':

        city = input('What City Would you like to explore? Enter Chicago, New York or Washington: ')
        city=city.lower()
        if city == 'chicago':
            print('\n You have selected Chicago City.\n')
            break
        elif city == 'new york':
            print('\n You have selected New York City.\n')
            break
        elif city == 'washington':
            print('\n You have selected Washington City.\n')
            break
        else:
            print("\n I don't understand that choice, please try again.\n")
    else:
            print('\n Thanks for exploring the US Bikeshare Data. Have a nice day.\n')

    # Get user input for month (all, january, february, ... , june)
    print("Let's choose a month to explore...")
    filter_data=input("Would you like to filter by month, day, both or not at all? Enter 'none' for not at all.: ")
    filter_data=filter_data.lower()
    month = ''
    day = ''
    if filter_data == 'month':
        while month != 'all':
            month = input("\n What month's data would you love to explore?: Enter January, February, March, April, May or June: ")
            month = month.lower()
            if month == 'january':
                print("\n Great! You have selected January.\n")
                break
            elif month == 'february':
                print("\n Great! You have selected February.\n")
                break
            elif month == 'march':
                print("\n Great! You have selected March.\n")
                break
            elif month == 'april':
                print("\n Great! You have selected April.\n")
                break
            elif month == 'may':
                print("\n Great! You have selected May.\n")
                break
            elif month == 'june':
                print("\n Great! You have selected June.\n")
                break

            else:
                print("\n I am a little confused with that choice, can you try again")

    elif filter_data == 'day':
        month = 'all'
        while day != 'all':
            day = input("\n What day of the week would you want to explore?: Enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ")
            day=day.lower()
            if day == 'monday':
                print("\n Great. You have chosen to explore Monday's data.\n")
                break
            elif day == 'tuesday':
                print("\n Great. You have chosen to explore Tuesday's data.\n")
                break
            elif day == 'wednesday':
                print("\n Great. You have chosen to explore Wednesday's data.\n")
                break
            elif day == 'thursday':
                print("\n Great. You have chosen to explore Thursday's data.\n")
                break
            elif day == 'friday':
                print("\n Great. You have chosen to explore Friday's data.\n")
                break
            elif day == 'saturday':
                print("\n Great. You have chosen to explore Saturday's data.\n")
                break
            elif day == 'sunday':
                print("\n Great. You have chosen to explore Sunday's data.\n")
                break

            else:
                print("\n I'm sorry, I do not seem to understand that input, can you please try again")

    elif filter_data == 'both':
        month= ''
        day = ''
        month= input("\n What month would you like to filter the data by?  Enter January, February, March, April, May or June: ")
        month= month.lower()
        day = input("\n What day of the week would you want to filter by?: Enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ")
        day=day.lower()

        while day != 'all':
            if day == 'monday':
                print("\n Lovely. You have chosen to explore {} and Monday's data.\n".format(month))
                break
            elif day == 'tuesday':
                print("\n Great. You have chosen to explore {} Tuesday's data.\n".format(month))
                break
            elif day == 'wednesday':
                print("\n Great. You have chosen to explore Wednesday's data.\n")
                break
            elif day == 'thursday':
                print("\n Great. You have chosen to explore Thursday's data.\n")
                break
            elif day == 'friday':
                print("\n Great. You have chosen to explore Friday's data.\n")
                break
            elif day == 'saturday':
                print("\n Great. You have chosen to explore Saturday's data.\n")
            elif day == 'sunday':
                print("\n Great. You have chosen to explore Sunday's data.\n")

        else:
            print("\n I am a little confused with that choice, can you try again")
    elif filter_data == 'none':
        month = 'all'
        print("Great! No filter will hence be applied to our data.")
    else:
        ("\n I do not understand that input, please try again.")

    # Get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.dayofweek
    if month == 'january':
        df = df[df['Start Time'].dt.month == 1]
    elif month == 'february':
        df = df[df['Start Time'].dt.month == 2]
    elif month == 'march':
        df = df[df['Start Time'].dt.month == 3]
    elif month == 'april':
        df = df[df['Start Time'].dt.month == 4]
    elif month == 'may':
        df = df[df['Start Time'].dt.month == 5]
    elif month == 'june':
        df = df[df['Start Time'].dt.month == 6]
    elif month == 'all':
        df
    else:
        df
    if day == 'monday':
        df=df[df['Start Time'].dt.dayofweek == 0]
    elif day == 'tuesday':
        df=df[df['Start Time'].dt.dayofweek == 1]
    elif day == 'wednesday':
        df=df[df['Start Time'].dt.dayofweek == 2]
    elif day == 'thursday':
        df=df[df['Start Time'].dt.dayofweek == 3]
    elif day == 'friday':
        df=df[df['Start Time'].dt.dayofweek == 4]
    elif day == 'saturday':
        df=df[df['Start Time'].dt.dayofweek == 5]
    elif day == 'sunday':
        df=df[df['Start Time'].dt.dayofweek == 6]
    else:
        df


    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month= df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    #display the most common day of week
    df['day_of_week']= df['Start Time'].dt.dayofweek
    popular_weekday= df['day_of_week'].mode()[0]
    print('Most Popular Week Day:', popular_weekday)

    #display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    #display most commonly used start station
    popular_start_station= df['Start Station'].value_counts().idxmax()
    print('Most Commonly used Start Station:', popular_start_station)
    #display most commonly used end station
    popular_end_station= df['End Station'].value_counts().idxmax()
    print('Most Commonly used End Station:', popular_end_station)
    # Display most frequent combination of start station and end station trip
    start_end_combination= (df['Start Station'] +'|'+ df['End Station']).mode()[0]
    start_end_combination= str(start_end_combination.split('|'))
    print('Most Frequent Combination of Start Station and End Station Trip is:\n{}' .format(start_end_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #Display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time is:' + str(total_travel_time))
    #Display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean travel time is:' + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the given fitered data is: \n" + str(user_types))

    #Display counts of gender
    gender = df['Gender'].value_counts()
    print("The count of user gender from the given fitered data is: \n" + str(gender))

    #Display earliest, most recent, and most common year of birth
    earliest_year_of_birth=df['Birth Year'].min()
    print('Earliest Year of Birth is: {}\n'.format(earliest_year_of_birth))
    most_recent_year_of_birth=df['Birth Year'].max()
    print('The Most Recent Year of Birth is: {}\n'.format(most_recent_year_of_birth))
    most_common_year_of_birth=df['Birth Year'].mode()[0]
    print('The Most Common Year of Birth is: {}\n'.format(most_common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def show_raw_data(df):
    """Displays raw data based on user input."""
    data = 0
    while True:
        show_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if show_raw_data.lower() != 'yes':
            break
            return
        else:
            data = data + 5
            print(df.iloc[data:data+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
