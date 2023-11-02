class Colisao():
    def __init__(self):
        super().__init__()
    
    def zerarVel(numero, player, rect, tolerancia):
        print(f'Colisão detectada no retangulo {numero}')
        if abs(player.top - rect.bottom) < tolerancia:
            return "up"
        elif abs(player.bottom - rect.top) < tolerancia:
            return "down"
        elif abs(player.left - rect.right) < tolerancia:
            return "left"
        elif abs(player.right - rect.left) < tolerancia:
            return "right"
        else:
            print("Erro ao zerar velocidade do personagem!")
