from PIL import Image, ImageDraw, ImageFont
import datetime

if __name__ == "__main__":
    
    with Image.open("429.jpg", "r") as img:
        print("Carregando a imagem...")
        draw = ImageDraw.Draw(img)

        # Tenta carregar a font comic sans. Caso não encontre, carrega a fonte padrão do sistema
        print("Tentando carregar a fonte comic-sans.")
        try:
            font = ImageFont.truetype("comic-sans", 16)
        except:
            print("Fonte comic-sans não encontrada. Carregando a fonte padrão do sistema.")
            font = ImageFont.load_default(size=48)

        # Vamos escrever um texto na imagem
        print("Desenhando o texto na imagem.")
        draw.text(
            xy=(33, 15,),
            text="Proway 2025",
            fill=(217, 32, 44, 128),
            font=font)
        
        # Salvar o arquivo
        texto_data_hora = datetime.datetime.now(datetime.UTC).strftime(
            "%Y%m%d%H%M%S"
        )
        nome_do_arquivo = f"429_{texto_data_hora}.jpg"
        
        print(f"Salvando o arquivo '{nome_do_arquivo}'.")
        img.save(nome_do_arquivo)