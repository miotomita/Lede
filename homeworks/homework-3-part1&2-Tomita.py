##PART1:Pokemon API

#import libraries
import requests
import json
##########
###1: What is the URL to the documentation?
url_documentation1 = 'https://pokeapi.co/docs/v2#pokemon-section'
print("the URL to the documentaion: ", url_documentation1)
print('---------')

###2: What pokemon has the ID of 55?
#ID & URL
id = '55'
url_pokemonapi = f"https://pokeapi.co/api/v2/pokemon/{id}/"   
r = requests.get(url_pokemonapi)
data_id55= r.json()
#print the name
print(data_id55['name'])
print('---------')

####3:How tall is that pokemon?
#The height of this Pokémon in decimetres. 
print(f"The height of {data_id55['name']} is {data_id55['height']} decimetres.")
print('---------')

###4: How many versions of Pokemon games have been released?
#API to get version-groups
url_games = 'https://pokeapi.co/api/v2/version-group/'
#get data
r = requests.get(url_games)
data_game = r.json()
#print
print(f"{data_game['count']} versions have been released.")
print('---------')

###5: Print out the name of every electric-type pokemon.
#As the only pokemon I know is Pikachu and google says it's an electric pokemon
#I first took a look at info on Pikachu to find ID for electric pokemons
id = 'pikachu' 
url_pokemonapi = f"https://pokeapi.co/api/v2/pokemon/{id}/"
r = requests.get(url_pokemonapi)
data_pikachu = r.json()
#get API url for electric pokemon
url_electric = data_pikachu['types'][0]['type']['url']
print(url_electric)
#get data
r = requests.get(url_electric)
data_electric = r.json()
#list of electric pokemons
e_pokemon_list = [e_pokemon['pokemon']['name'] for e_pokemon in data_electric['pokemon']]
#print
print(e_pokemon_list)
print('---------')

###6:What are electric-type Pokemon called in the Korean version of the game?
requests.get(url_electric).json()
korean_name = [name['name'] for name in data_electric['names'] if name['language']['name']=='ko'][0]
print(korean_name, '.....?')
print('---------')

###7:Who has a higher speed stat, Eevee or Pikachu?
names = ['Eevee','Pikachu']
dic = {}
for name in names:
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}/"
    r = requests.get(url)
    data = r.json()
    speed = [stat['base_stat'] for stat in data['stats'] if stat['stat']['name']=='speed'][0]
    dic[name] = speed
fastest = {val : key for key, val in dic.items()}[max(dic.values())]
print(f"{fastest} has a higher speed stat.")
print('---------')

#######################################################
##Part TWO: Weather API
print('PART2: Weather API')
###1: What is the URL to the documentation?
url_documentation2 = 'https://www.weatherapi.com/docs/'
print("The URL to the documentation: ",url_documentation2)
print('---------')

###2: Make a request for the current weather where you are born, or somewhere you've lived.
#source: API Explorer
#https://www.weatherapi.com/api-explorer.aspx
url_tokyo = 'http://api.weatherapi.com/v1/current.json?key=42febc308e914aaf9ed193214221306&q=Tokyo&aqi=yes'
r = requests.get(url_tokyo)
tokyo = r.json()
print(f"The current weather in {tokyo['location']['name']}:\n-Temperature: {tokyo['current']['temp_c']}°C\n-Condition: {tokyo['current']['condition']['text']}")
print('---------')

###3: Print out the country this location is in.
print(f"{tokyo['location']['name']} is in {tokyo['location']['country']}.")
print('---------')

###4: Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.
#temperatures
temp_tokyo_current = tokyo['current']['temp_c']
temp_tokyo_feels_like = tokyo['current']['feelslike_c']
#difference
temp_difference = temp_tokyo_current - temp_tokyo_feels_like
#note
if temp_difference >0:
    text = f"It feels {temp_difference} degrees Celcius colder" + f" in {tokyo['location']['name']}."
elif temp_difference ==0:
    text = "It feels as the same degree as the actual temperature" + f" in {tokyo['location']['name']}."
else:
    text = f"It feels {temp_difference} degrees Celcius warmer" + f" in {tokyo['location']['name']}."
#print
print(text)
print('---------')

###5: What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
#source: https://www.world-airport-codes.com/united-kingdom/london-heathrow-4171.html
#Heathrow Int'l Airport == 'LHR'
url_heathrow = 'http://api.weatherapi.com/v1/current.json?key=42febc308e914aaf9ed193214221306&q=LHR'
r = requests.get(url_heathrow)
heathrow = r.json()
temp_heathrow_current = heathrow['current']['temp_c']
print(f"It is {temp_heathrow_current} degrees Celcius at {heathrow['location']['name']}.")
print('---------')

###6: What URL would I use to request a 3-day forecast at Heathrow?
url_heathrow2 = 'http://api.weatherapi.com/v1/forecast.json?key=42febc308e914aaf9ed193214221306&q=LHR&days=3'
print(url_heathrow2)
print('---------')

###7: Print the date of each of the 3 days you're getting a forecast for.
r = requests.get(url_heathrow2)
heathrow2 = r.json()

print("The dates with forecasts are:")
for i in range(len(heathrow2['forecast']['forecastday'])):
    forecast_date = heathrow2['forecast']['forecastday'][i]['date']
    print(forecast_date)
print('---------')

###8: Print the maximum temperature of each of the days.
#dictionary data for #9
maxtemp_dic = {}
#pick up maxtemp for theeach days
print("The maximum temperature of the day is: ")
for i in range(len(heathrow2['forecast']['forecastday'])):
    forecast_date = heathrow2['forecast']['forecastday'][i]['date']
    maxtemp_c = heathrow2['forecast']['forecastday'][i]['day']['maxtemp_c']
    maxtemp_f = heathrow2['forecast']['forecastday'][i]['day']['maxtemp_f']
    #add data to the dictionary
    maxtemp_dic[forecast_date] = maxtemp_c 
    #print
    print(forecast_date, ": ", maxtemp_c, "°C, ", maxtemp_f, "°F")
print('---------')

###9: Print the day with the highest maximum temperature.
#reverse dictionary
maxtemp_dic_r = {val: key for key, val in maxtemp_dic.items()}
#search for the date
hottest_date = maxtemp_dic_r[max(maxtemp_dic.values())]
print(hottest_date)
