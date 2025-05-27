import requests

def baixar_img(url, nome_arquivo):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        with open(nome_arquivo, 'wb') as arquivo: #wb --> write binary (pega o arquivo escrito em binário)
            arquivo.write(resposta.content)
        print(f"Imagem salva como {nome_arquivo}")
    else:
        print("Erro ao baixar a imagem.")

def get_personagem(id_personagem):
    url = f"https://rickandmortyapi.com/api/character/{id_personagem}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        nome = dados['name']
        imagem = dados['image']
        print(f"Personagem: {nome}")
        print(f"Imagem: {imagem}")

        nome_arquivo = f"{nome.replace(' ', '_')}.jpg"
        baixar_img(imagem, nome_arquivo)

    else:
        print("Personagem não encontrado")

def main():
    while True: 
        id_personagem = input("\nDigite o ID do personagem (ou 'sair' para encerrar o programa): ").strip()
        
        if id_personagem.lower() == 'sair':
            print('\nPrograma encerrado')
            break

        if not id_personagem.isdigit():
            print("Por favor, digite um ID numérico válido")
            continue

        get_personagem(id_personagem)

if __name__ == "__main__":
    main()