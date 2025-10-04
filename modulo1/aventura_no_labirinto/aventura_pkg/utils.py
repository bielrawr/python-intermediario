"""Módulo com funções utilitárias para o jogo."""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import time
import threading
try:
    from playsound import playsound
    SOM_DISPONIVEL = True
except ImportError:
    SOM_DISPONIVEL = False

console = Console()
som_habilitado = True

def configurar_som(habilitado):
    """Configura se o som está habilitado ou não.
    
    Args:
        habilitado (bool): True para habilitar som, False para desabilitar.
    """
    global som_habilitado
    som_habilitado = habilitado

def tocar_som(arquivo, assincrono=True):
    """Toca um arquivo de som se o som estiver habilitado.
    
    Args:
        arquivo (str): Caminho para o arquivo de som.
        assincrono (bool): Se True, toca o som em thread separada.
    """
    if not som_habilitado or not SOM_DISPONIVEL:
        return
    
    def _tocar():
        try:
            playsound(arquivo)
        except:
            pass  # Ignora erros de som
    
    if assincrono:
        threading.Thread(target=_tocar, daemon=True).start()
    else:
        _tocar()

def som_coleta():
    """Toca som de coleta de item (simulação com print se não houver arquivo)."""
    if som_habilitado:
        console.print("[yellow]♪ Ding! ♪[/]", end="")

def som_vitoria():
    """Toca som de vitória (simulação com print se não houver arquivo)."""
    if som_habilitado:
        console.print("[green]♫ Vitória! ♫[/]")

def imprime_instrucoes():
    """Imprime as instruções do jogo formatadas."""
    instrucoes = Text()
    instrucoes.append("Como Jogar:\n\n", style="bold cyan")
    instrucoes.append("• Use as setas do teclado para mover o jogador ", style="white")
    instrucoes.append("(J)", style="bold green")
    instrucoes.append("\n• Coletar itens ", style="white")
    instrucoes.append("(*)", style="bold yellow")
    instrucoes.append(" dá 10 pontos cada\n", style="white")
    instrucoes.append("• Chegue à saída ", style="white")
    instrucoes.append("(S)", style="bold red")
    instrucoes.append(" para vencer!\n", style="white")
    instrucoes.append("• Pressione ", style="white")
    instrucoes.append("ESC", style="bold red")
    instrucoes.append(" para voltar ao menu\n\n", style="white")
    instrucoes.append("Legenda:\n", style="bold cyan")
    instrucoes.append("• ", style="white")
    instrucoes.append("#", style="grey")
    instrucoes.append(" = Parede\n", style="white")
    instrucoes.append("• ", style="white")
    instrucoes.append("*", style="bold yellow")
    instrucoes.append(" = Item (10 pontos)\n", style="white")
    instrucoes.append("• ", style="white")
    instrucoes.append("S", style="bold red")
    instrucoes.append(" = Saída\n", style="white")
    instrucoes.append("• ", style="white")
    instrucoes.append("J", style="bold green")
    instrucoes.append(" = Jogador (você!)", style="white")
    
    panel = Panel(instrucoes, title="[bold]Instruções do Jogo[/]", border_style="cyan")
    console.print(panel)

def imprimir_menu(nome, cor="cyan"):
    """Imprime o menu principal formatado.
    
    Args:
        nome (str): Nome do jogador.
        cor (str): Cor do tema.
    """
    console.clear()
    titulo = Text(f"Aventura no Labirinto", style=f"bold {cor}")
    subtitulo = Text(f"Bem-vindo, {nome}!", style="italic")
    
    menu_text = Text()
    menu_text.append("1", style="bold cyan")
    menu_text.append(" - Jogar\n", style="white")
    menu_text.append("2", style="bold cyan")
    menu_text.append(" - Instruções\n", style="white")
    menu_text.append("3", style="bold cyan")
    menu_text.append(" - Resolver Automaticamente\n", style="white")
    menu_text.append("4", style="bold cyan")
    menu_text.append(" - Sair", style="white")
    
    panel = Panel(menu_text, title=titulo, subtitle=subtitulo, border_style=cor)
    console.print(panel)

def animacao_vitoria(nome):
    """Animação recursiva para celebrar a vitória.

    Args:
        nome (str): Nome do jogador.
    """
    som_vitoria()
    
    def animar(contador=3):
        if contador == 0:
            console.clear()
            vitoria_text = Text()
            vitoria_text.append("🎉 PARABÉNS! 🎉\n\n", style="bold green blink")
            vitoria_text.append(f"{nome}, você venceu!\n\n", style="bold yellow")
            vitoria_text.append("🏆 Você é um verdadeiro aventureiro! 🏆", style="bold cyan")
            
            panel = Panel(vitoria_text, title="[bold green]VITÓRIA![/]", border_style="green")
            console.print(panel)
            return
        
        console.clear()
        console.print(f"[yellow blink]Celebrando vitória em: {contador}[/]", style="bold")
        time.sleep(1)
        animar(contador - 1)
    
    animar()