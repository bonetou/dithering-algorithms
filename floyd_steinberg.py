def floyd_steinberg(img):
    limite = 0.25
    x, y = img.shape
    
    for i in range(x-1):
        for j in range(y-1):
            
            pixel = img[i][j]
            
            if(pixel < limite):
                erro = img[i][j] - 0
                img[i][j] = 0 # preto
                
            elif((pixel > limite) and (pixel <= limite + 0.25)):
                erro = img[i][j] - 0.25
                img[i][j] = 0.25
                
            elif((pixel > limite + 0.25) and (pixel <= limite + 0.5)):
                erro = img[i][j] - 0.5
                img[i][j] = 0.5
                
            else:
                erro = img[i][j] - 1
                img[i][j] = 1 # branco

            img[i+1][j] += (3/8) * erro
            img[i][j+1] += (3/8) * erro
            img[i+1][j+1] += erro / 4
            
    return img