def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string( test_string ):
    return len(test_string)

def join_string( string_1, string_2 ):
    return string_1 + string_2

def add_string_as_number(num1, num2 ):
    return int(num1) + int(num2)

months = { 1 : "January",
2 : "February",
3 : "March",
4 : "April",
5 : "May",
6 : "June",
7 : "July",
8 : "August",
9 : "September",
10 : "October",
11 : "November",
12: "December"
}

def number_to_full_month_name( month ):
    return months[month]

def number_to_short_month_name( month ):
    return months[month][:3]

def cube_result(number):
    return number ** 3

def food_1(food2):
    return food2[::-1]

def fahrenheit_to_celsius(temp):
    return (temp - 32) * (5/9)