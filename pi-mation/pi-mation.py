#!/usr/bin/env python

# Pi-Mation v0.5
# Stop motion animation for the Raspberry Pi and camera module
# Russell Barnes - 12 Nov 2013 for Linux User magazine issue 134 
# www.linuxuser.co.uk

import pygame, os, sys
import picamera
import time
from data import pyganim

#define global variables
pics_taken = 0
pics_list = []
current_alpha, next_alpha = 255, 128

# Initialise Pygame, start screen and camera
pygame.init()
res = pygame.display.list_modes() # return the best resolution for your monitor
width, height = res[0] # Having trouble getting the right resolution? Manually set with: 'width, height = 1650, 1050' (where the numbers match your monitor)
print "Reported resolution is:", width, "x", height
if width == 1600:
    print "You appear to be trying to run Pi-Mation from the command prompt. Please try runnnig from the desktop (with 'startx') instead.\nQuitting..."
    sys.exit(0)
else:
    start_pic = pygame.image.load(os.path.join('data', 'start_screen.jpg'))
    start_pic_fix = pygame.transform.scale(start_pic, (width, height))
    screen = pygame.display.set_mode([width, height])
    pygame.display.toggle_fullscreen()
    play_clock = pygame.time.Clock()
    camera = picamera.PiCamera()
    camera.resolution = (width, height)

def take_pic():
    """Grabs an image and load it for the alpha preview and 
    appends the name to the animation preview list"""
    global pics_taken, pre_pic, pics_list
    pics_taken += 1
    camera.capture(os.path.join('pics', 'image_' + str(pics_taken) + '.jpg'), use_video_port = True)
    pre_pic = pygame.image.load(os.path.join('pics', 'image_' + str(pics_taken) + '.jpg'))
    pics_list.append((os.path.join('pics', 'image_' + str(pics_taken) + '.jpg'), 0.3))

def delete_pic():
    """Doesn't actually delete the last picture, but the preview will 
    update and it will be successfully overwritten the next time you take a shot"""
    global pics_taken, pre_pic, pics_list
    if pics_taken > 0:
        pics_taken -= 1
        del pics_list[-1]
    if pics_taken >= 1:
        pre_pic = pygame.image.load(os.path.join('pics', 'image_' + str(pics_taken) + '.jpg'))

def animate():
    """Do a quick live preview animation of 
    all current pictures taken using pyganim"""
    anim_obj = pyganim.PygAnimation(pics_list, loop=False)
    screen.fill((0,0,0))
    camera.stop_preview()
    anim_obj.play()
    for pics in pics_list:
        anim_obj.blit(screen, (0, 0))
        play_clock.tick(3.3)
        pygame.display.flip()
    camera.start_preview()
    
def make_movie():
    """Quit out of the application 
    and create a movie with your pics"""
    camera.stop_preview()
    pygame.quit()
    print "\nQuitting Pi-Mation to transcode your video.\nWarning: this will take a long time!"
    print "We recommend a frame rate between 5 (beginner) and 24 (expert)."
    print "\nOnce complete, write 'omxplayer video.mp4' in the terminal to play your video.\n"
    fps = raw_input("How many frames per second do you want your video to be?\n--> ")
    os.system("avconv -r " + str(fps) + " -i " + str((os.path.join('pics', 'image_%d.jpg'))) + " -vcodec libx264 video.mp4")

def change_alpha():
    """Toggle's camera preview optimacy between half and full."""
    global current_alpha, next_alpha
    camera.stop_preview()
    camera.preview_alpha = next_alpha
    camera.start_preview()
    current_alpha, next_alpha = next_alpha, current_alpha

def update_display():
    """Blit the screen (behind the camera preview) with the last picture taken"""
    screen.fill((0,0,0))
    if pics_taken > 0:
        screen.blit(pre_pic, (0, 0))
    pygame.display.flip()

def quit_app():
    """Cleanly closes the camera and the application"""
    camera.close()
    pygame.quit()
    print "Don't forget to backup your pictures or they'll be overwritten next time!"
    sys.exit(0)

def intro_screen():
    """Application starts on the help screen. User can exit 
    or start Pi-Mation proper from here"""
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_app()
                elif event.key == pygame.K_F1:
                    intro = False
                    camera.start_preview()
        screen.blit(start_pic_fix, (0, 0))
        pygame.display.update()

def main():
    """Begins on the help screen before the main application loop starts"""
    intro_screen()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_app()
                elif event.key == pygame.K_SPACE:
                    take_pic()
                elif event.key == pygame.K_BACKSPACE:
                    delete_pic()
                elif event.key == pygame.K_RETURN:
                    make_movie()
                elif event.key == pygame.K_TAB:
                    change_alpha()
                elif event.key == pygame.K_F1:
                    camera.stop_preview()
                    intro_screen()
                elif event.key == pygame.K_p:
                    if pics_taken > 1:
                        animate()
        update_display()

if __name__ == '__main__':
    main()
