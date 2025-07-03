class VirtualMouse:
    def __init__(self, screen_width=1280, screen_height=720):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.radius = 10
        self.visible = True

    def update_position(self, hand_data):
        if not hand_data:
            return

        # Verifica se há pelo menos uma mão (hand_data é uma lista de listas de pontos)
        for hand in hand_data:
            if len(hand) >= 9:  # Garante que ponto 8 (indicador) existe
                index_finger = hand[8]
                self.x = int((1 - index_finger[0]) * self.screen_width)  # espelhado
                self.y = int(index_finger[1] * self.screen_height)
                self.visible = True
                break  # Atualiza com a primeira mão encontrada


    def draw(self, screen):
        if self.visible:
            import pygame
            pygame.draw.circle(screen, (255, 100, 100), (self.x, self.y), self.radius)
