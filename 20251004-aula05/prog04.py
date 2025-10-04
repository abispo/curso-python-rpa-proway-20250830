from PIL import Image

if __name__ == "__main__":
    imagem = Image.open("200.jpg")

    # Obtemos informações sobre a imagem
    print(f"Formato: {imagem.format}.")
    print(f"Tamanho: {imagem.size}.")
    print(f"Modo: {imagem.mode}")

    # A imagem é aberta no visualizador padrão do sistema
    # imagem.show()

    # Redimensionar a imagem
    imagem_redimensionada = imagem.resize((1600, 900,))

    # Salvando a imagem redimensionada com um novo formato
    imagem_redimensionada.save(
        "200_redimensionado.bmp",
        format="bmp",
        compression=2
    )

    # Rotacionando a imagem
    imagem_rotacionada = imagem.rotate(45)
    imagem_rotacionada.save("200_rotacionado.jpg", format="jpeg")
