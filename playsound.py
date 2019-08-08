import pygame

pygame.mixer.init()
def sayHelloToMiray():
    pygame.mixer.init()
    pygame.mixer.music.load("sound/kucukkiz.mp3")
    pygame.mixer.music.play(1000)
    return

def stopMusic():
    pygame.mixer.music.stop()
    return
