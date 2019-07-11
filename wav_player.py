import os
import wave
import subprocess

def ns(r):
    while r!="n" and r!="s":
        r=input("Introduzca solo \'n\' o \'s\' según su opción: ")
    return r

while True:
    dire=input("Introduce directorio: ")
    if os.path.isdir(dire):
        os.chdir(dire)
        break

while True:
    file=(input("Introduzca archivo a reproducir: ")+(".wav"))
    if file in dire :
        wave.open(file,'rb')
        Wave_read.close()
    else:
        print("No se encontró el archivo",file,"especificado")

    conti=ns(input("¿Desea continuar?: "))  
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
    
