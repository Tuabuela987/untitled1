import datetime

ano = int(input("Dime al año: "))
mes = int(input("Dime el mes: "))
dia = int(input("Dime el dia: "))
hoy = datetime.datetime.now()

print(hoy-datetime.datetime(year=ano, month=mes, day=dia))

