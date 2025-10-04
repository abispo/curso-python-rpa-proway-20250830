# Adicionar imagem em outra imagem

from PIL import Image

if __name__ == "__main__":
    
    imagem_original = Image.open("galo.jpg").convert("RGBA")
    imagem_marca = Image.open("dino.png").convert("RGBA")

    largura, altura = imagem_original.size
    imagem_marca = imagem_marca.resize(
        (int(largura * 0.20), int(altura * 0.20))
    )

    pos_x = 750
    pox_y = 100

    # Aplicar a marca dágua
    imagem_com_marca = Image.new("RGBA", imagem_original.size)
    imagem_com_marca = Image.alpha_composite(
        imagem_original, Image.new("RGBA", imagem_original.size)
    )
    imagem_com_marca.paste(imagem_marca, (pos_x, pox_y,), imagem_marca)

    imagem_com_marca.convert("RGB").save("imagem_com_marca.jpg", "JPEG")