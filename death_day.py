import datetime
import random

LIFE_EXPECTANCY = 80
SMOKER_PENALITY = 5
DRUNKER_PENALITY = 5
JOGGIN = 5
penalized_years = 0

def message_with_lines(message):
    print (message)
    print(len(message)*"-")

message_with_lines("Vamos a predecir cuando vas a morir" )



def penalized_question(question):
    response = None
    while response != "S" and response != "N":
        response = input(question +"[S/N]").upper()
    return response =="S"

birth_date = datetime.datetime.strptime(input("Que dia nacistes[dd/mm/YYYY]: "),"%d/%m/%Y")

if penalized_question ("¿Fumas?"):
    penalized_years += SMOKER_PENALITY

if  penalized_question ("¿Bebes?"):
    penalized_years += DRUNKER_PENALITY

if penalized_question("¿Haces deporte?"):
    penalized_years += JOGGIN

average_lifespan = LIFE_EXPECTANCY//2+random.randint(0, LIFE_EXPECTANCY//2)-penalized_years
deth_day = birth_date + datetime.timedelta(days= 365*average_lifespan)


days_to_death = deth_day - datetime.datetime.now()

print("El dia de tu mmuerte sera el {}".format(deth_day.strftime("%d/%m/%Y")))
print("Te quedan {} de vida".format(days_to_death.days))






