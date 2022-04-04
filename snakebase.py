import pygame
from sys import exit
from SnakeMovement import snake_move, key_direction, opposite_moves
from random import randrange

pygame.init()

width, height = 800, 600

dimensions = (width, height)

display = pygame.display
display.set_caption("Nibbles Reboot")
window = display.set_mode(size=dimensions)

font = pygame.font.SysFont('script', 50)


def game():
    clock = pygame.time.Clock()

    pos = [randrange(100, 200), randrange(100, 200)]
    x, y = pos
    body = [[x, y], [x - 10, y], [x - (2 * 10), y]]

    score = 0

    spawn = True

    direction = "right"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        window.fill((149, 120, 229))

        keys = pygame.key.get_pressed()

        old_direction = direction

        for k in key_direction.keys():
            if keys[k]:
                direction = key_direction.get(k)
                break

        for square in body:
            pygame.draw.rect(window, (255, 255, 0),
                             (square[0], square[1], 10, 10))

        if old_direction == opposite_moves[direction]:
            direction = old_direction

        move = snake_move[direction]
        pos[move[0]] += move[1]
        body.append(list(pos))

        for square in body[:-1]:
            if pygame.Rect(square[0], square[1], 10, 10).colliderect(pygame.Rect(pos[0], pos[1], 10, 10)):
                end(score)

        if pos[0] + 10 <= 0 or pos[0] >= width or pos[1] + 10 <= 0 or pos[1] >= height:
            end(score)

        if spawn:
            fruit = [randrange(40, width - 40), randrange(40, height - 40)]
            spawn = False

        pygame.draw.rect(window, (255, 0, 0), (fruit[0], fruit[1], 10, 10))

        if pygame.Rect(pos[0], pos[1], 10, 10).colliderect(pygame.Rect(fruit[0], fruit[1], 10, 10)):
            spawn = True
            score += 1
        else:
            body.pop(0)

        scoreboard = font.render(f'{score}', True, (255, 255, 255))
        loc = scoreboard.get_rect(center=(width // 2, height // 2))
        window.blit(scoreboard, loc)

        pygame.display.update()
        clock.tick(25)


def menu():
    main_menu_message = font.render(
        'Click to Start Nibbles Reboot', True, (255, 255, 51))
    font_pos = main_menu_message.get_rect(center=(width // 2, height // 2))
    window.blit(main_menu_message, font_pos)
    pygame.display.update()

    while True:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            game()

        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

        window.fill((223, 224, 255))


def end(score: int):
    window.fill((0, 0, 0))
    game_over_message = font.render('GAME OVER ;)', True, (255, 0, 0))
    # showing 'You score was SCORE'
    game_over_score = font.render(f'Score: {score}', True, (255, 255, 51))

    font_pos_message = game_over_message.get_rect(
        center=(width // 2, height // 2))
    font_pos_score = game_over_score.get_rect(
        center=(width // 2, height // 2 + 40))
    window.blit(game_over_message, font_pos_message)
    window.blit(game_over_score, font_pos_score)
    pygame.display.update()

    while True:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


if __name__ == '__main__':
    menu()
