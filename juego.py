import pygame
import random

from jugador import *
from bloque import *
from enemigo import *

ANCHO = 1000
ALTO = 580

VERDE=(0,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0, 0, 255)
AMARILLO=(255, 255, 0)
CIAN=(0, 255, 255)
MAGNETA=(255, 0, 255)
ROSADO=(234,137,154)
FUCSIA=(222,076,138)
GRIS=(215,215,215)

#-------------------------------------------------------
#FUNCION PARA RECORTAR SPRITES
def Recortar(archivo,anc,alc):
    matriz = []
    imagen = pygame.image.load(archivo).convert_alpha()
    i_ancho, i_alto =imagen.get_size()
    for x in range(i_ancho/anc):
        linea = []
        for y in range(i_alto/alc):
            cuadro = (x*anc,y*alc,anc,alc)
            linea.append(imagen.subsurface(cuadro))
        matriz.append(linea)
    return matriz


#CLASE PARA CREAR LAS BALAS
class bala(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0

        self.var_x=0
        self.var_y=0
        self.dir=""
        #self.dir2=1


    def update(self):
	   
	    
        if self.dir==2:
        	self.var_x+=10
        	self.var_y=0

        if self.dir==1:
        	self.var_x-=10
        	self.var_y=0	
		
		if self.dir==3:
			self.var_y=-10
			self.var_x=0
        		

        if self.dir==0:
        	self.var_y+=10
        	self.var_x=0
        
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y 
        

    	'''
    	if self.dir==0 and jp.var_x>0:
            self.var_x=10
            
        self.rect.x+=self.var_x
        '''
        
      

        
        
       	
        
    	'''
        if jp.var_x>0:
        	b.var_x=10
        	#self.dir=0

           	#b.rect.x+=self.var_x
	            
	    	self.rect.x+=self.var_x
	    ''' 

           


#---------------------------------------------------------------
bloque=[]
#INICIO DEL JUEGO
if __name__ == '__main__':
    # CONFIGURACION DEL JUEGO
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    # SPRITES GRUPOS
    todos = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    bloques = pygame.sprite.Group()


    dibujar_bloques(todos,bloques) #FUNCION QUE DIBUJA LOS BLOQUES EN LA PANTALLA
    animal = Recortar('img/animales2.png',32,32)
    jp = Jugador(animal[6][0])
    jugadores.add(jp)
    todos.add(jp)
    jp.bloques = bloques
    balas=pygame.sprite.Group()

    '''
    for i in range(1):
        bv=Bloque('img/bloque.png')
        bv.rect.x=800
        bv.rect.y=0
        todos.add(bv)
        bloques.add(bv)
    '''
    for i in range(1):
        en=Enemigo(animal[0][4])
        en.rect.x=random.randrange(0,ANCHO-990)
        en.rect.y=random.randrange(0,ANCHO-990)
        en.var_x=(-1)*random.randrange(1,10)
        en.var_y=random.randrange(3,10)
        enemigos.add(en)
        todos.add(en)
    
    #SEGUNDO ENEMIGO
    for i in range(1):
        en2=Enemigo(animal[0][4])
        en2.rect.x=ANCHO
        en2.rect.y=0
        en2.var_x=(-1)*random.randrange(1,10)
        en2.var_y=random.randrange(3,10)
        enemigos.add(en2)
        todos.add(en2)

    #TERCER ENEMIGO
    for i in range(1):
        en3=Enemigo(animal[0][4])
        en3.rect.x=340
        en3.rect.y=0
        en3.var_x=(-1)*random.randrange(1,10)
        en3.var_y=random.randrange(3,10)
        enemigos.add(en3)
        todos.add(en3) 

        #CUARTO ENEMIGO
    for i in range(1):
        en4=Enemigo(animal[0][4])
        en4.rect.x=650
        en4.rect.y=0
        en4.var_x=(-1)*random.randrange(1,10)
        en4.var_y=random.randrange(3,10)
        enemigos.add(en4)
        todos.add(en4)

        #QUINTO ENEMIGO
    for i in range(1):
        en5=Enemigo(animal[0][4])
        en5.rect.x=ANCHO
        en5.rect.y=100
        en5.var_x=(-1)*random.randrange(1,10)
        en5.var_y=random.randrange(3,10)
        enemigos.add(en5)
        todos.add(en5)

    #SEXTO ENEMIGO
    for i in range(1):
        en6=Enemigo(animal[0][4])
        en6.rect.x=ANCHO
        en6.rect.y=200
        en6.var_x=(-1)*random.randrange(1,10)
        en6.var_y=random.randrange(3,10)
        enemigos.add(en6)
        todos.add(en6)        


    #SEPTIMO ENEMIGO
    for i in range(1):
        en7=Enemigo(animal[0][4])
        en7.rect.x=ANCHO
        en7.rect.y=300
        en7.var_x=(-1)*random.randrange(1,10)
        en7.var_y=random.randrange(3,10)
        enemigos.add(en7)
        todos.add(en7)

    #OCTAVO ENEMIGO
    for i in range(1):
        en8=Enemigo(animal[0][4])
        en8.rect.x=ANCHO
        en8.rect.y=400
        en8.var_x=(-1)*random.randrange(1,10)
        en8.var_y=random.randrange(3,10)
        enemigos.add(en8)
        todos.add(en8)    
        

    reloj=pygame.time.Clock()
    con=0
    pos_x=ANCHO
    pos_y=0
    fin=False
    conenemi = 50

    while not fin:
        #Control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.var_x=7
                    jp.var_y=0
                    jp.dir=2
                if event.key == pygame.K_LEFT:
                    jp.var_x=-7
                    jp.var_y=0
                    jp.dir=1
                if event.key == pygame.K_UP:
                    jp.var_y=-7
                    jp.var_x=0
                    jp.dir=3
                if event.key == pygame.K_DOWN:
                    jp.var_y=7
                    jp.var_x=0
                    jp.dir=0
                if event.key== pygame.K_SPACE:
                    b= bala("img/kameha.png")
                    #if jp.var_x>0:
                    b.rect.x=jp.rect.x+10
                    b.rect.y=jp.rect.y+10
                    b.dir=jp.dir
                    
                    balas.add(b)
                    todos.add(b)
            if event.type==pygame.KEYUP:
            	if event.key==pygame.K_SPACE:
            		b.dir=9
            

        #ELIMINAR JUGADOR
        #ls_choque=pygame.sprite.spritecollide(jp,enemigos, False)
        #for elemento in ls_choque:
        
        for ju in enemigos:
            ls_impacto=pygame.sprite.spritecollide(ju,jugadores,False)
            for im in ls_impacto:
                #balas.remove(bl)
                #todos.remove(bl)
                print jp.vida
                im.vida-=1
                if im.vida==0:
                    jugadores.remove(im)
                    todos.remove(im) 

        for bl in balas:
            ls_impacto=pygame.sprite.spritecollide(bl,enemigos,False)
            for im in ls_impacto:
                balas.remove(bl)
                todos.remove(bl)
                #im.vida-=1
                if im.vida==0:
                    enemigos.remove(im)
                    todos.remove(im)       
                   
    	'''
    	if pygame.sprite.spritecollide(jp,enemigos, False):
    		jp.vida-=1
    	print jp.vida
    	
    	for muerte in ls_choque:	
			if pygame.sprite.spritecollide(muerte,enemigos, False)and jp.vida < 0:
				jugadores.remove(jp)
				todos.remove(jp)
        	#print 'Golpe'                    	
        '''
       

        #CHOQUE DEL SPRITE CON LOS BORDES                    
        if jp.rect.x>ANCHO-jp.rect.width:
            jp.rect.x=ANCHO-jp.rect.width
            jp.var_x=0
        if jp.rect.x<0:
            jp.rect.x=0
            jp.var_x=0
        if jp.rect.y>ALTO-jp.rect.height:
            jp.rect.y=ALTO-jp.rect.height
            jp.var_y=0
        if jp.rect.y<0:
            jp.rect.y=0
            jp.var_y=0

        #CHOQUE DEL PRIMER ENEMIGO CON LOS BORDES
        
        if en.rect.left<0:
            en.var_y=5
            en.var_x=0 

        if en.rect.bottom>ALTO:
            en.var_x=5
            en.var_y=0 

        if en.rect.right>ANCHO:#-en.rect.right:
            en.var_y=-5
            en.var_x=0             
        
        if en.rect.top<0:
            en.var_x=-5
            en.var_y=0      
            if en.rect.left<0:
                en.var_y=5
                en.var_x=0 

        #CHOQUE SEGUNDO ENEMIGO CON LOS BORDES 


        if en2.rect.left>ANCHO:
            en2.var_x=-5
            en2.var_y=0 

        if en2.rect.bottom>ALTO:
            en2.var_x=5
            en2.var_y=0 

        if en2.rect.right>ANCHO:#-en.rect.right:
            en2.var_y=-5
            en2.var_x=0             
        
        if en2.rect.top<0:
            en2.var_x=-5
            en2.var_y=0      
            if en2.rect.left<0:
                en2.var_y=5
                en2.var_x=0 
       
        
       #CHOQUES DEL TERCER ENEMIGO
        
        if en3.rect.left>0:
            en3.var_y=5
            en3.var_x=0
        
        if en3.rect.bottom>ALTO:
            en3.var_x=5
            en3.var_y=0 
    	
        if en3.rect.right>658:#-en.rect.right:
            en3.var_y=-5
            en3.var_x=0             
        
        if en3.rect.top<0:
            en3.var_x=-5
            en3.var_y=0      
            if en3.rect.left==340:
                en3.var_y=5
                en3.var_x=0

        #CHOQUE CUARTO ENEMIGO 
        if en4.rect.left>0:
            en4.var_y=5
            en4.var_x=0
        
        if en4.rect.bottom>ALTO:
            en4.var_x=5
            en4.var_y=0 
    	
        if en4.rect.right>ANCHO:#-en.rect.right:
            en4.var_y=-5
            en4.var_x=0             
        
        if en4.rect.top<0:
            en4.var_x=-5
            en4.var_y=0      
            if en4.rect.left==650:
                en4.var_y=5
                en4.var_x=0 

        #CHOQUES QUINTO ENEMIGO 
                      
        if en5.rect.left<0:
            en5.var_x=5
            en5.var_y=0
        
        if en5.rect.bottom>ALTO:
            en5.var_x=5
            en5.var_y=0 
    	
        if en5.rect.right>ANCHO:#-en.rect.right:
            en5.var_x=-5
            en5.var_y=0             
        
        if en5.rect.top<0:
            en5.var_x=-5
            en5.var_y=0      
            if en5.rect.left<0:
                en5.var_x=5
                en5.var_y=0


        #CHOQUES SEXTO ENEMIGO 
                      
        if en6.rect.left<0:
            en6.var_x=5
            en6.var_y=0
        
        if en6.rect.bottom>ALTO:
            en6.var_x=5
            en6.var_y=0 
    	
        if en6.rect.right>ANCHO:#-en.rect.right:
            en6.var_x=-5
            en6.var_y=0             
        
        if en6.rect.top<0:
            en6.var_x=-5
            en6.var_y=0      
            if en6.rect.left<0:
                en6.var_x=5
                en6.var_y=0


        #CHOQUES SEPTIMO ENEMIGO 
                      
        if en7.rect.left<0:
            en7.var_x=5
            en7.var_y=0
        
        if en7.rect.bottom>ALTO:
            en7.var_x=5
            en7.var_y=0 
    	
        if en7.rect.right>ANCHO:#-en.rect.right:
            en7.var_x=-5
            en7.var_y=0             
        
        if en7.rect.top<0:
            en7.var_x=-5
            en7.var_y=0      
            if en7.rect.left<0:
                en7.var_x=5
                en7.var_y=0 


        #CHOQUES SEPTIMO ENEMIGO 
                      
        if en8.rect.left<0:
            en8.var_x=5
            en8.var_y=0
        
        if en8.rect.bottom>ALTO:
            en8.var_x=5
            en8.var_y=0 
    	
        if en8.rect.right>ANCHO:#-en.rect.right:
            en8.var_x=-5
            en8.var_y=0             
        
        if en8.rect.top<0:
            en8.var_x=-5
            en8.var_y=0      
            if en8.rect.left<0:
                en8.var_x=5
                en8.var_y=0                       
      
        '''
        if en3.rect.bottom>168:
            en3.var_x=-5
            en3.var_y=0 
            if en3.rect.left<98:
                en3.var_y=5
                en3.var_x=0

        '''
        
           

        jp.image=animal[9+jp.con][jp.dir]
        pantalla.fill(BLANCO)
        #pantalla.blit(enemigo[9+con][5],(pos_x,100))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)








            
