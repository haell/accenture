
# Instruções:
# 1 - Entender a lógica 
# 2 - Inserir o comentário onde tem "# Cerquilha" em cada bloco 
# 3 - Fazer rodar o código na IDE
# Obs: Não é permitido nenhum tipo de consulta.
# Inicia a classe do jogo da forca
import random

class JogoForca():
    # inicializa a lista de palavras
    def __init__(self):
        self.palavras = ['python', 'programacao', 'computador', 'jogo', 'forca', 'desenvolvimento']
    # sorteia uma palavra aleatória da lista
    def sortear_palavra(self):
        return random.choice(self.palavras)
    # funcao para mostrar o tabuleiro com letras corretas e espaços para letras faltantes
    def mostrar_tabuleiro(self, palavra, letras_corretas):
        tabuleiro = ''
        for letra in palavra:
            if letra in letras_corretas:
                tabuleiro += letra
            else:
                tabuleiro += '_'
        return tabuleiro
    # função principal do jogo
    def jogar_forca(self):
        palavra = self.sortear_palavra()
        letras_corretas = []
        tentativas = 6
        print("Bem-vindo ao jogo da forca!")
        print("A palavra tem", len(palavra), "letras.")
        # Loop principal do jogo
        while True:
            print("\nPalavra:", self.mostrar_tabuleiro(palavra, letras_corretas))
            letra = input("Digite uma letra: ").lower()
            if letra in letras_corretas:
                print("Você já tentou essa letra. Tente outra.")
            elif letra in palavra:
                letras_corretas.append(letra)
                print("Letra correta!")
            else:
                tentativas -= 1  
                print("Letra errada. Você tem", tentativas, "tentativas restantes.")
            if tentativas == 0:
                print("Você perdeu! A palavra era:", palavra)
                break
            if all(letra in letras_corretas for letra in palavra):
                print("Parabéns! Você ganhou!")
                break

if __name__ == "__main__":
    gf = JogoForca() # Cria uma instância do jogo
    gf.jogar_forca() # Aqui começa o jogo