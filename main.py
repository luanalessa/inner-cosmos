import pygame
import cv2
from gestures.hand_tracker import HandTracker
from utils.mouse import VirtualMouse
from ui.periodic_table import draw_periodic_table

# Inicialização do pygame
pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Inner Cosmos — Plano B")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# Inicializa câmera, rastreador de mãos e mouse virtual
cap = cv2.VideoCapture(0)
hand_tracker = HandTracker()
mouse = VirtualMouse(screen_width, screen_height)

running = True
while running:

    screen.fill((10, 10, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Processa o frame para detectar mãos
    hand_data = hand_tracker.get_hand_positions(frame)
    print("hand_data:", hand_data)

    # Atualiza posição do mouse virtual baseado na mão direita
    mouse.update_position(hand_data)

    # Desenha tabela periódica e obtém retângulos clicáveis
    elements = draw_periodic_table(screen, font)

    # Detecta clique por gesto de pinça da mão direita
    if hand_tracker.is_right_hand_pinch():
        for element in elements:
            if element["rect"].collidepoint(mouse.x, mouse.y):
                print(f"✨ Átomo selecionado: {element['atom']['name']}")

    # Desenha o mouse virtual
    mouse.draw(screen)

    # Atualiza tela
    pygame.display.flip()
    clock.tick(60)

# Libera recursos
cap.release()
pygame.quit()
