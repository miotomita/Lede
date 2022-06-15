#Mio Tomita
#June 7, 2022
#Homework 1

from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd
import re

##pip install wikipedia 
import wikipedia as wiki

#Input your birthdate
future = True

while future:
    bd = input('type in your date of birth yyyymmdd')
    bd = datetime.strptime(bd, '%Y%m%d')
    print (bd.date())
    if bd <= datetime.today():
        future = False
    else:
        print("You've come from future? Please try again!")


# 1: How old the user is
age = relativedelta(date.today(), bd).years

print("Your age is:",age)


# 2: How many times the user's heart has beaten
#source:
#https://my.clevelandclinic.org/health/diagnostics/17402-pulse--heart-rate
#Children (ages 6 - 15) 70 – 100 beats per minute
#Adults (age 18 and over) 60 – 100 beats per minute

#normal heartbeat rate per day
hb_child = (70+100)/2 * 60 * 24 #children under 16
hb_adult = (60+100)/2 * 60 * 24 #adults(16 and upper)

if age > 15:
    #16th birthday
    bd_16 = bd + relativedelta(years=16)
    #heartbeat
    beat1 = (bd_16 - bd).days * hb_child 
    beat2 = ((datetime.today() - bd_16).days + 1) * hb_adult
    hb_total = beat1 + beat2
else:
    hb_total = (datetime.today() - bd).days * hb_child

print("Your heart has beaten",int(hb_total), "times.")


# 3 : How many times a blue whale's heart has beaten
#source: 
#https://www.theatlantic.com/science/archive/2019/11/diving-blue-whales-heart-beats-very-very-slowly/602557/
# a 220-ton blue whale (the largest animal on record) should have a resting heart rate of 11 beats a minute

whale = (datetime.today() - bd).days * 60 * 24 * 11

print("A Blue whale's heart has beaten", int(whale), "times.")

# 4: How many times a rabbit's heart has beaten
#source:
#https://www.medivet.co.uk/pet-care/pet-advice/heart-disease-in-rabbits/#:~:text=A%20rabbit's%20resting%20heart%20rate,than%20five%20beats%20a%20second).
#A rabbit’s resting heart rate ranges between 140 and 180 beats per minute

rabbit = (datetime.today() - bd).days * 60 * 24 * ((140+180)/2)

print("A rabbit's heart has beaten", int(rabbit), "times.")

# 5: If the answer to rabbit heartbeats is more than a million, say "XXX million" instead of the very long raw number
rabbit = str(int(rabbit/1000000))+' million' if rabbit >= 1000000 else str(rabbit)

print("A rabbit's heart has beaten", rabbit, "times.")

# 6: How old they are in Venus years
#source: https://www.spacecentre.nz/resources/faq/solar-system/venus/how-old-would-i-be.html
#Venus year == 0.615 times the legth of an Earth year

print("You age on Venus is", round(age / 0.615,1))

# 7: How old they are in Neptune years
#source:
#https://www.spacecentre.nz/resources/faq/solar-system/neptune/how-old-would-i-be.html
#Neptune year == 165 Earth years long

print("You age on Neptune is", round(age / 165,2))

# 8: Whether they are the same age as you, older or younger
my_age = relativedelta(datetime.today(),datetime(1981,1,28)).years

if age == my_age:
    print("You are the same age as me! Let's celebrate together!")
elif age > my_age:
    print('You are older than me. Please have a seat.')
else:
    print('You are younger than me!')

# 9: If older or younger, how many years difference
age_dif = abs(age - my_age)

print("Our age difference is",age_dif,"years. But never mind. It's only", round(age_dif/165.2,2), "years on Neptune.")

# 10: If they were born in an even or odd year
even_or_odd = "even year" if bd.year%2 == 0 else "odd year"

print("You are born in an " + even_or_odd + ".")

# 11: How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once)
#source:
#https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States

url = wiki.page('List of presidents of the United States').html()
presidents = pd.read_html(url)[0]
presidents.columns = ['presidency','portrait','name','term','party1','party2','election','vice_president']
presidents = presidents.loc[~presidents.duplicated(subset=['name'])]

#format dates
presidents['term_start'] = presidents.term.apply(lambda x: datetime.strptime(re.sub('\[.\]','',x.split('–')[0]),'%B %d, %Y'))
presidents['term_end'] = presidents.term.apply(lambda x: datetime.strptime(re.sub('\[.\]','',x.split('–')[1].replace('Incumbent',datetime.today().strftime('%B %d, %Y'))),'%B %d, %Y'))

presidents.loc[(presidents.term_start>=bd)&(presidents.party2=='Democratic')]

demo_count = presidents.loc[(presidents.term_start>=bd)&(presidents.party2=='Democratic')].shape[0]

print('There has been a president from the Democratic Party in office',demo_count, "times since you were born.")

# 12: Which US President was in office when they were born (1960 onward)
presidents_name = presidents.loc[(presidents.term_start<=bd)].sort_values(by=['term_start']).iloc[-1]['name'].split('(')[0]

print("President "+ presidents_name + " was in office when you were born.")
