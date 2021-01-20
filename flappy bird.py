import pygame
import sys
import random
import time
import pygame_menu
import json 
pygame.init()
surface = pygame.display.set_mode((576,660))
 
 
 
 
def set_difficulty(value, difficulty):
    # Do the job here !
    pass
def level1():
    def base():
        screen.blit(base_surface,[start_x , 580])
        screen.blit(base_surface,[start_x + 576 , 580])
    def createPipe():
        random_pipe = random.choice(pipe_height)
        bottom_pipe = pipe_surface.get_rect(midtop = (530 ,random_pipe))
        top_pipe = pipe_surface.get_rect(midbottom =(530 , random_pipe- 300))
        return bottom_pipe , top_pipe
    def movepipe(pipes):
        for pipe in pipes:
            pipe.centerx -= 3

        return pipes
    def drawpipe(pipes):
        for pipe in pipes:
            if pipe.bottom >= 600:

                screen.blit(pipe_surface, pipe)
            else:
                flip_pipe =  pygame.transform.flip(pipe_surface , False , True)
                screen.blit(flip_pipe ,pipe)
    def rotate_bird(bird):
        rotated_bird = pygame.transform.rotozoom(bird ,birdmovement* -4 ,1)
        return rotated_bird
    def checkCollision(pipes):
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                hit_sound.play()
                 
                time_set()
                return False
            if bird_rect.top <= -80 or bird_rect.bottom >= 600:
                return False
        return True
   
    def draw_score(gamestate):
        if gamestate ==  "maingame":
            font_surface = font.render(f"Score:{int(score)}", True, (255,255,255))
            font_rect = font_surface.get_rect(center = ((60, 25)))
            screen.blit(font_surface , font_rect)
        if gamestate == "gameover":
            high_score_font_surface = font.render(f"Highscore:{int(highscore)}", True, (255,0, 0))
            high_score_font_rect =high_score_font_surface.get_rect(center = ((288,550)))
            screen.blit(high_score_font_surface, high_score_font_rect)
            
        if gamestate == "return":
            font_return = font2.render("PRESS 'C' TO GO BACK or PRESS 'SPACE' TO CONTINUE" ,True, (255,0,0))
            font_return_rect = font_return.get_rect(center = (265,200))
            screen.blit(font_return , font_return_rect)
        
    def update_score(score, highscore):
        if score > highscore:
            highscore = score
        return highscore
    def gameover():
         gameoverrect = gameoversurface.get_rect(center = (288, 330))
         screen.blit(gameoversurface,gameoverrect)
    def create_cloud():
        random_cloud= random.choice(cloudpos)
        newcloud = cloud_surface.get_rect(center = (530 , random_cloud))
        return newcloud

    def movecloud(clouds):
        for cloud in clouds:
            cloud.centerx -= 5
             
        return clouds
    def drawcloud(clouds):
        for cloud in clouds:
            screen.blit(cloud_surface, cloud)
    def checkCollision2(clouds):
        for cloud in clouds:
            if bird_rect.colliderect(cloud):
                hit_sound.play()
                
                time_set()
                return False
        return True
    def time_set():
        gap = time.sleep(.3)
    def won():
        won_font = font.render("you won move to level - 2", True ,(255,0,0))
        won_font_rect = won_font.get_rect(center =(250, 100))
        screen.blit(won_font, won_font_rect)
    def target():
        font3_surface = font3.render(f"Target:{(int(score_2))}",True,(0,255,0))
        font3_surface_rect = font3_surface.get_rect(center =(460 ,25))
        screen.blit(font3_surface  ,font3_surface_rect)
    def lives():
        fontlive_surface = live_font.render(f"Lives:{(int(live))}",True, (200,255,0))
        foont_rect =fontlive_surface.get_rect(center = (288,25))
        screen.blit(fontlive_surface,foont_rect)
    def lose():
        won_font = font.render("you Lose", True ,(255,0,0))
        won_font_rect = won_font.get_rect(center =(250, 100))
        screen.blit(won_font, won_font_rect)   
        
    pygame.init()
    width = 530
    height = 660
    gameActive = True
    
    

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Flappy bird")
    # icon 

    icon = pygame.image.load('blue-bird.png').convert()
    pygame.display.set_icon(icon)

    #pipe 
    pipe_surface = pygame.image.load('pipe-red.png').convert()
    pipe_list = []
    pipe_height= [300,400,450]
    # base surface 
    base_surface = pygame.image.load('base.png').convert()
    base_surface = pygame.transform.scale2x(base_surface).convert()
    start_x = 0

    #background
    bg_surface = pygame.image.load('background-day.png').convert()
    bg_surface =  pygame.transform.scale2x(bg_surface).convert()
    # bird image
    bird_surface = pygame.image.load("blue-bird.png").convert_alpha()
    bird_rect = bird_surface.get_rect(center = (80, 100))
    birdmovement = 0
    gravity = 0.15
    #game oversurface
    gameoversurface = pygame.image.load('gameover.jpg').convert_alpha()
   

    #clock
    clock = pygame.time.Clock()
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE , 1200)

    SPAWNCLOUD = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWNCLOUD,2000)
    #score 
    font = pygame.font.SysFont("camicsonsms" ,40)
    font2 = pygame.font.Font("freesansbold.ttf",16)
    font3 = pygame.font.Font("freesansbold.ttf",25)
    score_2 = 21
    #score
    score = 0
    highscore =0
    live_font =pygame.font.Font("freesansbold.ttf",25)
    live = 3
    # adding sound
    flap_sound = pygame.mixer.Sound('wing.wav')
    hit_sound = pygame.mixer.Sound('hit.wav')
    point_sound = pygame.mixer.Sound('point.wav')
    #cloud image
    cloud_surface = pygame.image.load('image.png').convert_alpha()
    cloud_surface  = pygame.transform.scale2x(cloud_surface )
    cloudlist= []
    cloudpos = [100,150, 200]

    while True:
        screen.blit(bg_surface,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == SPAWNCLOUD:
                cloudlist.append(create_cloud())
                
            if event.type == SPAWNPIPE:
                pipe_list.extend(createPipe())
                
                if gameActive :
                    
                    point_sound.play()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and gameActive:
                    flap_sound.play()
                    birdmovement = 0
                    birdmovement -= 5
                     
                    
                if event.key == pygame.K_SPACE and gameActive == False:
                    birdmovement = 0
                    if lives == 0:
                        score = 0
                        
                    if lives ==3 or score >= 1 or score <20:
                        score_2 = 21
                        score = 0
                    if lives == 2 or score >= 1 or score < 20:
                        score_2 = 21
                        score = 0
                    if lives == 1 or  score >= 1 or score < 20:
                        score_2 = 21
                        score = 0
                    gameActive = True
                    bird_rect.center = (80, 100)
                    pipe_list.clear()
                    cloudlist.clear()
                if event.key == pygame.K_SPACE and live == 0:
                    menu.mainloop(surface)
                        
                     
                if event.key == pygame.K_c:
                    
                    menu.mainloop(surface)
                    
        if gameActive:
            rotated_bird = rotate_bird(bird_surface)
            screen.blit(rotated_bird, bird_rect)
            #cloudlist = movecloud(cloudlist)
            #drawcloud(cloudlist)
            birdmovement += gravity
            bird_rect.centery += birdmovement
            gameActive = checkCollision(pipe_list)
             
            pipe_list = movepipe(pipe_list)
            drawpipe(pipe_list)
            draw_score("maingame")
            lives()
            score+= 0.01
            target()
            
            score_2 -= 0.01
            if score_2 <= 0:
                score_2 = 0
            if gameActive == False:
                live -=1
            
             
                
        #if gameActive:
            #gameActive = checkCollision2(cloudlist)
            
            
        else:
            draw_score("gameover") 
            draw_score("maingame")  
            highscore=  update_score(score , highscore)
            if live == 0:
                gameover()
                draw_score("return")
                lose()
            if score > 20:
                won()
                 
                draw_score("return")
        start_x -= 3
        base()
        if start_x <= - 576:
            start_x=0
        if score >=20 and score <= 24 :
             won()
             draw_score("return")
        
        clock.tick(120)
        pygame.display.update()
# level2 flappy bird     
def level2():
    def base():
        screen.blit(base_surface,[start_x , 580])
        screen.blit(base_surface,[start_x + 576 , 580])
    def createPipe():
        random_pipe = random.choice(pipe_height)
        bottom_pipe = pipe_surface.get_rect(midtop = (530 ,random_pipe))
        top_pipe = pipe_surface.get_rect(midbottom =(530 , random_pipe- 260))
        return bottom_pipe , top_pipe
    def movepipe(pipes):
        for pipe in pipes:
            pipe.centerx -= 4

        return pipes
    def drawpipe(pipes):
        for pipe in pipes:
            if pipe.bottom >= 600:

                screen.blit(pipe_surface, pipe)
            else:
                flip_pipe =  pygame.transform.flip(pipe_surface , False , True)
                screen.blit(flip_pipe ,pipe)
    def rotate_bird(bird):
        rotated_bird = pygame.transform.rotozoom(bird ,birdmovement* -4.5 ,1)
        return rotated_bird
    def checkCollision(pipes):
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                hit_sound.play()
                 
                time_set()
                return False
            if bird_rect.top <= -80 or bird_rect.bottom >= 600:
                return False
        return True
   
    def draw_score(gamestate):
        if gamestate ==  "maingame":
            font_surface = font.render(f"Score:{int(score)}", True, (255,255,255))
            font_rect = font_surface.get_rect(center = ((60, 25)))
            screen.blit(font_surface , font_rect)
        if gamestate == "gameover":
            high_score_font_surface = font.render(f"Highscore:{int(highscore)}", True, (255,0, 0))
            high_score_font_rect =high_score_font_surface.get_rect(center = ((288,550)))
            screen.blit(high_score_font_surface, high_score_font_rect)
            
        if gamestate == "return":
            font_return = font2.render("PRESS 'C' TO GO BACK or PRESS 'SPACE' TO CONTINUE" ,True, (255,0,0))
            font_return_rect = font_return.get_rect(center = (265,200))
            screen.blit(font_return , font_return_rect)
        
    def update_score(score, highscore):
        if score > highscore:
            highscore = score
        return highscore
    def gameover():
         gameoverrect = gameoversurface.get_rect(center = (288, 330))
         screen.blit(gameoversurface,gameoverrect)
    def create_cloud():
        random_cloud= random.choice(cloudpos)
        newcloud = cloud_surface.get_rect(center = (530 , random_cloud))
        return newcloud

    def movecloud(clouds):
        for cloud in clouds:
            cloud.centerx -= 5
             
        return clouds
    def drawcloud(clouds):
        for cloud in clouds:
            screen.blit(cloud_surface, cloud)
    def checkCollision2(clouds):
        for cloud in clouds:
            if bird_rect.colliderect(cloud):
                hit_sound.play()
                
                time_set()
                return False
        return True
    def time_set():
        gap = time.sleep(.3)
    def won():
        won_font = font.render("you won move to level - 2", True ,(255,0,0))
        won_font_rect = won_font.get_rect(center =(250, 100))
        screen.blit(won_font, won_font_rect)
    def target():
        font3_surface = font3.render(f"Target:{(int(score_2))}",True,(0,255,0))
        font3_surface_rect = font3_surface.get_rect(center =(460 ,25))
        screen.blit(font3_surface  ,font3_surface_rect)
    def lives():
        fontlive_surface = live_font.render(f"Lives:{(int(live))}",True, (200,255,0))
        foont_rect =fontlive_surface.get_rect(center = (288,25))
        screen.blit(fontlive_surface,foont_rect)
    def lose():
        won_font = font.render("you Lose", True ,(255,0,0))
        won_font_rect = won_font.get_rect(center =(250, 100))
        screen.blit(won_font, won_font_rect)   
        
    pygame.init()
    width = 530
    height = 660
    gameActive = True
    
    

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Flappy bird")
    # icon 

    icon = pygame.image.load('blue-bird.png').convert()
    pygame.display.set_icon(icon)

    #pipe 
    pipe_surface = pygame.image.load('pipe-red.png').convert()
    pipe_list = []
    pipe_height= [300,400,450]
    # base surface 
    base_surface = pygame.image.load('base.png').convert()
    base_surface = pygame.transform.scale2x(base_surface).convert()
    start_x = 0

    #background
    bg_surface = pygame.image.load('background-day.png').convert()
    bg_surface =  pygame.transform.scale2x(bg_surface).convert()
    # bird image
    bird_surface = pygame.image.load("blue-bird.png").convert_alpha()
    bird_rect = bird_surface.get_rect(center = (80, 100))
    birdmovement = 0
    gravity = 0.20
    #game oversurface
    gameoversurface = pygame.image.load('gameover.jpg').convert_alpha()
   

    #clock
    clock = pygame.time.Clock()
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE , 1200)

    SPAWNCLOUD = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWNCLOUD,2000)
    #score 
    font = pygame.font.SysFont("camicsonsms" ,40)
    font2 = pygame.font.Font("freesansbold.ttf",16)
    font3 = pygame.font.Font("freesansbold.ttf",25)
    score_2 = 51
    #score
    score = 0
    highscore =0
    live_font =pygame.font.Font("freesansbold.ttf",25)
    live = 3
    # adding sound
    flap_sound = pygame.mixer.Sound('wing.wav')
    hit_sound = pygame.mixer.Sound('hit.wav')
    point_sound = pygame.mixer.Sound('point.wav')
    #cloud image
    cloud_surface = pygame.image.load('image.png').convert_alpha()
    cloud_surface  = pygame.transform.scale2x(cloud_surface )
    cloudlist= []
    cloudpos = [100,150, 200]

    while True:
        screen.blit(bg_surface,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == SPAWNCLOUD:
                cloudlist.append(create_cloud())
                
            if event.type == SPAWNPIPE:
                pipe_list.extend(createPipe())
                
                if gameActive :
                    
                    point_sound.play()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and gameActive:
                    flap_sound.play()
                    birdmovement = 0
                    birdmovement -= 7
                     
                    
                if event.key == pygame.K_SPACE and gameActive == False:
                    birdmovement = 0
                    if lives == 0:
                        score = 0
                        
                    if lives ==3 or score >= 1 or score <50:
                        score_2 = 51
                        score = 0
                    if lives == 2 or score >= 1 or score < 50:
                        score_2 = 51
                        score = 0
                    if lives == 1 or  score >= 1 or score < 50:
                        score_2 = 51
                        score = 0
                    gameActive = True
                    bird_rect.center = (80, 100)
                    pipe_list.clear()
                    cloudlist.clear()
                    
                if event.key == pygame.K_SPACE and live == 0:
                    menu.mainloop(surface)
                    
                        
                     
                if event.key == pygame.K_c:
                    
                    menu.mainloop(surface)
                    
        if gameActive:
            rotated_bird = rotate_bird(bird_surface)
            screen.blit(rotated_bird, bird_rect)
            cloudlist = movecloud(cloudlist)
            drawcloud(cloudlist)
            birdmovement += gravity
            bird_rect.centery += birdmovement
            gameActive = checkCollision(pipe_list)
             
            pipe_list = movepipe(pipe_list)
            drawpipe(pipe_list)
            draw_score("maingame")
            lives()
            score+= 0.02
            target()
            
            score_2 -= 0.01
            if score_2 <= 0:
                score_2 = 0
            if gameActive == False:
                live -=1
           
             
                
        if gameActive:
            gameActive = checkCollision2(cloudlist)
            
            
        else:
            draw_score("gameover") 
            draw_score("maingame")  
            highscore=  update_score(score , highscore)
            if live == 0:
                gameover()
                draw_score("return")
                lose()
                
            if score >=50:
                won()
                draw_score("return")
        start_x -= 4
        base()
        if start_x <= - 576:
            start_x=0
        if score >=50 and score <= 54 :
             won()
             draw_score("return")
        
        clock.tick(120)
        pygame.display.update()
    
# final level    
def Final():
    def base():
        screen.blit(base_surface,[start_x , 580])
        screen.blit(base_surface,[start_x + 576 , 580])
    def createPipe():
        random_pipe = random.choice(pipe_height)
        bottom_pipe = pipe_surface.get_rect(midtop = (530 ,random_pipe))
        top_pipe = pipe_surface.get_rect(midbottom =(530 , random_pipe- 250))
        return bottom_pipe , top_pipe
    def movepipe(pipes):
        for pipe in pipes:
            pipe.centerx -= 4.5

        return pipes
    def drawpipe(pipes):
        for pipe in pipes:
            if pipe.bottom >= 600:

                screen.blit(pipe_surface, pipe)
            else:
                flip_pipe =  pygame.transform.flip(pipe_surface , False , True)
                screen.blit(flip_pipe ,pipe)
    def rotate_bird(bird):
        rotated_bird = pygame.transform.rotozoom(bird ,birdmovement* -5 ,1)
        return rotated_bird
    def checkCollision(pipes):
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                hit_sound.play()
                 
                time_set()
                return False
            if bird_rect.top <= -80 or bird_rect.bottom >= 600:
                return False
        return True
   
    def draw_score(gamestate):
        if gamestate ==  "maingame":
            font_surface = font.render(f"Score:{int(score)}", True, (255,255,255))
            font_rect = font_surface.get_rect(center = ((60, 25)))
            screen.blit(font_surface , font_rect)
        if gamestate == "gameover":
            high_score_font_surface = font.render(f"Highscore:{int(highscore)}", True, (255,0, 0))
            high_score_font_rect =high_score_font_surface.get_rect(center = ((288,550)))
            screen.blit(high_score_font_surface, high_score_font_rect)
            
        if gamestate == "return":
            font_return = font2.render("PRESS 'C' TO GO BACK or PRESS 'SPACE' TO CONTINUE" ,True, (255,0,0))
            font_return_rect = font_return.get_rect(center = (265,200))
            screen.blit(font_return , font_return_rect)
        
    def update_score(score, highscore):
        if score > highscore:
            highscore = score
        return highscore
    def gameover():
         gameoverrect = gameoversurface.get_rect(center = (288, 330))
         screen.blit(gameoversurface,gameoverrect)
    def create_cloud():
        random_cloud= random.choice(cloudpos)
        newcloud = cloud_surface.get_rect(center = (530 , random_cloud))
        return newcloud

    def movecloud(clouds):
        for cloud in clouds:
            cloud.centerx -= 5.2
             
        return clouds
    def drawcloud(clouds):
        for cloud in clouds:
            screen.blit(cloud_surface, cloud)
    def checkCollision2(clouds):
        for cloud in clouds:
            if bird_rect.colliderect(cloud):
                hit_sound.play()
                
                time_set()
                return False
        return True
    def time_set():
        gap = time.sleep(.3)
    def won():
        won_font = font.render("you won move to level - 2", True ,(255,0,0))
        won_font_rect = won_font.get_rect(center =(250, 100))
        screen.blit(won_font, won_font_rect)
    def target():
        font3_surface = font3.render(f"Target:{(int(score_2))}",True,(0,255,0))
        font3_surface_rect = font3_surface.get_rect(center =(460 ,25))
        screen.blit(font3_surface  ,font3_surface_rect)
    def lives():
        fontlive_surface = live_font.render(f"Lives:{(int(live))}",True, (200,255,0))
        foont_rect =fontlive_surface.get_rect(center = (288,25))
        screen.blit(fontlive_surface,foont_rect)
    def lose():
        won_font = font.render("you Lose", True ,(255,0,0))
        won_font_rect = won_font.get_rect(center =(250, 100))
        screen.blit(won_font, won_font_rect)   
        
    pygame.init()
    width = 530
    height = 660
    gameActive = True
    
    

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Flappy bird")
    # icon 

    icon = pygame.image.load('blue-bird.png').convert()
    pygame.display.set_icon(icon)

    #pipe 
    pipe_surface = pygame.image.load('pipe-red.png').convert()
    pipe_list = []
    pipe_height= [300,400,450]
    # base surface 
    base_surface = pygame.image.load('base.png').convert()
    base_surface = pygame.transform.scale2x(base_surface).convert()
    start_x = 0

    #background
    bg_surface = pygame.image.load('background-day.png').convert()
    bg_surface =  pygame.transform.scale2x(bg_surface).convert()
    # bird image
    bird_surface = pygame.image.load("blue-bird.png").convert_alpha()
    bird_rect = bird_surface.get_rect(center = (80, 100))
    birdmovement = 0
    gravity = 0.25
    #game oversurface
    gameoversurface = pygame.image.load('gameover.jpg').convert_alpha()
   

    #clock
    clock = pygame.time.Clock()
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE , 1200)

    SPAWNCLOUD = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWNCLOUD,2000)
    #score 
    font = pygame.font.SysFont("camicsonsms" ,40)
    font2 = pygame.font.Font("freesansbold.ttf",16)
    font3 = pygame.font.Font("freesansbold.ttf",25)
    score_2 = 101
    #score
    score = 0
    highscore =0
    live_font =pygame.font.Font("freesansbold.ttf",25)
    live = 3
    # adding sound
    flap_sound = pygame.mixer.Sound('wing.wav')
    hit_sound = pygame.mixer.Sound('hit.wav')
    point_sound = pygame.mixer.Sound('point.wav')
    #cloud image
    cloud_surface = pygame.image.load('image.png').convert_alpha()
    cloud_surface  = pygame.transform.scale2x(cloud_surface )
    cloudlist= []
    cloudpos = [100,150, 200]

    while True:
        screen.blit(bg_surface,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == SPAWNCLOUD:
                cloudlist.append(create_cloud())
                
            if event.type == SPAWNPIPE:
                pipe_list.extend(createPipe())
                
                if gameActive :
                    
                    point_sound.play()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and gameActive:
                    flap_sound.play()
                    birdmovement = 0
                    birdmovement -= 8
                     
                    
                if event.key == pygame.K_SPACE and gameActive == False:
                    birdmovement = 0
                    if lives == 0:
                        score = 0
                        
                    if lives ==3 or score >= 1 or score <100:
                        score_2 = 101
                        score = 0
                    if lives == 2 or score >= 1 or score < 100:
                        score_2 = 101
                        score = 0
                    if lives == 1 or  score >= 1 or score < 100:
                        score_2 = 101
                        score = 0
                    gameActive = True
                    bird_rect.center = (80, 100)
                    pipe_list.clear()
                    cloudlist.clear()
                if event.key == pygame.K_SPACE and live == 0:
                    menu.mainloop(surface)
                    
                        
                     
                if event.key == pygame.K_c:
                    
                    menu.mainloop(surface)
                    
        if gameActive:
            rotated_bird = rotate_bird(bird_surface)
            screen.blit(rotated_bird, bird_rect)
            cloudlist = movecloud(cloudlist)
            drawcloud(cloudlist)
            birdmovement += gravity
            bird_rect.centery += birdmovement
            gameActive = checkCollision(pipe_list)
             
            pipe_list = movepipe(pipe_list)
            drawpipe(pipe_list)
            draw_score("maingame")
            lives()
            score+= 0.08 
            target()
            
            score_2 -= 0.01
            if score_2 <= 0:
                score_2 = 0
            if gameActive == False:
                live -= 1
            
                
            
             
                
        if gameActive:
            gameActive = checkCollision2(cloudlist)
            
            
        else:
            draw_score("gameover") 
            draw_score("maingame")  
            highscore=  update_score(score , highscore)
            if live == 0:
                gameover()
                draw_score("return")
                lose()
            if score >=100:
                won()
        start_x -= 4.5
        base()
        if start_x <= - 576:
            start_x=0
        if score >=100 and score <= 100 :
             won()
             draw_score("return")
        
        clock.tick(120)
        pygame.display.update()
    
    
menu = pygame_menu.Menu(660, 574, 'Welcome',
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add_text_input('Name :', default='mehruddin')
menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_button('Level1' ,level1)
menu.add_button('Level2' ,level2)
menu.add_button('Final', Final)

menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)



