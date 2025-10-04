"""Módulo para controle do jogador e movimentação."""

from pynput import keyboard
from rich.console import Console
from .utils import som_coleta

console = Console()
ouvinte = None

def iniciar_jogador(labirinto):
    """Inicia o jogador na posição inicial do labirinto.

    Args:
        labirinto (list): Matriz do labirinto.

    Returns:
        tuple: Posição inicial (linha, coluna) e pontuação inicial.
    """
    return (1, 1), 0  

def mover(labirinto, pos_atual, pontuacao):
    """Move o jogador com base na tecla pressionada.

    Args:
        labirinto (list): Matriz do labirinto.
        pos_atual (tuple): Posição atual (linha, coluna).
        pontuacao (int): Pontuação atual.

    Returns:
        tuple: Nova posição, pontuação atualizada e flag de saída (pos, pontos, sair).
    """
    global ouvinte
    nova_pos = pos_atual
    nova_pontuacao = pontuacao
    moved = False
    sair = False

    def on_press(key):
        nonlocal nova_pos, nova_pontuacao, moved, sair
        try:
            if key == keyboard.Key.up:
                nova_pos = (nova_pos[0] - 1, nova_pos[1])
                moved = True
            elif key == keyboard.Key.down:
                nova_pos = (nova_pos[0] + 1, nova_pos[1])
                moved = True
            elif key == keyboard.Key.left:
                nova_pos = (nova_pos[0], nova_pos[1] - 1)
                moved = True
            elif key == keyboard.Key.right:
                nova_pos = (nova_pos[0], nova_pos[1] + 1)
                moved = True
            elif key == keyboard.Key.esc:
                sair = True
                moved = True
                return False
        except AttributeError:
            pass

        if moved and not sair:
            # Verifica se a nova posição é válida
            if (0 <= nova_pos[0] < len(labirinto) and
                0 <= nova_pos[1] < len(labirinto[0]) and
                labirinto[nova_pos[0]][nova_pos[1]] != "#"):
                # Verifica se coletou um item
                if labirinto[nova_pos[0]][nova_pos[1]] == "*":
                    nova_pontuacao += 10
                    labirinto[nova_pos[0]][nova_pos[1]] = " "  # Remove o item
                    som_coleta()  # Toca som de coleta
            else:
                # Posição inválida, volta para a posição anterior
                nova_pos = pos_atual
            
        if moved:
            ouvinte.stop()

    ouvinte = keyboard.Listener(on_press=on_press)
    ouvinte.start()
    ouvinte.join()
    return nova_pos, nova_pontuacao, sair

def resolver_labirinto(labirinto, pos_atual, caminho=None):
    """Função recursiva que encontra o caminho até a saída.

    Args:
        labirinto (list): Matriz do labirinto.
        pos_atual (tuple): Posição atual (linha, coluna).
        caminho (list, optional): Lista de posições visitadas.

    Returns:
        list: Lista de posições até a saída ou None se não houver caminho.
    """
    if caminho is None:
        caminho = [pos_atual]

    lin, col = pos_atual
    if labirinto[lin][col] == "S":
        return caminho

    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    for mov in movimentos:
        nova_pos = (lin + mov[0], col + mov[1])
        if (0 <= nova_pos[0] < len(labirinto) and 
            0 <= nova_pos[1] < len(labirinto[0]) and 
            labirinto[nova_pos[0]][nova_pos[1]] != "#" and 
            nova_pos not in caminho):
            resultado = resolver_labirinto(labirinto, nova_pos, caminho + [nova_pos])
            if resultado:
                return resultado
    return None