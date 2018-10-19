import os
import subprocess

def ns(r):
    while r!="n" and r!="s":
        r=input("Introduzca solo \'n\' o \'s\' según su opción: ")
    return r

archivos_wav=[]
lista=os.listdir('/Users/Antonio/AppData/Local/Programs/Python/Python36-32/')

for nombre in lista:
    if nombre[-4:]==".wav":
        archivos_wav.append(nombre)

while True:
    file=(input("Introduzca archivo a reproducir: ")+(".wav"))
    if file in archivos_wav:
        os.system(file)
    else:
        print("No se encontró el archivo",file,"especificado")

    conti=ns(input("¿Desea continuar?: "))  
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
    
