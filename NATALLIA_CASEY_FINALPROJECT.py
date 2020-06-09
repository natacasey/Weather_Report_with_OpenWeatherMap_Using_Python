#Purpose: Program(getting data from an open API) presents a user with a weather report for the entered zip or city as many times as asked.
#Assignment number: 12.1.
#Name: Natallia Casey
#Importing neccesary modules
import requests

from requests.exceptions import HTTPError

import json

#creating main() function with a loop that lets a user continue getting weather report or stopping it
#validating user's response
def main():
    message = 'Welcome to the weather report center!'
    print(message)
    making_a_choice()
    while True:
        try:
            user_response = str(input('Please, type "yes" if you want to see current weather information and type "no" if you do not.\n')).lower()
#printing error messages if the input is not as planned, asking the user to try again
            if user_response not in ('yes', 'no'):
                raise ValueError
        except ValueError:
            print('Sorry. Invalid input. Please, try again.')
        else:
# calling making_a_choice() function if the user wants to see another forecast
            if user_response == "yes":
                making_a_choice()
            elif user_response == "no":
                print('Have a great day!')
                break


#prompting the user with the next function to enter either zip or a city to get a current weather report
def making_a_choice():
    try:
        choice = input('If you want to enter a zip for weather search, type 1; if you want to enter a city, type 2.\n').lower()
        if choice not in ('1', '2'):
            raise ValueError
    except ValueError:
        print('Sorry. Invalid input. Please, try again.')
#letting a user get back to making a choice between a city and zip by letting a function call itslef if user's input is not valid.
        making_a_choice()
    else:
#calling sendingrequestzip() if user enters 1
        if choice == "1":
            sendingrequestzip()
#calling sendingrequestcity() if user enters 2
        elif choice == "2":
            sendingrequestcity()


#making a call to OpenWeatherMap API in the next two functions to get data
def sendingrequestzip():
    askingforzip = input('What zip do you want to know weather for?\n')
    zipandcountry = '{},US'.format(askingforzip)
    print('Zip entered: {}'.format(askingforzip))
    url = 'http://api.openweathermap.org/data/2.5/weather'
    querystring = {'zip': zipandcountry, 'APPID': '0ca1629b4ea085ca8af2a4a0b7af4e83', 'units': 'imperial'}
    headers = {'cache-control': 'no-cache'}
#checking if connection is successful, catching errors, displaying error code and description to be more specific than just a custom message
    try:
        response = requests.request('Get', url, headers=headers, params=querystring)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Sorry. Connection was not successful. Input needs to be modified. Error details: {http_err}')
    except Exception as err:
        print(f'We are sorry. An error occurred. Please, try again. {err}')
    else:
        print('Your connection was successful')
        source = response.text
#calling parsing() function to work with the data
        parsing(source)


def sendingrequestcity():
    askingforcity = input('What city do you want to know weather for?\n')
    cityandcountry = '{},US'.format(askingforcity)
    print('City entered: {}'.format(askingforcity))
    url = 'http://api.openweathermap.org/data/2.5/weather'
    querystring = {'q': cityandcountry, 'APPID': '0ca1629b4ea085ca8af2a4a0b7af4e83', 'units': 'imperial'}
    headers = {'cache-control': 'no-cache'}
#checking if connection is successful, catching errors, displaying error code and description to be more specific than just a custom message
#asking user to modify input in the http error message
    try:
        response = requests.request('Get', url, headers=headers, params=querystring)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Sorry. Connection was not successful. Input needs to be modified. Error details: {http_err}')
    except Exception as err:
        print(f'We are sorry. An error occurred. Please, try again. {err}')
    else:
        print('Your connection was successful')
        source = response.text
#calling parsing() function to work with the data
        parsing(source)


#next function: parsing json string to a Python dictionary
#printing weather report from the dictionary
def parsing(source):
    data = json.loads(source)
    print('{}'.format('------------------------------------------------'))
    print('Current weather report for {}'.format(data['name']))
    print('{}'.format('------------------------------------------------'))
    print('Current temperature: {} degrees'.format(data['main']['temp']))
    print('Pressure: {}hPa'.format(data['main']['pressure']))
    print('Humidity: {}%'.format(data['main']['humidity']))
    print('Low Temperature: {} degrees'.format(data['main']['temp_min']))
    print('High Temperature: {} degrees'.format(data['main']['temp_max']))
    print('Clouds: {}'.format(data['weather'][0]['description']))


if __name__ == "__main__":
    main()
