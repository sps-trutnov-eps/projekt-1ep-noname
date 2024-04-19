import pygame


class Games:
    def __init__(self, jmeno_hry, popis_hry, cislo_hry, nazev_slozky):
        self.name = jmeno_hry
        self.description = popis_hry
        self.id = cislo_hry
        self.location = nazev_slozky

    def drawing(self, x, y, window):
        velky_font = pygame.font.Font(None, 45)
        maly_font = pygame.font.Font(None, 35)
        titul_hry = velky_font.render(self.name, True, (255, 255, 255))
        popis_hry = maly_font.render(self.description, True, (255, 255, 255))
        window.blit(titul_hry, (x, y))
        window.blit(popis_hry, (x + 50, y))


def get_games(x, y):
    pokerun = Games("Pokérun", "Pokérun je hra, ve které je hlavní cíl získat co nejvíce bodů.", 1, "Pokerun")

    games = [pokerun]

    return games
