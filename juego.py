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
        self.vida = 3
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
        if self.rect.y >= ALTO-self.rect.height and self.var_y >=0:
            self.rect.bottom=ALTO
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
    todos=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    asensores=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    jugadoresvida=pygame.sprite.Group()

    ebalas=pygame.sprite.Group()
    hongos= pygame.sprite.Group()


    fondo=pygame.image.load('img/im3.jpeg')
    dim_fondo=fondo.get_rect()
    ventana=fondo.subsurface(0,500,ANCHO,ALTO)
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
    jp2.rect.y=520

    
    #todos.add(jp2)
    #jugadores.add(jp2)
    #DIBUJAR ENEMIGOS
    for i in range(30):
        en=enemigo('img/enemigo.png')
        en.rect.x=random.randrange(ANCHO,11000)
        en.rect.y=ALTO-60#random.randrange(ALTO-200)
        en.var_x=-5
        
            
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

    var_x=0
    pos_x=0
    conenemi=50
    perder =0
    enemimuerots = 0

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
                
            
            
                
            

            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    jp.var_x=2
                    jp.var_y=0
                    jp.dir=2
                    #b.var_x=-3
                if event.key==pygame.K_LEFT:
                    jp.var_x=-2
                    jp.var_y=0
                    jp.dir=1
                if event.key==pygame.K_UP:
                    jp.var_y=-8
                    jp.rect.y += -2
                    

                if event.key== pygame.K_SPACE:
                    b= bala("img/kameha.png")
                    #if jp.var_x>0:
                    b.rect.x=jp.rect.x+10
                    b.rect.y=jp.rect.y+10
                    b.dir=jp.dir
                    balas.add(b)
                    todos.add(b)

            
               
            if event.type == pygame.KEYUP:

                if event.key==pygame.K_SPACE:
                    #balas.remove(b)
                    todos.remove(b)
                
                if event.key == pygame.K_LEFT and jp.var_x < 0:
                    jp.no_mover()

                if event.key == pygame.K_RIGHT and jp.var_x > 0:
                        jp.no_mover()    
                
                
        #ELIMINAR AL ENEMIGO

            
            
                   
        for bl in balas:
            ls_impacto=pygame.sprite.spritecollide(bl,enemigos,True)
            for im in ls_impacto:
                enemimuerots+=1
                print "choque"
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
            if jp.vida==4:
                jugadores.remove(jp)
                todos.remove(jp)
                jp2.rect.x=100
                jp2.rect.y=520
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
            if  jp2.vida==0 and jp.vida ==3:
                jugadores.remove(jp2)
                todos.remove(jp2)
                jugadores.add(jp)
                todos.add(jp)
                 

        
                    
                            
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

        #ANIMACION DEL JUGADOR
        if jp.var_x==0:
            jp.image=animal[0][jp.dir]
        else:
            jp.image=animal[0+jp.con][jp.dir]
        
        #MOVIMIENTO DEL FONDO
        if jp.var_x >0 and pos_x < (dim_fondo.width - ANCHO):
            pos_x+=2
        if jp.var_x<0 :
            pos_x-=2
        if pos_x>0 and pos_x < (dim_fondo.width - ANCHO):
            ventana=fondo.subsurface(pos_x,500,ANCHO,ALTO)

        
        if jp.vida <1:
                pantalla.fill(NEGRO)
                texto=fuente.render("GAME OVER", True, BLANCO)
                pantalla.blit(texto,(100,100))
                imagen=pygame.image.load('img/kameha.png')
                pantalla.blit(imagen,[120,150])
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
        
        if pag ==1 and jp.vida!=0:   
            #pantalla.fill(BLANCO)
            pantalla.blit(ventana,(0,0))
            todos.update()
            todos.draw(pantalla)
            pygame.display.flip()
            reloj.tick(60)
            
            

        