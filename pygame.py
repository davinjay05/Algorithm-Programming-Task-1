import pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40
obstacle_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3)
obstacle_size = 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("purple")
    
    player_rect = pygame.draw.circle(screen, "red", player_pos,player_radius)


    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and player_pos.y - player_radius > 0: 
        player_pos.y -= 200 * dt 
    if keys[pygame.K_s] and player_pos.y + player_radius < screen.get_height(): 
        player_pos.y += 200 * dt 
    if keys[pygame.K_a] and player_pos.x - player_radius > 0:
        player_pos.x -= 200 * dt 
    if keys[pygame.K_d] and player_pos.x + player_radius < screen.get_width(): 
        player_pos.x += 200 * dt

    player_rect = pygame.Rect(player_pos.x - player_radius, player_pos.y - player_radius, player_radius * 2, player_radius * 2)
    obstacle_rect = pygame.Rect(obstacle_pos.x, obstacle_pos.y, obstacle_size, obstacle_size)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()