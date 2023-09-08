from time import sleep
import random
from rich import print
from rich.progress import track


def process_data():
    sleep(0.02)

print("Iniciando el 'ataque' en : \n")

countdown =  random.randint(3, 10)
for counter_decreasing in range(countdown, 0, -1):
    print("{} ... \n".format(counter_decreasing))

for _ in track(range(100), description='[cyan]Conectando a los servidores...\n'):
    process_data()

porcentaje_de_hackeo = 0
while porcentaje_de_hackeo <= 100:
    print("Hackeando los servidores de la NASA: {} % completado.\n".format(porcentaje_de_hackeo))
    porcentaje_de_hackeo += 10
    sleep(random.randint(1, 4))

for _ in track(range(100), description='[green]Procesando los datos hackeados...\n'):
    process_data()

if porcentaje_de_hackeo >= 100:
    print("Los servidores de la NASA han sido hackeados de manera EXITOSA.\n")