import pandas as pd
import pytest
from functools import reduce
import datetime
from geopy.distance import geodesic 

##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

def count_simba(input_str_list): 
    return sum(list(map(lambda string: string.lower().count('simba'), input_str_list)))

def test_count_simba():
    assert count_simba(["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]) == 3

# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

def append_date_data(date_dict, date):
    date_dict['year'].append(date.year)
    date_dict['day'].append(date.day)
    date_dict['month'].append(date.month)
    date_dict['date'].append(date)

def get_day_month_year(list_of_dates): 
    date_dict = {'year':[],'day':[],'month':[],'date':[]}
    return pd.DataFrame(map(lambda date: append_date_data(date_dict, date), list_of_dates))
        

def test_get_day_month_year(): 
    assert get_day_month_year([datetime.date.today(), datetime.date.today(), datetime.date.today(), datetime.date.today(), datetime.date.today()]).shape[0] == 5

# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

def compute_distance(list_of_coords):
    return list(map(lambda x: geodesic(x[0], x[1]).km, list_of_coords))

def test_compute_distance():
    assert len(compute_distance([((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))])) == 2

#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#

def sum_general_int_list(list_of_lists):
    sum = 0
    for each in list_of_lists: 
        if type(each) == list: 
            sum += sum_general_int_list(each)
        else: 
            sum += each
    return sum

def test_sum_general_int_list():
    assert sum_general_int_list([[2], 3, [[1,2],5]]) == 13



