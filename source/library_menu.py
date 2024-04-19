import pygame

# barvy
RED = (255, 0, 0)
BACKGROUND_COLOR = (0, 128, 195)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# texty
font = pygame.font.Font(None, 80)
Timetable = "knihovna"
Timetable_surface = font.render(Timetable, True, WHITE)
# username přihlášeného uživatele
username_text = font.render("username", True, WHITE)

games = []


def scrolling():
    pass


def library_draw(window, rozliseni, games):
    window.fill(BACKGROUND_COLOR)

    # zobrazování her
    x = 200
    y = 200
    for game in games:
        game.drawing(x, y, window)


    pygame.draw.rect(window, BLACK, (0, 110, 1300, 2))
    # texty
    window.blit(Timetable_surface, (50, 32))
    # profilový obrázek
    pygame.draw.circle(window, BLACK, (rozliseni[0] - 55, 55), 40, 40)

    pygame.display.flip()


def library(rozliseni, window, clock):
    running = True
    clock.tick(60)

    from game_list import get_games

    while running:
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                running = False

        testing = False
        if pygame.mouse.get_pressed() and testing:
            from minihry.Pokerun.source import main
        scrolling()
        library_draw(window, rozliseni, games)
