import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

pygame.init()

class Game():
    def __init__(self):
        self.highscore = 0
        self.score = 0
        self.lives = 3
        self.level = 1
        
    
    def display(self):
        print("Your current score is " + str(self.score))
        print("Your high score is " + str(self.highscore))
        print("Your current amount of lives is " + str(self.lives))
        print("Your current level is " + str(self.level))


window = pygame.display.set_mode((800,800))
pygame.display.set_caption("Codable Mixup Project")
font = pygame.font.Font("freesansbold.ttf", 22)

textX = 30
textY = 30
newGame = Game()

def show_stats(x, y):
    score = font.render("Score: " + str(newGame.score), True, (255, 255, 255))
    high_score = font.render("High Score: " + str(newGame.highscore), True, (255, 255, 255))
    lives = font.render("Lives: " + str(newGame.lives), True, (255, 255, 255))
    level = font.render("Level: " + str(newGame.level), True, (255, 255, 255))
    window.blit(score, (x, y))
    window.blit(high_score, (x, y+30))
    window.blit(lives, (x, y+60))
    window.blit(level, (x, y+90))

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,32)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + "".join(current_string))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + "".join(current_string))
  return "".join(current_string)


run = True
while run:
    pygame.time.delay(100)
    window.fill((0, 0, 0))
    show_stats(textX, textY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
          inkey = get_key()
          if inkey == K_a:
            newGame.score += 1
          else:
            x = ask(window, "Input")
            print(x)

    pygame.display.update()

pygame.quit()