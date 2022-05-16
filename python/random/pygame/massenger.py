import pygame

pygame.init()
window_obj = pygame.display.set_mode((800, 500))
pygame.display.set_caption("messenger")
icon = pygame.image.load("messenger.png")
pygame.display.set_icon(icon)
user_img = pygame.image.load("messenger.png")
img_x = 0
img_y = 0
change_img_x = 0

def player(x, y):
    window_obj.blit(user_img, (x, y))


running = True
while running:

    window_obj.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("right pressed")
            if event.key == pygame.K_LEFT:
                print("left pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                change_img_x = 0.1
            if event.key == pygame.K_LEFT:
                change_img_x = 0
    img_x += change_img_x
    player(img_x, img_y)
    pygame.display.update()
