import pygame

# Crie um programa no python que reproduza um arquivo de audio MP3.

pygame.init()
pygame.mixer.music.load('lpbo.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
