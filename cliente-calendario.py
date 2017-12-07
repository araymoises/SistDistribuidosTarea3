# saved as greeting-client.py
import Pyro4
import argparse

anio = 2017
parser = argparse.ArgumentParser(description='Cliente python rmi para obtener un calendario de un anio xxxx')
parser.add_argument('anio', type=int,
                    help='Entero xxxx que representa el anio a generar del calendario')
arg = parser.parse_args()
if arg.anio > 1990:
	anio = arg.anio
else:
	print 'Agrege el anio para el calendario'


greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")    # use name server object lookup uri shortcut
calendario = greeting_maker.get_fortune(anio)
print calendario