import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 205, 0)

width = 800
height = 600

speed = 5

tile_width = 20
tile_height = 150

ball_size = 25

lead_x = 20
lead_y = 200

lead_x2 = 760
lead_y2 = 200

lead_x_ball = width/2-ball_size/2
lead_y_ball = height/2-ball_size

lead_y_change = 0
lead_y2_change = 0

clock = pygame.time.Clock()

pygame.display.set_caption("Pong.exe")
gameDisplay = pygame.display.set_mode((width, height))

mediumfont = pygame.font.SysFont("Agency FB", 60)


def tile(lead_x, lead_y, tile_width, tile_height):
    pygame.draw.rect(gameDisplay, white, [lead_x, lead_y, tile_width, tile_height])

def tile2(lead_x2, lead_y2, tile_width, tile_height):
    pygame.draw.rect(gameDisplay, white, [lead_x2, lead_y2, tile_width, tile_height])

def ball(lead_x_ball, lead_y_ball, ball_size):
    pygame.draw.rect(gameDisplay, white, [lead_x_ball, lead_y_ball, ball_size, ball_size])

def message_to_corner(msg, color):
    screen_text = mediumfont.render(msg, True, color)
    gameDisplay.blit(screen_text, [width/2-200, 1])

def message_to_corner2(msg, color):
    screen_text = mediumfont.render(msg, True, color)
    gameDisplay.blit(screen_text, [width/2+175, 1])

def text_objects(msg, color):
    textsurface = mediumfont.render(msg, True, color)
    return textsurface, textsurface.get_rect()

def message_to_center(msg, color, y_displace=0, size="medium"):
    textsurf, textrect = text_objects(msg, color)
    textrect.center = (width / 2), (height / 2) + y_displace
    gameDisplay.blit(textsurf, textrect)

def intro():
    intro = True
    while intro is True:
        gameDisplay.fill(white)
        message_to_center("Welcome to my pong game", black, -100)
        message_to_center("Press ENTER to play or ESCAPE to quit", black)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_RETURN:
                    intro = False

def gameLoop():

    gameDone = False

    lead_y = 200
    lead_y2 = 200

    end_y = lead_y + tile_height
    end_y2 = lead_y2 + tile_height

    lead_y_change = 0
    lead_y2_change = 0

    lead_x_ball = width / 2 - ball_size / 2
    lead_x_ball_change = 0

    lead_y_ball = height / 2 - ball_size
    lead_y_ball_change = 0

    ball_starting_side = ("left", "right")

    direction = random.choice(ball_starting_side)

    score = 0
    score2 = 0

    fps = 144

    i = 1

    while gameDone is not True:
        gameDisplay.fill(black)
        tile(lead_x, lead_y, tile_width, tile_height)
        tile2(lead_x2, lead_y2, tile_width, tile_height)
        ball(lead_x_ball, lead_y_ball, ball_size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    gameDone = True

                if event.key == pygame.K_w:
                    lead_y_change = -speed
                if event.key == pygame.K_s:
                    lead_y_change = speed

                if event.key == pygame.K_UP:
                    lead_y2_change = -speed
                if event.key == pygame.K_DOWN:
                    lead_y2_change = speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    lead_y_change = 0
                if event.key == pygame.K_s:
                    lead_y_change = 0

                if event.key == pygame.K_UP:
                    lead_y2_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y2_change = 0


        lead_y += lead_y_change
        lead_y2 += lead_y2_change

        end_y = lead_y + tile_height
        end_y2 = lead_y2 + tile_height

        if end_y >= height:
            lead_y_change = 0

        if end_y2 >= height:
            lead_y2_change = 0

        if lead_y <= 0:
            lead_y_change = 0

        if lead_y2 <= 0:
            lead_y2_change = 0

        if direction is "left":
            lead_x_ball_change = -speed
        else:
            lead_x_ball_change = speed



        if lead_x_ball <= lead_x:
            if lead_y <= lead_y_ball <= end_y:
                direction = "right"
                lead_y_ball_change = lead_y_change-(i/2)
                i += 1

        if lead_x_ball+(ball_size-4) >= lead_x2:
            if end_y2 >= lead_y_ball >= lead_y2:
                direction = "left"
                lead_y_ball_change = lead_y2_change+(i/2)
                i += 1

        lead_x_ball += (lead_x_ball_change)
        lead_y_ball += (lead_y_ball_change)


        if (lead_x_ball <= 0):
            score2 += 1
            lead_x_ball = width / 2 - ball_size / 2
            lead_y_ball = height / 2 - ball_size
            lead_y_ball_change = 0
            lead_y = 200
            lead_y2 = 200
            i = 1

        if (lead_x_ball >= width):
            score += 1
            lead_x_ball = width / 2 - ball_size / 2
            lead_y_ball = height / 2 - ball_size
            lead_y_ball_change = 0
            lead_y = 200
            lead_y2 = 200
            i = 1


        if (lead_y_ball <= 0):
            lead_y_ball_change = -lead_y_ball_change
        if (lead_y_ball >= height):
            lead_y_ball_change = -lead_y_ball_change


        message_to_corner(str(score), white)
        message_to_corner2(str(score2), white)

        if score >= 10:
            message_to_center("PLAYER1 WON!!!", white)
            pygame.display.update()
            time.sleep(1)
            gameDone = True
        if score2 >= 10:
            message_to_center("PLAYER2 WON!!!", white)
            pygame.display.update()
            time.sleep(1)
            gameDone = True

        pygame.display.update()
        clock.tick(fps)

def afterGame():
    gameDisplay.fill(white)
    message_to_center("Hope you enjoyed!!!", black)
    pygame.display.update()

intro()
gameLoop()
afterGame()

time.sleep(1)

pygame.quit()
quit()