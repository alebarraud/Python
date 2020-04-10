#! /usr/bin/python

# 6ta Practica Laboratorio 
# Complementos Matematicos I
# Ejemplo parseo argumentos

import argparse
import matplotlib.pyplot as plt
import numpy as np
import math
import random
from collections import defaultdict


class LayoutGraph:

    def __init__(self, grafo, iters, gravedad, temperatura, refresh, repulsion, atraccion, epsilon, esparcimiento, verbose=True):    
        '''
    	Parametros de layout:            
	    iters: cantidad de iteraciones a realizar
    	refresh: Numero de iteraciones entre actualizaciones de pantalla. 
   		0 -> se grafica solo al final.
	    repulsion: constante usada para calcular la repulsion entre nodos
   		atraccion: constante usada para calcular la atraccion de aristas
    	verbose: imprime mas informacion             
    	gravedad: la gravedad atrae a los vertices al centro del marco
    	tempertura: la temperatura permite tener variaciones en el sistema
    	epsilon: constante que sirve para mantener el modulo entre vertices
    	esparcimiento: constante usada para calcular el esparcimiento de los vertices
		'''
        
    	#coord_x: coordenada x de los vertices, por defecto en 0
    	#coord_y: coordenada y de los vertices, por defecto en 0
    	#accumulator_x: fuerzas acumuladas en la coordenada x de los vertices
    	#accumulator_y: fuerzas acumuladas en la coordenada y de los vertices
        self.grafo = grafo
        self.coord_x = defaultdict(lambda: 0)
        self.coord_y = defaultdict(lambda: 0)
        self.accumulator_x = defaultdict(lambda: 0)
        self.accumulator_y = defaultdict(lambda: 0)
    	#W : ancho maximo del marco
    	#H : altura maxima del marco
        self.W = 1000
        self.H = 1700
        self.gravedad = gravedad
        self.temperatura = temperatura
        self.iters = iters
        self.verbose = verbose
        self.refresh = refresh
        self.repulsion = repulsion
        self.atraccion = atraccion
        self.esparcimiento = esparcimiento
        #area del marco
        self.area = self.W * self.H
        self.k = self.esparcimiento * (math.sqrt((self.area) / len(self.grafo[0])))
        self.epsilon = epsilon


    def initialize_accumulators(self):
        for vertices in self.grafo[0]:
            self.accumulator_x[vertices] = 0
            self.accumulator_y[vertices] = 0

        

    def compute_attraction_forces(self):
        aristas=self.grafo[1]
        for (v1,v2) in aristas:
            distancia = self.distance(v1,v2)
            if(distancia > self.epsilon):
                mod_fa = (distancia**2 / self.k) * self.atraccion  #copiamos mal de internet la formula
                self.accumulator_x[v1] += mod_fa *(self.coord_x[v2] - self.coord_x[v1]) / distancia
                self.accumulator_y[v1] += mod_fa *(self.coord_y[v2] - self.coord_y[v1]) / distancia
                self.accumulator_x[v2] -= mod_fa *(self.coord_x[v2] - self.coord_x[v1]) / distancia
                self.accumulator_y[v2] -= mod_fa *(self.coord_y[v2] - self.coord_y[v1]) / distancia



    def compute_repulsion_forces(self):
        for v in self.grafo[0]:
            for u in self.grafo[0]:
                if u != v:
                    if(self.distance(v,u) < self.epsilon):
                        resorte_x = random.randint(-11, 11)
                        resorte_y = random.randint(-11, 11)
                    else:
                        mod_fr = self.repulsion * ((self.k)**2 / self.distance(v,u))   #cambiamos esto
                        resorte_x = mod_fr * (self.coord_x[u] - self.coord_x[v]) / self.distance(v,u)
                        resorte_y = mod_fr * (self.coord_y[u] - self.coord_y[v]) / self.distance(v,u)
                    self.accumulator_x[u] += resorte_x
                    self.accumulator_y[u] += resorte_y


    def compute_gravity_forces(self):
        for vertice in self.grafo[0]:
            self.accumulator_x[vertice] = self.accumulator_x[vertice] - self.coord_x[vertice] * self.gravedad
            self.accumulator_y[vertice] = self.accumulator_y[vertice] - self.coord_y[vertice] * self.gravedad
			

    def update_positions(self):
        for vertice in self.grafo[0]:
            modulo_de_acumuladas = math.sqrt((self.accumulator_x[vertice]**2) + (self.accumulator_y[vertice]**2))
            if (modulo_de_acumuladas > self.temperatura):
                self.accumulator_x[vertice] = (self.accumulator_x[vertice] / modulo_de_acumuladas) * self.temperatura
                self.accumulator_y[vertice] = (self.accumulator_y[vertice] / modulo_de_acumuladas) * self.temperatura
            self.coord_x[vertice] += self.accumulator_x[vertice]
            self.coord_y[vertice] += self.accumulator_y[vertice]
            #los vertices se mantienen adentro del marco
            if(self.coord_x[vertice] < 1):
                self.coord_x[vertice] = 1
            if(self.coord_x[vertice] > (self.W - 1)):
                self.coord_x[vertice] = (self.W - 1)
            if(self.coord_y[vertice] < 1):
                self.coord_y[vertice] = 1
            if(self.coord_y[vertice] > (self.H - 1)):
                self.coord_y[vertice] = (self.H - 1)
                
                
    def update_temperature(self):
        self.temperatura = self.temperatura - self.temperatura / 20


    def randomize_position(self):
        for vertices in self.grafo[0]:
            self.coord_x[vertices] = random.randint(1, self.W - 1)
            self.coord_y[vertices] = random.randint(1, self.H - 1)

    
    def distance(self,v,u):
        return math.sqrt(((self.coord_x[u] - self.coord_x[v])**2) + ((self.coord_y[u] - self.coord_y[v])**2))
         

    def step(self, grafico):
        self.initialize_accumulators()
        self.compute_attraction_forces()
        self.compute_repulsion_forces()
        self.compute_gravity_forces()
        self.update_positions()
        self.update_temperature()


    def dibujar(self):
        plt.clf()
        for vertice in self.grafo[0]:
            plt.scatter(self.coord_x[vertice], self.coord_y[vertice])
        for arista in self.grafo[1]:
            plt.plot([self.coord_x[arista[0]], self.coord_x[arista[1]]], [self.coord_y[arista[0]], self.coord_y[arista[1]]])
        plt.show()
        plt.pause(0.03)
       

    def layout(self):
        self.randomize_position()
        plt.ion()
        dibujo = self.dibujar()
        i = 0    
       	while(i < self.iters and self.temperatura > 1):
	        self.step(dibujo)
	        if not(i % self.refresh):
	            self.dibujar()
        	i += 1
        self.dibujar()
        plt.ioff()
        plt.show()
        

def leer_grafo_archivo(file_name):
    vertices = []
    aristas = []
    f = open(file_name, 'r')
    #cantidad de vertices
    i = int(f.readline().strip(" \n"))
    while i != 0:
        v = f.readline().split()
        vertices += v
        i -= 1
    linea = f.readline()
    while linea != "":
        e = (linea.split()[0], linea.split()[1])
        aristas += [e]
        linea = f.readline()
    grafo = (vertices, aristas)
    return grafo



def main():
    # Definimos los argumentos de linea de comando que aceptamos
    parser = argparse.ArgumentParser()

    # Verbosidad, opcional, False por defecto
    parser.add_argument(
        '-v', '--verbose', 
        action='store_true', 
        help='Muestra mas informacion al correr el programa'
    )
    # Cantidad de iteraciones, opcional, 50 por defecto
    parser.add_argument(
        '--iters',
        type=int,
        help='Cantidad de iteraciones a efectuar', 
        default=50
    )
    # Temperatura inicial
    parser.add_argument(
        '--temperatura',
        type=float, 
        help='Temperatura inicial', 
        default=100.0
    )
    
    # Archivo del cual leemos el grafo
    
    parser.add_argument(
        'file_name',
        help='Archivo de entrada'
    )
    

    # Fuerza de gravedad, por defecto 1
    parser.add_argument(
        '--gravedad',
        type = float,
        help = 'Fuerza de gravedad',
        default = 1
    )
    
    # Fuerza de atraccion, por defecto 11
    parser.add_argument(
        '--atraccion',
        type = float,
        help = 'Fuerza de atraccion',
        default = 30
    )

    # Fuerza de repulsion, por defecto 1.6
    parser.add_argument(
        '--repulsion',
        type = float,
        help = 'Fuerza de repulsion',
        default = 0.3
    )    
        
    # Modulo minimo, por defecto 0.05
    parser.add_argument(
    	'--epsilon',
    	type = float,
    	help = 'Modulo minimo entre vertices',
    	default = 0.05
    )
    
    # Cantidad de iteraciones antes de graficar, por defecto 4
    parser.add_argument(
        '--refresh',
        type = int,
        help = 'Cantidad de iteraciones antes de graficar',
        default = 4
    )
    
    # Constante de esparcimiento, por defecto 1.7
    parser.add_argument(
    	'--esparcimiento',
    	type = float,
    	help = 'Constante para modificar el esparcimiento de los vertices',
    	default = 1.7
    )
    
    args = parser.parse_args()

    # Descomentar abajo para ver funcionamiento de argparse
    #print(args.verbose)
    #print(args.iters)    
    #print(args.file_name)
    #print(args.temperatura)
    # return
    
    grafo = leer_grafo_archivo(args.file_name)
    

    # Creamos nuestro objeto LayoutGraph
    layout_gr = LayoutGraph(
        grafo, 
        iters=args.iters,
        gravedad = args.gravedad,
        temperatura = args.temperatura,
        atraccion = args.atraccion,
        repulsion = args.repulsion,
        epsilon = args.epsilon,
        refresh=args.refresh,
        esparcimiento = args.esparcimiento,
        verbose=args.verbose
        )
    
    # Ejecutamos el layout
    layout_gr.layout()
    return


if __name__ == '__main__':
    main()
