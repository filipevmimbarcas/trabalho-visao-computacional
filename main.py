import cv2
import pickle
import numpy as np


vagas = []

with open('vagas.pkl','rb') as arquivo:
    vagas = pickle.load(arquivo)




video = cv2.VideoCapture('video-carga.mp4')

while True:
    check, img = video.read()
    img_cinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_th = cv2.adaptiveThreshold(img_cinza,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    img_median = cv2.medianBlur(img_th,5)
    kernel = np.ones((3,3),np.int8)
    img_dil = cv2.dilate(img_median,kernel)


    vagas_livres = 0

    for x,y,w,h in vagas:
        vaga = img_dil[y:y+h,x:x+w]
        contador = cv2.countNonZero(vaga)
        cv2.putText(img,str(contador),(x,y+h-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)

        if contador < 1500:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            vagas_livres = vagas_livres + 1
        else:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        
        cv2.rectangle(img,(90,0),(415,60),(0,255,0),-1)
        cv2.putText(img, f'Livre: {vagas_livres}/9 ',(95,45),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255.255,255),5)


    cv2.imshow('Video', img)
    #cv2.imshow('Video Th', img_th)
    #cv2.imshow('Video Median', img_median)
    #cv2.imshow('Video dil', img_dil)
    cv2.waitKey(10)