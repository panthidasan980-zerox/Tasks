import pygame
import cv2
from deepface import DeepFace

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Move with smile")

cap = cv2.VideoCapture(0)   # Camera

CHECK_EMOTION_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHECK_EMOTION_EVENT , 2000)

running = True
player = pygame.Rect(200, 100, 50, 50)
playerColor = (255, 0,0)

# game loop
while running:
    # event loop
    for event in   pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHECK_EMOTION_EVENT:
            print("Taking image")
            ret, frame =  cap.read()
            if ret == True:
                try:
                    result = DeepFace.analyze(frame, actions=["emotion"])
                    print(result)
                    dict = result[0]
                    if result[0]['dominant_emotion'] == 'happy':
                        player.x = player.x + 10
                except:
                   print("Face not detected")

    
    # draw player
    pygame.draw.rect(screen, playerColor, player)
    

    pygame.display.update()
