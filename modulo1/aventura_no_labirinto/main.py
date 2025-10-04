#!/usr/bin/env python3
"""Script principal para executar o jogo Aventura no Labirinto.

Este módulo implementa a interface de linha de comando (CLI) para o jogo
Aventura no Labirinto, permitindo configurar opções como nome do jogador,
cor do tema, dificuldade e controle de som.
"""

import argparse
import time
from rich.console import Console
from aventura_pkg import (
    criar_labirinto, imprimir_labirinto, iniciar_jogador, mover, 
    resolver_labirinto, imprime_instrucoes, animacao_vitoria,
    imprimir_menu, configurar_som
)

console = Console()

def criar_parser():
    """Cria e configura o parser de argumentos da CLI.
    
    Returns:
        argparse.ArgumentParser: Parser configurado com todas as opções.
    """
    parser = argparse.ArgumentParser(
        description="Jogo Aventura no Labirinto - Explore, colete itens e encontre a saída!",
        epilog="Exemplo: python main.py --name João --color green --dificuldade 2"
    )
    
    parser.add_argument(
        "--name", 
        required=True,
        help="Nome do jogador (obrigatório)"
    )
    
    parser.add_argument(
        "--color", 
        default="cyan", 
        choices=["cyan", "yellow", "green", "red", "blue", "magenta"],
        help="Cor principal do jogo (padrão: cyan)"
    )
    
    parser.add_argument(
        "--dificuldade", 
        type=int, 
        choices=[1, 2, 3], 
        default=1,
        help="Dificuldade: 1 (fácil), 2 (médio), 3 (difícil) - padrão: 1"
    )
    
    parser.add_argument(
        "--disable-sound", 
        action="store_true",
        help="Desabilita os efeitos sonoros do jogo"
    )
    
    parser.add_argument(
        "--auto-solve", 
        action="store_true",
        help="Adiciona opção para resolver o labirinto automaticamente"
    )
    
    return parser

def jogar(labirinto, nome, cor):
    """Executa o loop principal do jogo.
    
    Args:
        labirinto (list): Matriz do labirinto.
        nome (str): Nome do jogador.
        cor (str): Cor do tema.
        
    Returns:
        bool: True se o jogador venceu, False se saiu do jogo.
    """
    pos, pontuacao = iniciar_jogador(labirinto)
    
    while True:
        imprimir_labirinto(labirinto, pos)
        console.print(f"\n[{cor}]Pontuação: {pontuacao} pontos[/]")
        console.print(f"[dim]Use as setas para mover, ESC para voltar ao menu[/]")
        
        # Verifica se chegou na saída antes de mover
        if labirinto[pos[0]][pos[1]] == "S":
            animacao_vitoria(nome)
            input("\nPressione Enter para continuar...")
            return True
        
        # Move o jogador
        nova_pos, nova_pontuacao, sair = mover(labirinto, pos, pontuacao)
        
        if sair:
            return False
            
        pos = nova_pos
        pontuacao = nova_pontuacao

def resolver_automaticamente(labirinto, nome, cor):
    """Resolve o labirinto automaticamente mostrando o caminho.
    
    Args:
        labirinto (list): Matriz do labirinto.
        nome (str): Nome do jogador.
        cor (str): Cor do tema.
    """
    console.print(f"\n[{cor}]Resolvendo labirinto automaticamente...[/]")
    pos_inicial, _ = iniciar_jogador(labirinto)
    caminho = resolver_labirinto(labirinto, pos_inicial)
    
    if caminho:
        console.print(f"[green]Solução encontrada! Mostrando caminho...[/]")
        time.sleep(2)
        
        for i, passo in enumerate(caminho):
            imprimir_labirinto(labirinto, passo)
            console.print(f"\n[{cor}]Passo {i+1}/{len(caminho)}[/]")
            console.print(f"[dim]Posição: {passo}[/]")
            time.sleep(0.8)
            
        console.print(f"\n[bold green]Labirinto resolvido em {len(caminho)} passos![/]")
    else:
        console.print("[bold red]Não foi possível encontrar uma solução![/]")
    
    input("\nPressione Enter para continuar...")

def main():
    """Função principal do programa."""
    parser = criar_parser()
    args = parser.parse_args()
    
    # Configura o som
    configurar_som(not args.disable_sound)
    
    # Mensagem de boas-vindas
    console.print(f"\n[bold {args.color}]🎮 Aventura no Labirinto 🎮[/]")
    console.print(f"[italic]Preparando aventura para {args.name}...[/]")
    time.sleep(1)
    
    # Loop principal do menu
    while True:
        imprimir_menu(args.name, args.color)
        
        try:
            opcao = console.input("\n[bold]Escolha uma opção (1-4): [/]")
        except KeyboardInterrupt:
            console.print(f"\n[{args.color}]Até logo, {args.name}![/]")
            break
        
        match opcao.strip():
            case "1":
                # Jogar
                labirinto = criar_labirinto(args.dificuldade)
                venceu = jogar(labirinto, args.name, args.color)
                if not venceu:
                    console.print(f"[yellow]Voltando ao menu principal...[/]")
                    time.sleep(1)
                    
            case "2":
                # Instruções
                console.clear()
                imprime_instrucoes()
                input("\n[dim]Pressione Enter para voltar ao menu...[/]")
                
            case "3":
                # Resolver automaticamente
                if args.auto_solve:
                    labirinto = criar_labirinto(args.dificuldade)
                    resolver_automaticamente(labirinto, args.name, args.color)
                else:
                    console.print("[red]Opção não disponível. Use --auto-solve para habilitar.[/]")
                    time.sleep(2)
                    
            case "4":
                # Sair
                console.print(f"\n[bold {args.color}]Obrigado por jogar, {args.name}![/]")
                console.print("[italic]Até a próxima aventura! 🚀[/]")
                break
                
            case _:
                console.print("[red]Opção inválida! Escolha entre 1 e 4.[/]")
                time.sleep(1.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Jogo interrompido pelo usuário. Até logo![/]")
    except Exception as e:
        console.print(f"\n[red]Erro inesperado: {e}[/]")
        console.print("[dim]Por favor, reporte este erro.[/]")