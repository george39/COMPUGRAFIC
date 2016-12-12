import pygame
import random
ANCHO=800
ALTO=600
BLANCO=(255,255,255)
NEGRO=(0,0,0)
VERDE=(0,255,0)


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


class Jugador_nivel2(pygame.sprite.Sprite):
    bloques = None
    def __init__(self, img_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = img_sprite
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 550
        self.var_x = 0
        self.var_y = ""
        self.con = 0
        self.dir = 0
        self.vida = 1
        
    def update(self):
        self.vida
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.con < 2:
            self.con += 1
        else:
            self.con = 0
        
        #LIMITE CON LOS BORDES
        if self.rect.right>ANCHO-100:
            self.rect.right=ANCHO-100
            self.var_x=0

        if self.rect.left<100:
            self.rect.left=100
            self.var_x=0
        
        if self.rect.bottom>ALTO-100:
            self.rect.bottom=ALTO-100
            

        if self.rect.top<100:
            self.rect.top=100
                    
           
        '''    
        ls_choque = pygame.sprite.spritecollide(self,self.bloques,False)
        
        for b in ls_choque:
                if self.var_x > 0:
                    self.rect.right = b.rect.left
                if self.var_x < 0:
                    self.rect.left = b.rect.right
                if self.var_y>0:
                    self.rect.bottom=b.rect.top
                if self.var_y<0:
                    self.rect.top=b.rect.bottom
        '''  
    def no_mover2(self):
            """ Usuario no pulsa teclas """
            self.var_y = 0 



class Jugador2(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=550
        self.var_x=0
        self.var_y=0
        self.vida=1
        self.con=0
        self.dir=0
    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y

    def no_mover(self):
        """ Usuario no pulsa teclas """
        self.var_x = 0    


class jugador(pygame.sprite.Sprite):
    lp=None
    la=None
    def __init__(self, img_sprite):
        pygame.sprite.Sprite.__init__(self)
        '''
        self.image=pygame.Surface([30,50])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=0
        '''
        self.image = img_sprite
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.var_x = 0
        self.var_y = 0
        self.con = 0
        self.dir = 0
        self.vida = 1
    def gravedad(self):
        
        if self.var_y==0:
            self.var_y=1
        else:
            self.var_y+=0.35

        
        
        # Detener movimiento vertical
           
        '''
        if self.rect.y >= ALTO - self.rect.height and self.var_y >= 0:
            self.var_y = 0
            self.rect.y = ALTO - self.rect.height    
        '''
        if self.rect.y >= ALTO-18-self.rect.height and self.var_y >=0:
            self.rect.bottom=ALTO-18
            self.var_y=0
          
     
    def update(self):
        self.vida
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.con < 4:
            self.con += 1
        else:
            self.con = 0

        self.gravedad()
        self.rect.x+=self.var_x
        
        l_col=pygame.sprite.spritecollide(self,self.lp,False)
        for pl in l_col:
            if self.var_x>0:
                self.rect.right=ANCHO#pl.rect.left
            else:
                self.rect.left=pl.rect.right
        
        
               
        self.rect.y+=self.var_y
        l_col=pygame.sprite.spritecollide(self,self.lp,False)
        for pl in l_col:
            if self.var_y>0:
                self.rect.bottom=pl.rect.top
                if pl.var_y!=0:
                    self.rect.y+=pl.var_y
            else:
                self.rect.top=pl.rect.bottom
                if pl.var_y!=0:
                    self.rect.y-=pl.var_y
            self.var_y=0

        #CHOQUES CON LOS BORDES
        if self.rect.right>100:
            self.rect.right=100


        if self.rect.left<100:
            self.rect.left=100
            #self.var_x=0        

    def no_mover(self):
        """ Usuario no pulsa teclas """
        self.var_x = 0 

class jugador3(pygame.sprite.Sprite):
    lp=None
    la=None
    def __init__(self, img_sprite):
        pygame.sprite.Sprite.__init__(self)
        '''
        self.image=pygame.Surface([30,50])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=0
        '''
        self.image = img_sprite
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.var_x = 0
        self.var_y = 0
        self.con = 0
        self.dir = 0
        self.vida = 1
    def gravedad(self):
        
        if self.var_y==0:
            self.var_y=1
        else:
            self.var_y+=0.35

        
        
        # Detener movimiento vertical
           
        '''
        if self.rect.y >= ALTO - self.rect.height and self.var_y >= 0:
            self.var_y = 0
            self.rect.y = ALTO - self.rect.height    
        '''
        if self.rect.y >= ALTO-18-self.rect.height and self.var_y >=0:
            self.rect.bottom=ALTO-18
            self.var_y=0
          
     
    def update(self):
        self.vida
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.con < 4:
            self.con += 1
        else:
            self.con = 0

        self.gravedad()
        self.rect.x+=self.var_x
        '''
        l_col=pygame.sprite.spritecollide(self,self.lp,False)
        for pl in l_col:
            if self.var_x>0:
                self.rect.right=ANCHO#pl.rect.left
            else:
                self.rect.left=pl.rect.right
        
        '''
               
        self.rect.y+=self.var_y
        '''
        l_col=pygame.sprite.spritecollide(self,self.lp,False)
        for pl in l_col:
            if self.var_y>0:
                self.rect.bottom=pl.rect.top
                if pl.var_y!=0:
                    self.rect.y+=pl.var_y
            else:
                self.rect.top=pl.rect.bottom
                if pl.var_y!=0:
                    self.rect.y-=pl.var_y
            self.var_y=0
        '''
        '''
        #CHOQUES CON LOS BORDES
        if self.rect.right>100:
            self.rect.right=100


        if self.rect.left<100:
            self.rect.left=100
            #self.var_x=0        
        '''
        if self.rect.right>ANCHO:
            self.rect.right=ANCHO
            self.var_x=0

        if self.rect.left<100:
            self.rect.left=100
            self.var_x=0
              
    def no_mover(self):
        """ Usuario no pulsa teclas """
        self.var_x = 0 

class enemigo(pygame.sprite.Sprite):
    bloques = None
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=ANCHO
        self.rect.y=ALTO
        self.var_x=0
        self.var_y=0
        self.disparar=False
        self.vida=0
        self.tiempo=random.randrange(20)
    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        self.tiempo-=1
        if self.tiempo==0:
            self.disparar=True
            self.tiempo=random.randrange(20)


class enemigopatron(pygame.sprite.Sprite):
    bloques = None
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=0#ANCHO
        self.rect.y=0#ALTO
        self.var_x=0
        self.var_y=0
        self.disparar=False
        self.vida=3
        self.tiempo=random.randrange(20)
    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        self.tiempo-=1
        if self.tiempo==0:
            self.disparar=True
            self.tiempo=random.randrange(20) 

        #limites
        ''' 
        if self.rect.right>ANCHO-150:
            #self.rect.right=ANCHO-150
            self.var_x-=2

        if self.rect.left<150:
            #self.rect.left=150
            self.var_x+=2
        
        if self.rect.top<0:
            #self.rect.top=100 
            self.var_y+=2 
        if self.rect.bottom==300:
            self.var_x-=2
            self.var_y=0
        
        if self.rect.left==100:
            self.var_y-=2
            self.var_x=0
            #self.rect.bottom=ALTO-400
        '''    

                     


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
        '''
        if self.dir==3:
            self.var_y=-10
            self.var_x=0
                

        if self.dir==0:
            self.var_y+=10
            self.var_x=0
        '''
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y

class bala2(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0

        self.var_x=10
        self.var_y=10
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


class Hongos(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=100
        self.var_x=0
        self.var_y=0
         
    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y


class bloque(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=100
        self.var_x=0
        self.var_y=0
         
    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y


def pausa():
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausado = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pantalla.fill(NEGRO)
        texto=fuente.render("PAUSADO", True, BLANCO)
        pantalla.blit(texto,(100,100))
        texto=fuente.render("presione P para continuar o Q para terminar", True, BLANCO)
        pantalla.blit(texto,(100,400))
        pygame.display.update()            
        '''            
        pantalla.fill(NEGRO)
        
        texto=fuente.render("PAUSADO", True, BLANCO)
        pantalla.blit(texto,(100,100))
        texto=fuente.render("presione P para continuar o Q para terminar", True, BLANCO)
        pantalla.blit(texto,(100,400))
        '''
        pygame.display.update()
        #reloj.tick(2) 

''' 
def dibujar_bloques(gruposprite1,gruposprite2):
    # DIBUJA LA PRIMERA FILA DE BLOQUES
    for i in range(1):
        b=Bloque('img/bloque.png')
        b.rect.x=600
        b.rect.y=700
        gruposprite1.add(b)
        gruposprite2.add(b)
'''
if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])


    fuente=pygame.font.SysFont("Arial",36)
    '''
    texto=fuente.render("Ejemplo de letrero", True, BLANCO)
    pantalla.blit(texto,(100,100))
    pygame.display.flip()
    '''
    #PRIMER NIVEL
    #************************************************************************
    #************************************************************************ 
    todos=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    asensores=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    jugadoresvida=pygame.sprite.Group()

    ebalas=pygame.sprite.Group()
    hongos= pygame.sprite.Group()


    fondo=pygame.image.load('img/fond.png')
    dim_fondo=fondo.get_rect()
    ventana=fondo.subsurface(0,2248,ANCHO,ALTO)
    ''' 
    fondo2=pygame.image.load('img/f.png')
    dim_fondo2=fondo2.get_rect()
    ventana=fondo2.subsurface(0,2000,ANCHO,ALTO)
    '''
    #JUGADOR    
    animal = Recortar('img/soldier.png', 32,32) 
    jp=jugador(animal[4][7])
    todos.add(jp)
    jugadores.add(jp)
     
    #JUGADOR CON VIDA
    jp2=Jugador2("img/soldier2.png")
    jp2.rect.x=100
    jp2.rect.y=508

    
    '''
    #DIBUJAR ENEMIGOS
    for i in range(10):
        en=enemigo('img/enemigo.png')
        en.rect.x=random.randrange(ANCHO,11000)
        en.rect.y=ALTO-90#random.randrange(ALTO-200)
        en.var_x=-5            
        enemigos.add(en)
        todos.add(en)
    '''
    for i in range(10):
        en=enemigo('img/enemigo.png')
        en.rect.x=random.randrange(ANCHO,5000)
        en.rect.y=ALTO-100
        #en.var_x=(-1)*random.randrange(1,10)
        en.var_x=(-1)*random.randrange(3,4)
        enemigos.add(en)
        todos.add(en)    
    
    
    #DIBUJAR LOS BLOQUES
    for i in range(20):
        blo=bloque('img/bloque.png')
        blo.rect.x=random.randrange(800,ANCHO+9000)
        blo.rect.y=500
        blo.var_x=-3
        plataformas.add(blo)
        todos.add(blo)
    
    for i in range(1):
        hongo=Hongos('img/hongo.png')
        hongo.rect.x=random.randrange(800,ANCHO+2000)
        hongo.rect.y=450
        hongo.var_x=-3
        hongos.add(hongo)
        todos.add(hongo)
    '''
    b1=bloque('img/bloque.png')
    #b1.image.fill(VERDE)
    b1.var_y=3
    plataformas.add(b1)
    todos.add(b1)
    '''
    jp.lp=plataformas
    jp.la=asensores
    #********************************************************************


    #SEGUNDO NIVEL
    #********************************************************************
    fondo2=pygame.image.load('img/im3.jpeg')
    dim_fondo2=fondo2.get_rect()
    ventana2=fondo2.subsurface(3488,0,ANCHO,ALTO)

    todos2=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    asensores=pygame.sprite.Group()
    jugadores2=pygame.sprite.Group()
    balas2=pygame.sprite.Group()
    enemigos2=pygame.sprite.Group()
    jugadoresvida=pygame.sprite.Group()

    animal2 = Recortar('img/soldiernivel2.png', 32,32) 
    j2=Jugador_nivel2(animal2[4][7])
    todos2.add(j2)
    jugadores2.add(j2)
    '''
    #ENEMIGOS HORIZONTALES 
    for i in range(30):
        en2=enemigo('img/pirana1.png')
        en2.rect.x=random.randrange(100,ANCHO-100)
        en2.rect.y=random.randrange(-3000,300)
        #en.var_x=(-1)*random.randrange(1,10)
        en2.var_y=random.randrange(2,4)
        enemigos2.add(en2)
        todos2.add(en2)

    #ENEMIGOS VERTICALES
    for i in range(30):
        en3=enemigo('img/pira.png')
        en3.rect.x=random.randrange(-3000,0)
        en3.rect.y=random.randrange(0,ALTO)
        #en.var_x=(-1)*random.randrange(1,10)
        en3.var_x=random.randrange(2,4)
        enemigos2.add(en3)
        todos2.add(en3) 
    '''
    #ENEMIGO PATRON
    for i in range(1):
        en4=enemigopatron('img/pantano.png')
        en4.rect.x=random.randrange(100,ANCHO-100)
        en4.rect.y=0#random.randrange(-30,300)
        #en.var_x=(-1)*random.randrange(1,10)
        en4.var_y=random.randrange(2,4)
        enemigos2.add(en4)
        todos2.add(en4)        
      
    #********************************************************************
    #********************************************************************
    #          NIVEL 3
    #********************************************************************
    fondo3=pygame.image.load('img/im3.jpeg')
    dim_fondo3=fondo3.get_rect()
    ventana3=fondo3.subsurface(3488,0,ANCHO,ALTO)

    todos3=pygame.sprite.Group()
    enemigo3=pygame.sprite.Group()
    jugadores3=pygame.sprite.Group()

    animal3 = Recortar('img/soldier.png', 32,32) 
    j3=jugador3(animal3[4][7])
    todos3.add(j3)
    jugadores3.add(j3) 


    #********************************************************************
    var_x=0
    pos_x=0
    var_y=0
    pos_y=0
    var_y2=0
    pos_y2=0
    conenemi=50
    nivel =0
    nivel2=1
    nivel3=0
    enemimuerots = 10

    
    abajo=False
    arriba=False
    izquierda=False
    derecha=True

    reloj=pygame.time.Clock()
    seleccionar="play"
    pag=0
    terminar=False

    while not terminar:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                terminar=True
                #exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                pag+=1
                
            if pag==0:
                pantalla.fill(NEGRO)
                texto=fuente.render("INICIO", True, BLANCO)
                pantalla.blit(texto,(100,100))
                imagen=pygame.image.load('img/kameha.png')
                pantalla.blit(imagen,[120,150])
                pygame.display.flip()
                
            
            
                
          

            #menu pausa
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausa()
                if event.key==pygame.K_RIGHT:
                    jp.var_x=2
                    jp.var_y=0
                    jp.dir=2

                    j2.var_x=2
                    j2.var_y=0
                    j2.dir=2

                    j3.var_x=2
                    j3.var_y=0
                    j3.dir=2
                   
                    #b.var_x=-3
                if event.key==pygame.K_LEFT:
                    jp.var_x=-2
                    jp.var_y=0
                    jp.dir=1

                    j2.var_x=-2
                    j2.var_y=0
                    j2.dir=1


                    j3.var_x=-2
                    j3.var_y=0
                    j3.dir=1


                    '''
                    arriba = False
                    abajo = False
                    izquierda = True
                    
                    derecha = False
                    '''
                if event.key==pygame.K_UP:
                    jp.var_y=-8
                    jp.rect.y += -2
                    
                    j2.var_y=-2
                    j2.var_x=0
                    j2.dir=3

                    j3.var_y=-8
                    j3.rect.y += -2
                    j3.var_x=0
                        
                    arriba = True
                    abajo = False
                    izquierda = False
                    derecha = False

                if event.key == pygame.K_DOWN:
                    j2.var_y=2
                    j2.var_x=0
                    j2.dir=0

                   
                    
                    arriba = False
                    abajo = True
                    izquierda = False
                    derecha = False

                if event.key== pygame.K_SPACE:
                    be = bala2("img/kameha.png")
                    b= bala("img/kameha.png")
                    b.rect.x=jp.rect.x+10
                    b.rect.y=jp.rect.y+10
                    b.dir=jp.dir
                    
                    balas.add(b)
                    todos.add(b)


                    be.rect.x=j2.rect.x+10
                    be.rect.y=j2.rect.y+10
                    be.dir=j2.dir
                    balas2.add(be)
                    todos2.add(be)
                    
                    
                   
               
            if event.type == pygame.KEYUP:

                if event.key==pygame.K_SPACE:
                    #balas.remove(b)
                    todos.remove(b)
                    be.dir=9
                if event.key == pygame.K_LEFT and jp.var_x < 0:
                    jp.no_mover()

                    #j2.no_mover2()

                if event.key == pygame.K_RIGHT and jp.var_x > 0:
                        jp.no_mover()
                           
                
                if event.key == pygame.K_UP and j2.var_y < 0:
                        
                        j2.no_mover2()

                if event.key == pygame.K_DOWN and j2.var_y > 0:
                        
                        j2.no_mover2()
                
                #no mover 3
                if event.key==pygame.K_SPACE:
                    #balas.remove(b)
                    todos.remove(b)
                    be.dir=9
                if event.key == pygame.K_LEFT and j3.var_x < 0:
                    j3.no_mover()

                    #j2.no_mover2()

                if event.key == pygame.K_RIGHT and j3.var_x > 0:
                        j3.no_mover()
                           
                
                
        #ELIMINAR AL ENEMIGO

            
            
                   
        for bl in balas:
            ls_impacto=pygame.sprite.spritecollide(bl,enemigos,True)
            for im in ls_impacto:
                enemimuerots-=1
                print "choque", enemimuerots
                balas.remove(bl)
                todos.remove(bl)
                
                if im.vida==0:
                    enemigos.remove(im)
                    todos.remove(im)

                   
                   
        
        #ELIMINAR AL JUGADOR 
        ls_choque=pygame.sprite.spritecollide(jp,enemigos, True)
        for elemento in ls_choque:
        
            jp.vida-=1
            print jp.vida
            if jp.vida==0:
                jugadores.remove(jp)
                todos.remove(jp)
        

        #CHOCAR Y COJER UNA VIDA EL JUGADOR
        ls_choque=pygame.sprite.spritecollide(jp,hongos, True)
        for elemento in ls_choque:
            jp.vida+=1
            if jp.vida==2:
                jugadores.remove(jp)
                todos.remove(jp)
                jp2.rect.x=100
                jp2.rect.y=508
                jugadores.add(jp2)
                todos.add(jp2)
            #jugadores.add(jp2)
            #todos.add(jp2)
            print jp.vida
        
        ls_choque=pygame.sprite.spritecollide(jp2,enemigos, True)
        for elemento in ls_choque:
            jp2.vida-=1
            jp.vida-=1

            print jp.vida
            print "vida menos jp2",jp2.vida
            if  jp2.vida==0 and jp.vida ==1:
                jugadores.remove(jp2)
                todos.remove(jp2)
                jugadores.add(jp)
                todos.add(jp)
        
        
        #ELIMINAR ENEMIGOS SEGUNDO NIVEL
        for bal2 in balas2:
            ls_impacto=pygame.sprite.spritecollide(bal2,enemigos2,True)
            for im in ls_impacto:
                enemimuerots-=1
                print "choque", enemimuerots
                balas2.remove(bal2)
                todos.remove(bal2)
                
                if im.vida==0:
                    enemigos2.remove(im)
                    todos2.remove(im)
        
        '''
        if jp.vida==2:
            j2.vida=2
        '''    
        #ELIMINAR JUGADOR SEGUNDO NIVEL
        
        ls_choque=pygame.sprite.spritecollide(j2,enemigos2, True)
        for elemento in ls_choque:
            j2.vida=jp.vida
            j2.vida-=1
            jp.vida-=1
            print "vida j2",j2.vida
            print "vida jp",jp.vida
            '''
            if j2.vida==0:
                jugadores2.remove(j2)
                todos2.remove(j2)
            '''
        '''
                
        for jug2 in enemigos2:
            ls_impacto=pygame.sprite.spritecollide(jug2,jugadores2,True)
            for im2 in ls_impacto:
                
                
                im2.vida-=1
                
                print "vida j2",j2.vida 
                print "im vida ",im2.vida
                
                
                if im.vida==0:
                    enemigos2.remove(jug2)
                    todos2.remove(jug2)
            '''
       

        '''
        for bl2 in balas2:
            ls_impacto=pygame.sprite.spritecollide(bl2,enemigos2,True)
            for im2 in ls_impacto:
                #enemimuerots2-=1
                print "choque", enemimuerots
                balas2.remove(bl2)
                todos2.remove(bl2)
                
                if im2.vida==0:
                    enemigos2.remove(im2)
                    todos2.remove(im2)        
        '''
                    
                            
        '''
        for ju in enemigos:
            ls_impacto2=pygame.sprite.spritecollide(ju,jugadores,False)
            for im in ls_impacto2:
                im.vida
                perder-=1
                print perder
                
                if jp.vida == 0:
                    jugadores.remove(im)
                    todos.remove(im)
                
                print jp.vida
                im.vida-=1
                if im.vida==0:
                    jugadores.remove(im)
                    todos.remove(im)            
                '''

        #LIMITES DEL PATRON        
        if en4.rect.left<0:
            en4.var_y=5
            en4.var_x=0 

        if en4.rect.bottom>ALTO-200:
            en4.var_x=5
            en4.var_y=0 

        if en4.rect.right>ANCHO:#-en.rect.right:
            en4.var_y=-5
            en4.var_x=0             
        
        if en4.rect.top<0:
            en4.var_x=-5
            en4.var_y=0      
            if en4.rect.left<0:
                en4.var_y=5
                en4.var_x=0    


        #ELIMINAR BALAS QUE SALGAN DE LA PANTALLA 
        for eb in balas2:
            if eb.rect.x < 0 or eb.rect.x > ANCHO or eb.rect.y > ALTO or eb.rect.y<0:
                balas2.remove(eb)
                todos2.remove(eb)

         
        #ANIMACION DEL JUGADOR 1
        if jp.var_x==0:
            jp.image=animal[0][jp.dir]
        else:
            jp.image=animal[0+jp.con][jp.dir]

        #ANIMACION JUGADOR SEGUNDO NIVEL  
        if j2.var_y== 0 and j2.var_x == 0:
            j2.image=animal2[1][j2.dir]
        else:
            j2.image=animal2[1+j2.con][j2.dir] 

        

        #ANIMACION DEL JUGADOR 3
        if j3.var_x==0:
            j3.image=animal3[0][j3.dir]
        else:
            j3.image=animal3[0+j3.con][j3.dir]


        #ATAJO PARA PASAR MUNDO 1
        if jp.rect.top==blo.rect.bottom:
            #pos_y=1
            pos_x=(dim_fondo.width-ANCHO)
            ventana=fondo.subsurface(pos_x,2248,ANCHO,ALTO)

        
        #ATAJO PARA PASAR MUNDO 2
        if j2.rect.right==ANCHO-100:
            #pos_y=1
            pos_x=(dim_fondo2.height-ALTO)
            ventana2=fondo2.subsurface(3488,pos_x,ANCHO,ALTO) 

        #MOVIMIENTO DEL FONDO 1
        if jp.var_x >0 and pos_x < (dim_fondo.width - ANCHO):
            pos_x+=2
        if jp.var_x<0 :
            pos_x-=2
        if pos_x>0 and pos_x < (dim_fondo.width - ANCHO):
            ventana=fondo.subsurface(pos_x,2248,ANCHO,ALTO)


        #movimiento fondo dos
        if j2.var_y >0 and pos_y < (dim_fondo2.height - ALTO):
            pos_y+=2
        if j2.var_y<0 :
            pos_y-=2
        if pos_y>0 and pos_y < (dim_fondo2.height - ALTO):
            ventana2=fondo2.subsurface(3488,pos_y,ANCHO,ALTO)

        
        #MOVIMIENTO DEL FONDO 3
        if j3.var_x >0 and pos_x < (dim_fondo3.width - ANCHO):
            pos_y2+=2

        if j3.var_x<0 :
            pos_y2-=2

        if pos_x>0 and pos_x < (dim_fondo3.width - ANCHO):
            ventana3=fondo3.subsurface(pos_y2,2248,ANCHO,ALTO)
        

        

        #LLAMAR SEGUNDO NIVEL
        
        if pos_x>0 and pos_x==(dim_fondo.width-ANCHO):
            
            jp.var_y-=1
            nivel+=1
            nivel2=1
            
            print "nivel 2",nivel2
            print "nivel",nivel
            #j2.vida=jp.vida
            todos.remove(en)
            jugadores.remove(en)
           

        #LLAMAR NIVEL 3

        if pos_x>0 and pos_x==(dim_fondo2.height-ALTO):
            nivel2+=1
            #j3.var_y-=1
            #nivel+=1
            #j2.vida=jp.vida
            todos2.remove(en4)
            jugadores2.remove(en4)    


        #CUANDO EL JUGADOR PIERDE EN EL PRIMER NIVEL
        if jp.vida <1 and nivel==0:
                
            pantalla.fill(NEGRO)
            texto=fuente.render("GAME OVER", True, BLANCO)
            pantalla.blit(texto,(100,100))
            #imagen=pygame.image.load('img/kameha.png')
            #pantalla.blit(imagen,[120,150])
            pygame.display.flip()
           


         
              
        
        '''
        if jp.vida==4:
            
            jp2=Jugador2("img/soldier2.png")
            jugadores.remove(jp)
            todos.remove(jp)
            jp2.rect.x=100
            jp2.rect.y=520
            jugadores.add(jp2)
            todos.add(jp2)

        '''

        #ACTUALIZA PANTALLA DEL PRIMER NIVEL
        if pag ==1 and jp.vida!=0 and nivel==0:   
            #pantalla.fill(BLANCO)
            pantalla.blit(ventana,(0,0))
            todos.update()
            todos.draw(pantalla)
            pygame.display.flip()
            reloj.tick(60)

        #CUANDO EL JUGADOR PIERDE EN SEGUNDO NIVEL
        if j2.vida <1 :
                
                pantalla.fill(NEGRO)
                texto=fuente.render("PERDIO", True, BLANCO)
                pantalla.blit(texto,(100,100))
                imagen=pygame.image.load('img/kameha.png')
                pantalla.blit(imagen,[120,150])
                pygame.display.flip()
        
        #ACTUALIZAR PANTALLA SEGUNDO NIVEL
        if nivel>1 and j2.vida>0 and nivel2==1:
            nivel3+=1
            print "suma nivel",nivel
            pantalla.blit(ventana2,(0,0))
            todos2.update()
            todos2.draw(pantalla)
            pygame.display.flip()
            reloj.tick(60)
        
        #ACTUALIZAR PANTALLA  NIVEL 3
        if nivel2>1 and nivel3>1:
            #print "nivel",nivel
            pantalla.blit(ventana3,(0,0))
            todos3.update()
            todos3.draw(pantalla)
            pygame.display.flip()
            reloj.tick(60)    

