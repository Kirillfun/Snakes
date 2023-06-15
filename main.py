import pygame
import random

pygame.init()
White = (255, 255, 255)
Black = (0, 0, 0)
RED = (255, 0, 0)
width = 640
height = 480
display = pygame.display.set_mode((width, height))
class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def set_text(self, text, fsize=12, text_color=White):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(display, self.fill_color, self.rect)
        display.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
pygame.display.update()
pygame.display.set_caption("Змейка_Game")
f = TextArea(0, 0, 0, 0, Black)
f.set_text('0', 50)
f.draw(320, 10)
colors = {
    "snake_head": (0, 255, 0),
    "snake_tail": (0, 200, 0),
    "apple": (255, 0, 0)
}

snake_pos = {
    "x": width / 2 - 0,
    "y": height / 2 - 10,
    "x_change": 0,
    "y_change": 0
}

snake_size = (10, 10)

snake_speed = 10

snake_tails = []

snake_pos["x_change"] = -snake_speed
for i in range(5):
    snake_tails.append([snake_pos["x"] + 10 * i, snake_pos["y"]])


food_pos = {
    "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10 - 20,
    "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10 - 20,
}

food_size = (10, 10)
food_eaten = 0

game_end = False
clock = pygame.time.Clock()
ppp = round(pygame.time.get_ticks() / 1000)
p = TextArea(0, 0, 0, 0, Black)



while not game_end:
    ppp = round(pygame.time.get_ticks() / 1000)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_end = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_pos["x_change"] == 0:

                snake_pos["x_change"] = -snake_speed
                snake_pos["y_change"] = 0

            elif event.key == pygame.K_RIGHT and snake_pos["x_change"] == 0:

                snake_pos["x_change"] = snake_speed
                snake_pos["y_change"] = 0

            elif event.key == pygame.K_UP and snake_pos["y_change"] == 0:

                snake_pos["x_change"] = 0
                snake_pos["y_change"] = -snake_speed

            elif event.key == pygame.K_DOWN and snake_pos["y_change"] == 0:

                snake_pos["x_change"] = 0
                snake_pos["y_change"] = snake_speed


    display.fill((0, 0, 0))


    ltx = snake_pos["x"]
    lty = snake_pos["y"]

    for i, v in enumerate(snake_tails):
        _ltx = snake_tails[i][0]
        _lty = snake_tails[i][1]

        snake_tails[i][0] = ltx
        snake_tails[i][1] = lty

        ltx = _ltx
        lty = _lty


    for t in snake_tails:
        pygame.draw.rect(display, colors["snake_tail"], [
            t[0],
            t[1],
            snake_size[0],
            snake_size[1]])


    snake_pos["x"] += snake_pos["x_change"]
    snake_pos["y"] += snake_pos["y_change"]


    if (snake_pos["x"] < -snake_size[0]):
        quit()

    elif (snake_pos["x"] > width):
        quit()

    elif (snake_pos["y"] < -snake_size[1]):
        snake_pos["y"] = height

    elif (snake_pos["y"] > height):
        snake_pos["y"] = 0

    pygame.draw.rect(display, colors["snake_head"], [
        snake_pos["x"],
        snake_pos["y"],
        snake_size[0],
        snake_size[1]])
    f.set_text('Съедено '+str(food_eaten), 50)
    f.draw(150, 10)
    p.set_text('Время '+str(ppp), 50)
    p.draw(400, 10)

    pygame.draw.rect(display, colors["apple"], [
        food_pos["x"],
        food_pos["y"],
        food_size[0],
        food_size[1]])


    if (snake_pos["x"] == food_pos["x"]
            and snake_pos["y"] == food_pos["y"]):
        food_eaten += 1
        snake_tails.append([food_pos["x"], food_pos["y"]])

        food_pos = {
            "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
            "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
        }

    for i, v in enumerate(snake_tails):
        if (snake_pos["x"] + snake_pos["x_change"] == snake_tails[i][0]
                and snake_pos["y"] + snake_pos["y_change"] == snake_tails[i][1]):
            quit()
    pygame.display.update()
    clock.tick(15)
    f.set_text('Длина '+str(food_eaten), 50)
    f.draw(320, 10)

pygame.quit()
quit()
