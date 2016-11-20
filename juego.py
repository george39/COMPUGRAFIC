import pygame
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

        if self.rect.y >= ALTO-self.rect.height:
            self.rect.bottom=ALTO
            self.var_y=0

    def update(self):
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
        if self.rect.right>ANCHO:
            self.rect.right=ANCHO


        if self.rect.left<0:
            self.rect.left=0
            #self.var_x=0        

    def no_mover(self):
        """ Usuario no pulsa teclas """
        self.var_x = 0    



class bloque(pygame.sprite.Sprite):
    def __init__(self,an,al,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=px
        self.rect.y=py
        self.var_y=0
        self.limsup=100
        self.liminf=400

    def update(self):
        self.rect.y+=self.var_y
        if self.rect.y > self.liminf:
            self.var_y=self.var_y*(-1)
        if self.rect.y < self.limsup:
            self.var_y=self.var_y*(-1)


if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    todos=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    asensores=pygame.sprite.Group()

    fondo=pygame.image.load('img/im3.jpeg')
    dim_fondo=fondo.get_rect()
    ventana=fondo.subsurface(0,2000,ANCHO,ALTO)
        
    animal = Recortar('img/soldier.png', 32,32) 
    jp=jugador(animal[4][6])
    todos.add(jp)

    b=bloque(100,40,600,500)
    plataformas.add(b)
    todos.add(b)

    b1=bloque(100,50,100,200)
    b1.image.fill(VERDE)
    b1.var_y=3
    plataformas.add(b1)
    todos.add(b1)

    jp.lp=plataformas
    jp.la=asensores

    var_x=0
    pos_x=0

    reloj=pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    jp.var_x=3
                    jp.var_y=0
                    jp.dir=2
                if event.key==pygame.K_LEFT:
                    jp.var_x=-3
                    jp.var_y=0
                    jp.dir=1
                if event.key==pygame.K_UP:
                    jp.var_y=-8
                    jp.rect.y += -2

            
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and jp.var_x < 0:
                        jp.no_mover()
                        
                    if event.key == pygame.K_RIGHT and jp.var_x > 0:
                        jp.no_mover() 

                    
                       
        #ANIMACION DEL JUGADOR
        if jp.var_x==0:
            jp.image=animal[0][jp.dir]
        else:
            jp.image=animal[0+jp.con][jp.dir]
        
        #MOVIMIENTO DEL FONDO
        if jp.var_x >0 and pos_x < (dim_fondo.width - ANCHO):
            pos_x+=5
        if jp.var_x<0 :
            pos_x-=5
        if pos_x>0 and pos_x < (dim_fondo.width - ANCHO):
            ventana=fondo.subsurface(pos_x,2000,ANCHO,ALTO) 
        #pantalla.fill(BLANCO)
        pantalla.blit(ventana,(0,0))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
import pygame
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

        if self.rect.y >= ALTO-self.rect.height:
            self.rect.bottom=ALTO
            self.var_y=0

    def update(self):
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
        if self.rect.right>ANCHO:
            self.rect.right=ANCHO


        if self.rect.left<0:
            self.rect.left=0
            #self.var_x=0        

    def no_mover(self):
        """ Usuario no pulsa teclas """
        self.var_x = 0    



class bloque(pygame.sprite.Sprite):
    def __init__(self,an,al,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=px
        self.rect.y=py
        self.var_y=0
        self.limsup=100
        self.liminf=400

    def update(self):
        self.rect.y+=self.var_y

        if self.rect.y > self.liminf:
            self.var_y=self.var_y*(-1)
        if self.rect.y < self.limsup:
            self.var_y=self.var_y*(-1)


if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    todos=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    asensores=pygame.sprite.Group()

    fondo=pygame.image.load('img/f.png')
    dim_fondo=fondo.get_rect()
    ventana=fondo.subsurface(0,2000,ANCHO,ALTO)
        
    animal = Recortar('img/soldier.png', 32,32) 
    jp=jugador(animal[4][6])
    todos.add(jp)

    b=bloque(100,40,600,500)
    plataformas.add(b)
    todos.add(b)

    b1=bloque(100,50,100,200)
    b1.image.fill(VERDE)
    b1.var_y=3
    plataformas.add(b1)
    todos.add(b1)

    jp.lp=plataformas
    jp.la=asensores

    var_x=0
    pos_x=0

    reloj=pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    jp.var_x=3
                    jp.var_y=0
                    jp.dir=2
                if event.key==pygame.K_LEFT:
                    jp.var_x=-3
                    jp.var_y=0
                    jp.dir=1
                if event.key==pygame.K_UP:
                    jp.var_y=-8
                    jp.rect.y += -2

            
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and jp.var_x < 0:
                        jp.no_mover()
                        
                    if event.key == pygame.K_RIGHT and jp.var_x > 0:
                        jp.no_mover() 

                    
                       
        #ANIMACION DEL JUGADOR
        if jp.var_x==0:
            jp.image=animal[0][jp.dir]
        else:
            jp.image=animal[0+jp.con][jp.dir]
        
        #MOVIMIENTO DEL FONDO
        if jp.var_x >0 and pos_x < (dim_fondo.width - ANCHO):
            pos_x+=5
        if jp.var_x<0 :
            pos_x-=5
        if pos_x>0 and pos_x < (dim_fondo.width - ANCHO):
            ventana=fondo.subsurface(pos_x,2000,ANCHO,ALTO) 
        #pantalla.fill(BLANCO)
        pantalla.blit(ventana,(0,0))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
import pygame
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

        if self.rect.y >= ALTO-self.rect.height:
            self.rect.bottom=ALTO
            self.var_y=0

    def update(self):
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
        if self.rect.right>ANCHO:
            self.rect.right=ANCHO


        if self.rect.left<0:
            self.rect.left=0
            #self.var_x=0        

    def no_mover(self):
        """ Usuario no pulsa teclas """
        self.var_x = 0    



class bloque(pygame.sprite.Sprite):
    def __init__(self,an,al,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=px
        self.rect.y=py
        self.var_y=0
        self.limsup=100
        self.liminf=400

    def update(self):
        self.rect.y+=self.var_y
        if self.rect.y > self.liminf:
            self.var_y=self.var_y*(-1)
        if self.rect.y < self.limsup:
            self.var_y=self.var_y*(-1)


if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    todos=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    asensores=pygame.sprite.Group()

    fondo=pygame.image.load('img/im3.jpeg')
    dim_fondo=fondo.get_rect()
    ventana=fondo.subsurface(0,2000,ANCHO,ALTO)
        
    animal = Recortar('img/soldier.png', 32,32) 
    jp=jugador(animal[4][6])
    todos.add(jp)

    b=bloque(100,40,600,500)
    plataformas.add(b)
    todos.add(b)

    b1=bloque(100,50,100,200)
    b1.image.fill(VERDE)
    b1.var_y=3
    plataformas.add(b1)
    todos.add(b1)

    jp.lp=plataformas
    jp.la=asensores

    var_x=0
    pos_x=0

    reloj=pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    jp.var_x=3
                    jp.var_y=0
                    jp.dir=2
                if event.key==pygame.K_LEFT:
                    jp.var_x=-3
                    jp.var_y=0
                    jp.dir=1
                if event.key==pygame.K_UP:
                    jp.var_y=-8
                    jp.rect.y += -2

            
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and jp.var_x < 0:
                        jp.no_mover()
                        
                    if event.key == pygame.K_RIGHT and jp.var_x > 0:
                        jp.no_mover() 

                    
                       
        #ANIMACION DEL JUGADOR
        if jp.var_x==0:
            jp.image=animal[0][jp.dir]
        else:
            jp.image=animal[0+jp.con][jp.dir]
        
        #MOVIMIENTO DEL FONDO
        if jp.var_x >0 and pos_x < (dim_fondo.width - ANCHO):
            pos_x+=5
        if jp.var_x<0 :
            pos_x-=5
        if pos_x>0 and pos_x < (dim_fondo.width - ANCHO):
            ventana=fondo.subsurface(pos_x,2000,ANCHO,ALTO) 
        #pantalla.fill(BLANCO)
        pantalla.blit(ventana,(0,0))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
import pygame
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

        if self.rect.y >= ALTO-self.rect.height:
            self.rect.bottom=ALTO
            self.var_y=0

    def update(self):
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
        if self.rect.right>ANCHO:
            self.rect.right=ANCHO


        if self.rect.left<0:
            self.rect.left=0
            #self.var_x=0        

    def no_mover(self):
        """ Usuario no pulsa teclas """
        self.var_x = 0    



class bloque(pygame.sprite.Sprite):
    def __init__(self,an,al,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=px
        self.rect.y=py
        self.var_y=0
        self.limsup=100
        self.liminf=400

    def update(self):
        self.rect.y+=self.var_y

        if self.rect.y > self.liminf:
            self.var_y=self.var_y*(-1)
        if self.rect.y < self.limsup:
            self.var_y=self.var_y*(-1)


if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    todos=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    asensores=pygame.sprite.Group()

    fondo=pygame.image.load('img/f.png')
    dim_fondo=fondo.get_rect()
    ventana=fondo.subsurface(0,2000,ANCHO,ALTO)
        
    animal = Recortar('img/soldier.png', 32,32) 
    jp=jugador(animal[4][6])
    todos.add(jp)

    b=bloque(100,40,600,500)
    plataformas.add(b)
    todos.add(b)

    b1=bloque(100,50,100,200)
    b1.image.fill(VERDE)
    b1.var_y=3
    plataformas.add(b1)
    todos.add(b1)

    jp.lp=plataformas
    jp.la=asensores

    var_x=0
    pos_x=0

    reloj=pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    jp.var_x=3
                    jp.var_y=0
                    jp.dir=2
                if event.key==pygame.K_LEFT:
                    jp.var_x=-3
                    jp.var_y=0
                    jp.dir=1
                if event.key==pygame.K_UP:
                    jp.var_y=-8
                    jp.rect.y += -2

            
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and jp.var_x < 0:
                        jp.no_mover()
                        
                    if event.key == pygame.K_RIGHT and jp.var_x > 0:
                        jp.no_mover() 

                    
                       
        #ANIMACION DEL JUGADOR
        if jp.var_x==0:
            jp.image=animal[0][jp.dir]
        else:
            jp.image=animal[0+jp.con][jp.dir]
        
        #MOVIMIENTO DEL FONDO
        if jp.var_x >0 and pos_x < (dim_fondo.width - ANCHO):
            pos_x+=5
        if jp.var_x<0 :
            pos_x-=5
        if pos_x>0 and pos_x < (dim_fondo.width - ANCHO):
            ventana=fondo.subsurface(pos_x,2000,ANCHO,ALTO) 
        #pantalla.fill(BLANCO)
        pantalla.blit(ventana,(0,0))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
