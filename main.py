import envia_frase_anime
import envia_fato_dog

print("--- BEM-VINDO AO IRRITADOR DE IRMÃS - A MELHOR FORMA DE IRRITAR A SUA ---")

print("Caso 1 - caso a sua irmã seja uma otaku")
print("Caso 2 - caso a sua irmã goste de cachorros")

irritador = int(input("Digite o caso da sua irma:"))

if (irritador == 1):
    envia_frase_anime.envia_mensagem(5)

if (irritador == 2):
    envia_fato_dog.envia_mensagem(5)