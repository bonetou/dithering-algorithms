def modularizacao_aleatoria(img):
    
    x, y = img.shape
    limite = 0.25
    # varrendo sobre todos os pixels
    # esquerda para direita e de cima para baixo
    for i in range(x):
        for j in range(y):
            
            pixel = img[i][j] + np.random.uniform(0, 0.25)

            if(pixel < limite):
                img[i][j] = 0 # preto
                
            elif((pixel > limite) and (pixel <= limite + 0.25)):
                img[i][j] = 0.25
                
            elif((pixel > limite + 0.25) and (pixel <= limite + 0.5)):
                img[i][j] = 0.5
                
            else:
                img[i][j] = 1 # branco
    return img