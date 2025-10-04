#!/usr/bin/env python3
"""Versão simplificada do jogo sem dependências externas."""

import argparse
import time
import os
import sys

# Simulação simples do Rich Console
class SimpleConsole:
    def print(self, text, **kwargs):
        # Remove formatação Rich e imprime texto simples
        clean_text = text
        for tag in ['[bold]', '[/]', '[green]', '[red]', '[yellow]', '[cyan]', '[dim]']:
            clean_text = clean_text.replace(tag, '')
        print(clean_text)
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def input(self, prompt):
        clean_prompt = prompt
        for tag in ['[bold]', '[/]', '[green]', '[red]', '[yellow]', '[cyan]']:
            clean_prompt = clean_prompt.replace(tag, '')
        return input(clean_prompt)

console = SimpleConsole()

def criar_labirinto(dificuldade=1):
    """Cria um labirinto com base na dificuldade escolhida."""
    if dificuldade == 1:
        return [
            ["#", "#", "#", "#", "#"],
            ["#", " ", " ", "*", "#"],
            ["#", " ", "#", " ", "#"],
            ["#", "*", " ", " ", "S"],
            ["#", "#", "#", "#", "#"]
        ]
    elif dificuldade == 2:
        return [
            ["#", "#", "#", "#", "#", "#"],
            ["#", " ", " ", "*", " ", "#"],
            ["#", "#", " ", "#", " ", "#"],
            ["#", " ", "*", " ", "#", "#"],
            ["#", " ", " ", " ", " ", "S"],
            ["#", "#", "#", "#", "#", "#"]
        ]
    else:  # dificuldade 3
        return [
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", " ", " ", "*", " ", " ", "#"],
            ["#", "#", " ", "#", "#", " ", "#"],
            ["#", " ", "*", " ", " ", "*", "#"],
            ["#", "#", " ", "#", " ", " ", "S"],
            ["#", " ", " ", " ", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#"]
        ]

def imprimir_labirinto(labirinto, pos_jogador):
    """Imprime o labirinto no terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "+" + "-" * (len(labirinto[0]) * 2 + 1) + "+")
    
    for i in range(len(labirinto)):
        print("| ", end="")
        for j in range(len(labirinto[i])):
            if (i, j) == pos_jogador:
                print("J", end=" ")
            else:
                if labirinto[i][j] == "#":
                    print("#", end=" ")
                elif labirinto[i][j] == "*":
                    print("*", end=" ")
                elif labirinto[i][j] == "S":
                    print("S", end=" ")
                else:
                    print(".", end=" ")
        print("|")
    
    print("+" + "-" * (len(labirinto[0]) * 2 + 1) + "+\n")

def iniciar_jogador(labirinto):
    """Inicia o jogador na posição inicial."""
    return (1, 1), 0

def mover_simples(labirinto, pos_atual, pontuacao):
    """Versão simplificada de movimento com input do teclado."""
    print("Use: w(cima) s(baixo) a(esquerda) d(direita) q(sair)")
    movimento = input("Movimento: ").lower().strip()
    
    nova_pos = pos_atual
    nova_pontuacao = pontuacao
    sair = False
    
    if movimento == 'w':
        nova_pos = (pos_atual[0] - 1, pos_atual[1])
    elif movimento == 's':
        nova_pos = (pos_atual[0] + 1, pos_atual[1])
    elif movimento == 'a':
        nova_pos = (pos_atual[0], pos_atual[1] - 1)
    elif movimento == 'd':
        nova_pos = (pos_atual[0], pos_atual[1] + 1)
    elif movimento == 'q':
        sair = True
        return pos_atual, pontuacao, sair
    else:
        print("Movimento inválido!")
        time.sleep(1)
        return pos_atual, pontuacao, False
    
    # Verifica se a nova posição é válida
    if (0 <= nova_pos[0] < len(labirinto) and
        0 <= nova_pos[1] < len(labirinto[0]) and
        labirinto[nova_pos[0]][nova_pos[1]] != "#"):
        # Verifica se coletou um item
        if labirinto[nova_pos[0]][nova_pos[1]] == "*":
            nova_pontuacao += 10
            labirinto[nova_pos[0]][nova_pos[1]] = " "
            print("🎵 Item coletado! +10 pontos!")
            time.sleep(1)
    else:
        # Posição inválida, volta para a posição anterior
        nova_pos = pos_atual
        print("Movimento inválido - parede!")
        time.sleep(1)
    
    return nova_pos, nova_pontuacao, sair

def resolver_labirinto(labirinto, pos_atual, caminho=None):
    """Função recursiva que encontra o caminho até a saída."""
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

def animacao_vitoria(nome):
    """Animação recursiva para celebrar a vitória."""
    def animar(contador=3):
        if contador == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("🎉" * 20)
            print(f"    PARABÉNS, {nome.upper()}!")
            print("      VOCÊ VENCEU!")
            print("🎉" * 20)
            return
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Celebrando vitória em: {contador}")
        time.sleep(1)
        animar(contador - 1)
    
    animar()

def imprimir_menu(nome):
    """Imprime o menu principal."""
    console.clear()
    print("=" * 40)
    print("    AVENTURA NO LABIRINTO")
    print(f"    Bem-vindo, {nome}!")
    print("=" * 40)
    print("1 - Jogar")
    print("2 - Instruções")
    print("3 - Resolver Automaticamente")
    print("4 - Sair")
    print("=" * 40)

def imprime_instrucoes():
    """Imprime as instruções do jogo."""
    print("=" * 50)
    print("           INSTRUÇÕES DO JOGO")
    print("=" * 50)
    print("Como Jogar:")
    print("• Use W/A/S/D para mover o jogador (J)")
    print("• Coletar itens (*) dá 10 pontos cada")
    print("• Chegue à saída (S) para vencer!")
    print("• Digite Q para voltar ao menu")
    print()
    print("Legenda:")
    print("• # = Parede")
    print("• * = Item (10 pontos)")
    print("• S = Saída")
    print("• J = Jogador (você!)")
    print("• . = Caminho livre")
    print("=" * 50)

def jogar(labirinto, nome):
    """Executa o loop principal do jogo."""
    pos, pontuacao = iniciar_jogador(labirinto)
    
    while True:
        imprimir_labirinto(labirinto, pos)
        print(f"Pontuação: {pontuacao} pontos")
        
        # Verifica se chegou na saída
        if labirinto[pos[0]][pos[1]] == "S":
            animacao_vitoria(nome)
            input("\nPressione Enter para continuar...")
            return True
        
        # Move o jogador
        nova_pos, nova_pontuacao, sair = mover_simples(labirinto, pos, pontuacao)
        
        if sair:
            return False
            
        pos = nova_pos
        pontuacao = nova_pontuacao

def resolver_automaticamente(labirinto, nome):
    """Resolve o labirinto automaticamente."""
    print(f"\nResolvendo labirinto automaticamente...")
    pos_inicial, _ = iniciar_jogador(labirinto)
    caminho = resolver_labirinto(labirinto, pos_inicial)
    
    if caminho:
        print("Solução encontrada! Mostrando caminho...")
        time.sleep(2)
        
        for i, passo in enumerate(caminho):
            imprimir_labirinto(labirinto, passo)
            print(f"Passo {i+1}/{len(caminho)}")
            print(f"Posição: {passo}")
            time.sleep(1)
            
        print(f"\nLabirinto resolvido em {len(caminho)} passos!")
    else:
        print("Não foi possível encontrar uma solução!")
    
    input("\nPressione Enter para continuar...")

def main():
    """Função principal do programa."""
    parser = argparse.ArgumentParser(
        description="Jogo Aventura no Labirinto (Versão Simplificada)"
    )
    
    parser.add_argument(
        "--name", 
        required=True,
        help="Nome do jogador (obrigatório)"
    )
    
    parser.add_argument(
        "--dificuldade", 
        type=int, 
        choices=[1, 2, 3], 
        default=1,
        help="Dificuldade: 1 (fácil), 2 (médio), 3 (difícil)"
    )
    
    args = parser.parse_args()
    
    print(f"\n🎮 Aventura no Labirinto 🎮")
    print(f"Preparando aventura para {args.name}...")
    time.sleep(1)
    
    # Loop principal do menu
    while True:
        imprimir_menu(args.name)
        
        try:
            opcao = input("\nEscolha uma opção (1-4): ")
        except KeyboardInterrupt:
            print(f"\nAté logo, {args.name}!")
            break
        
        if opcao.strip() == "1":
            # Jogar
            labirinto = criar_labirinto(args.dificuldade)
            venceu = jogar(labirinto, args.name)
            if not venceu:
                print("Voltando ao menu principal...")
                time.sleep(1)
                
        elif opcao.strip() == "2":
            # Instruções
            os.system('cls' if os.name == 'nt' else 'clear')
            imprime_instrucoes()
            input("\nPressione Enter para voltar ao menu...")
            
        elif opcao.strip() == "3":
            # Resolver automaticamente
            labirinto = criar_labirinto(args.dificuldade)
            resolver_automaticamente(labirinto, args.name)
            
        elif opcao.strip() == "4":
            # Sair
            print(f"\nObrigado por jogar, {args.name}!")
            print("Até a próxima aventura! 🚀")
            break
            
        else:
            print("Opção inválida! Escolha entre 1 e 4.")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nJogo interrompido pelo usuário. Até logo!")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        print("Por favor, reporte este erro.")