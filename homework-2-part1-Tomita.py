#Mio Tomita
#June 8, 2022
#Homework2, Part1

#import libraries
from statistics import median, mean

###PART ONE: Lists
#1: list of numbers 
numbers = [22, 90, 0, -10, 3, 22, 48]

#2: the number of elements in the list
print(len(numbers))

#3: the 4th element of the list
print(numbers[3])

#4: sum of the 2nd and 4th element of the list
print(numbers[1] + numbers[3])

#5: the 2nd-largest value in the list
print(sorted(numbers,reverse=True)[1])

#6: the last element of the original unsorted list
print(numbers[-1])

#7: the sum of all of the numbers divided by two
print(sum(numbers)/2)

#8: Print whether the median or the mean of the numbers is higher
if median(numbers) > mean(numbers):
    print('The median of the numbers is higher than the mean.')
elif median(numbers) < mean(numbers):
    print('The mean of the numbers is higher than the median.')
else:
    print('The median and the mean of the numbers are the same.')


###PART ONE: Dictionaries
#1) create a dictionary
#source:https://www.imdb.com/title/tt0116282/

movie = {
    'title':'Fargo',
    'year':1996,
    'director':'Joel & Ethan Coen'
}

#2) add ['budget']['revenue']
movie['budget'] = 7000000
movie['revenue'] = 51203925
ratio = movie['revenue'] / movie['budget']

print(f"The revenue of the movie was {ratio:.1f} times its budget.")

#3) evaluation of investment
if ratio < 0:
    print("That was a bad investment.")
elif ratio >5:
    print("That was a great investment.")
else:
    print("That was an okay investment.")
    
#4) dictionary for the population of the boroughs of NYC
nyc_population = {
    'Manhattan': 1.6,
    'Brooklyn': 2.6,
    'Bronx': 1.4,
    'Queens': 2.3,
    'Staten Island': 470000/1000000 
}

#5) Display the population of Brooklyn
print(f"The population of Brooklyn is {nyc_population['Brooklyn']} million.")

#6) Display the combined population of all five boroughs
nyc_total = sum(nyc_population.values())
print(f"The combined population of all five boroughs is {nyc_total} million.")

#7) Display what percent of NYC's population lives in Manhattan
pct_manhattan = nyc_population['Manhattan'] / nyc_total * 100
print(f"{pct_manhattan:.1f}% of NYC's population lives in Manhattan")