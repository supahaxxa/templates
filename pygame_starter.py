import pygame

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 720, 480
FRAMERATE = 60
GRAY = "#7f7f7f"

screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Pygame Starter")

running = True
while running:
	clock.tick(FRAMERATE)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	screen.fill(GRAY)

	pygame.display.update()
