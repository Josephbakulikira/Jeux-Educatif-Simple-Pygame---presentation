import math
from constants import *

def RenderText(screen, message, font, text_color=WHITE, x=WIDTH//2, y=HEIGHT//2):
    img = font.render(message, True, text_color)
    rect = img.get_rect()
    rect.center = (x, y)
    screen.blit(img, rect)

def GetDistance(x1, y1, x2, y2):
    return math.sqrt( (x2 - x1) * (x2-x1) + (y2 - y1) * (y2 - y1) )
