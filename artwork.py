import os
from PIL import Image

#Caminho onde estão as artes
art_path = './artwork/'
#Caminho onde está o background
background = './background.jpg'
#Lista com todas as artes
art_list = os.listdir(art_path)


#Abrir imagem que será usada de fundo e redimensioná-la
background_image = Image.open(background)
background_resized = background_image.resize((800, 1200))

#Iterar pelas imagens de obras de arte, adicionar moldura e aplicar sobre o background
for art in art_list:
    #Abrir a imagem da arte
    art_image = Image.open(art_path + art)
    #Redimensionar o tamanho da arte
    art_resized = art_image.resize((300, 200))
    
    #Criar a imagem preta um pouco maior que imagem original para fazer a função de moldura
    border = Image.new('RGB', (320, 220), color = 'black')
    #Criar cópia da imagem da borda (moldura)
    art_border = border.copy()
    #Colar a imagem da arte sobre a moldura e arrumar o posicionamento
    art_border.paste(art_resized, (10, 10))

    #Criar cópia da imagem de background
    art_background = background_resized.copy()
    #Colar a imagem da arte com moldura sobre o background e arrumar o posicionamento
    art_background.paste(art_border, (245, 455))
    #Salvar imagem
    art_background.save(art_path + 'arte_exposta - ' + art)

print ('Processo completo')
