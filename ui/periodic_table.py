import pygame
from domain.atoms.registry import ATOM_REGISTRY

def draw_periodic_table(screen, font):
    elements = []  # Lista de elementos clicáveis com posição e dados

    for i, atom in enumerate(ATOM_REGISTRY):
        rect = pygame.Rect(30, 30 + i * 110, 140, 100)
        pygame.draw.rect(screen, atom["color"], rect)
        pygame.draw.rect(screen, (255, 255, 255), rect, 2)

        symbol = font.render(atom["symbol"], True, (255, 255, 255))
        name = font.render(atom["name"], True, (230, 230, 230))

        screen.blit(symbol, (rect.x + 10, rect.y + 10))
        screen.blit(name, (rect.x + 10, rect.y + 40))

        # Salva o retângulo e o átomo para verificação posterior
        elements.append({"rect": rect, "atom": atom})

    return elements
