import cv2 
import pickle

img = cv2.imread('carga.png')

numero_de_vagas = 9

vagas = []

for x in range(numero_de_vagas):
    vaga = cv2.selectROI('vagas',img, False)
    cv2.destroyWindow('vagas')
    vagas.append((vaga))

    for x,y,w,h in vagas:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        

with open('vagas.pkl','wb') as arquivo:
    pickle.dump(vagas,arquivo)