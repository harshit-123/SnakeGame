import pygame
import random
from pygame.locals import *
import os
# initialize pygame
pygame.init()
pygame.mixer.init()


# set screeen width and height
screen_width = 900
screen_height = 600

# pygame.transform.scale(bgimage)

# set color for or screen and snake
white  = (255 , 255 , 255)
red = (255 , 0 , 0)
black = ( 0, 0 , 0)
# magenta = (44, 143 , 145)
coral = (255,127,80)

# set display
gameWindow = pygame.display.set_mode((screen_width , screen_height))

# background image
bgimage = pygame.image.load("bg1.jpg")
bgimage = pygame.transform.scale(bgimage , (screen_width , screen_height)).convert_alpha()

pygame.display.update()
pygame.display.set_caption("Snake Game by Harshit Shreshthi")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None , 40)

# show score the screen
def text_screen(text , color , x , y):
	screen_text = font.render(text , True , color) # true here for antialiasing 
	gameWindow.blit(screen_text , [x , y])


def plot_snk(gameWindow , color , snk_list , snake_size):
	for x , y in snk_list:
		pygame.draw.rect(gameWindow , color , [x , y , snake_size , snake_size])


def welcomeScreen():
	game_exit = False
	while not game_exit:
		gameWindow.fill(white)

		bgimage = pygame.image.load("download.jpg")
		bgimage = pygame.transform.scale(bgimage , (screen_width , screen_height)).convert_alpha()
		gameWindow.blit(bgimage , (0,0))

		text_screen("Welcome To Snakes World" , white , 250 , 80)
		text_screen("Press Space bar to Continue" , white ,250 , 130 )
		# pygame.mixer.music.load("welcomeMusic.mp3")
		# pygame.mixer.music.play()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pygame.mixer.music.load("backmusic.mp3")
					pygame.mixer.music.play()
					gameloop()



# Game loop

def gameloop():
# Game Specific variable
	game_exit = False
	game_over = False
	snake_x = 45
	snake_y = 65
	snake_size = 25
	fps = 60
	velocity_x = 4
	velocity_y = 4
	init_velocity = 5
	score = 0
	snk_list = []
	snk_length = 1

	food_x = random.randint(20 , screen_width/2)
	food_y = random.randint(20 , screen_height/2)

	if(not os.path.exists("HiScore.text")):
		with open ("HiScore.text" , "w") as f:
			f.write("0")

	with open("HiScore.text" , "r") as f:
		hiscore = f.read()


	while not game_exit:
		if game_over:
			with open("HiScore.text" , "w") as f:
				f.write(str(hiscore))

			gameWindow.fill(white)

			bgimg = pygame.image.load("bg.jpg")
			bgimg = pygame.transform.scale(bgimg , (screen_width , screen_height)).convert_alpha()
			gameWindow.blit(bgimg , (0,0))

			text_screen("Game Over! Press Enter To Continue" , red , 250 , 250)
			text_screen("Your Score: "+ str(score ), red , 400 , screen_height/2)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game_exit = True

				if event. type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						welcomeScreen()
		else:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game_exit = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						velocity_x = init_velocity
						velocity_y = 0

					if event.key == pygame.K_LEFT:
						velocity_x = -init_velocity
						velocity_y = 0

					if event.key == pygame.K_UP:
						velocity_y = -init_velocity
						velocity_x = 0

					if event.key == pygame.K_DOWN:
						velocity_y = init_velocity
						velocity_x = 0

			snake_x += velocity_x
			snake_y += velocity_y
			
			if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
				score += 10
				# print("Score:" , score * 10)
				food_x = random.randint(20 , screen_width / 2)
				food_y = random.randint(20 , screen_height / 2)
				snk_length += 4

				if score > int(hiscore):
					hiscore = score

			gameWindow.fill(white)

			gameWindow.blit(bgimage , (0,0))
			text_screen("Score: "+ str(score ), white , 10 , 10)
			# "  Hiscore: "+ str(hiscore) 
			text_screen("Hiscore:"+ str(hiscore), white , 730,10)

			pygame.draw.rect(gameWindow , black , [food_x , food_y , snake_size , snake_size])
			head = []
			
			if head.append(snake_x):
				pygame.mixer.music.load("Beep.mp3")
				pygame.mixer.music.play()

			if head.append(snake_y):
				pygame.mixer.music.load("Beep.mp3")
				pygame.mixer.music.play()

			# head.append(snake_x)
			# head.append(snake_y)
			snk_list.append(head)

			if len(snk_list) > snk_length:
				del snk_list[0]
			# pygame.draw.rect(gameWindow , black , [snake_x , snake_y , snake_size , snake_size])

			if head in snk_list[:-1]:
				game_over = True
				pygame.mixer.music.load("explosion.mp3")
				pygame.mixer.music.play()

			if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
				game_over = True
				pygame.mixer.music.load("explosion.mp3")
				pygame.mixer.music.play()
				print("Game Over!")

			plot_snk(gameWindow , white , snk_list ,  snake_size)
		pygame.display.update()
		clock.tick(fps)


	pygame.quit()
	quit()

welcomeScreen()
gameloop()
