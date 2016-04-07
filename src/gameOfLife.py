'''
Created on 13 mars 2016

http://www.labri.fr/perso/nrougier/teaching/matplotlib/
http://venusch.blogspot.fr/2012/12/2d-animation-in-xy-plane-using-scatter.html
https://nickcharlton.net/posts/drawing-animating-shapes-matplotlib.html
@author: famil
'''
import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

VERSION = "0.1.1 - 04/04/2016"

class Bacterie:
    CONSO_DISTANCE = 5          # facteur de consommation energie par unite de distance
    ENERGIE_INITIALE = 300      # quantite energie initiale
    
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.food = self.ENERGIE_INITIALE 
    

    def aller_vers(self,xval,yval):
        '''
            Cette method calcul la quantité de nourriture necessaire pour aller de la position
            courante de la bacterie (self x,y) vers xval,yval.
            Si la bacterie n'a pas assez d'energie pour aller jusque là la fct retourne -1 sinon 1
        '''
        x_ant = self.x
        y_ant = self.y
        distance_parcourue = math.sqrt((xval- x_ant)**2 + (yval - y_ant)**2)
        current_food = self.food - distance_parcourue*self.CONSO_DISTANCE 
        if (current_food > 0):
            self.food = current_food
            etat = 0
            print( "bacterie:%s   nouvelles coord: (%d,%d) distance parcourue:%f    restant nourriture:%f" % (self.name, xval,yval,distance_parcourue,self.food))
        else :
            etat = -1
            print ("a court de nourriture : bacterie immobile")      
        return etat

        
    def afficher_position(self):
        print ("(",self.x,",",self.y,")")

    def propose_nouvelles_positions(self):
        '''
            Cette method propose une nouvelle position dans un espace defini par L
            Cette proposition n'est pas enteriee tant que la fonction aller_vers() n'est pas appelee.
            Si aller_vers() retourne 0 c'est qu'il y a assez de nourriture pour aller vers new_val_x et new_val_y
                On peut mettre à jour x,y avec les nouvelles valeurs.
            Sinon on ne bouge plus
        '''
        coords = []
        L = [3,2,1,0,-1,-2,-3]
        mon_choix_x = random.choice(L)
        mon_choix_y = random.choice(L)
        new_val_x = self.x + mon_choix_x
        new_val_y = self.y + mon_choix_y
        if (self.aller_vers(new_val_x, new_val_y) == 0):
            self.x = new_val_x
            self.y = new_val_y
        coords.append(self.x)
        coords.append(self.y)
        return coords


class gameOfLife:
    pool_bacteries = []
    
    def ajout_bacterie(self,bacterie):
        self.pool_bacteries.append(bacterie)

    def update_plot(self,i, fig, scat):
        coord_list = ()
        for bacterie in self.pool_bacteries:
            nv_coords = bacterie.propose_nouvelles_positions()
            b=list(coord_list)
            b.append(nv_coords)
            coord_list=tuple(b)
            # On definit sa taille entre 50 et 200
            scat.set_sizes([bacterie.food])
        #scat.set_offsets(([0, i],[50, i],[100, i]))
        scat.set_offsets(coord_list)
        
        # On colorize la bacterie de facon aleatoir
        color_spec = ['b','g','r','c','m','y','k']
        scat.set_color(random.choice(color_spec))
                
        
        return scat,


if __name__ == '__main__':
    
    mygame = gameOfLife()
    ma_bacterie_1 = Bacterie("bacterie-1",0, 0)
    mygame.ajout_bacterie(ma_bacterie_1)
    ma_bacterie_2 = Bacterie("bacterie-2",10, 10)
    mygame.ajout_bacterie(ma_bacterie_2)
    

    # pour definir le graphique    
    fig =  plt.figure()                
    ax = fig.add_subplot(111)
    ax.grid(True, linestyle = '-', color = '0.75')
    # definition des axes
    ax.set_xlim([-50, 200])
    ax.set_ylim([-50, 200])
    x = [0]
    y = [0]
    # s= size, c= for color
    scat = plt.scatter(x, y, s=75, c = x)
    scat.set_alpha(0.6)
    anim = animation.FuncAnimation(fig, mygame.update_plot, fargs = (fig, scat),
                                   frames = 100, interval = 1000)
    plt.show()
