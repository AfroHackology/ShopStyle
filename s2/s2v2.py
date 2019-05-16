# calculating descriptive statistics
from introDataScience.s2.s2v1 import *

def number_of_records(data_sample):
    return len(data_sample)

numer_of_ties = number_of_records(data_from_csv) - 1

#print(numer_of_ties,"ties in our data sample")

def num_of_records2(data_sample):
    return data_sample.size

number_of_ties_my_csv = num_of_records2(my_csv)
print(number_of_ties_my_csv, "ties in out data sample")
