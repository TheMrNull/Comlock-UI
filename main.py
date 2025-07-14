import pygame

#Variables
pygame.init()
screen = pygame.display.set_mode((160,128))
pygame.display.set_caption("Comlock UI")
clock = pygame.time.Clock()
test_font = pygame.font.Font( "Fonts/Pixeltype.ttf",50)
#END of Variables

#Surfaces
background_surface = pygame.Surface((160,128))
background_surface.fill("Grey")
text_surface = test_font.render("Home", False, "Black")
#END of surfaces 

while True: #keeps the UI window opened
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(background_surface, (0,0))
    screen.blit(text_surface,(10,10))
    pygame.display.update()
    clock.tick(60)
    
