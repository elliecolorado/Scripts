"""
ZipCracker - Un script para realizar fuerza bruta sobre archivos ZIP con una lista de contraseñas.

Descripción: Este script intenta extraer un archivo ZIP protegido por contraseña probando cada contraseña de una lista proporcionada hasta que encuentra la correcta. Originalmente creado para un CTF de Immune Institute.

Uso: python ZipCracker.py <zip_file> <txt_file>

Argumentos:
- <zip_file> -> Localización del archivo ZIP protegido por contraseña.
- <txt_file> -> Localización del archivo TXT que contiene las contraseñas a probar.

Autora: Ellie Colorado
"""

import zipfile
import sys
import os

def test_passwords(zip_file, txt_file):
    with open(txt_file, 'r') as file:
        passwords = file.readlines()
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        for password in passwords:
            password = password.strip()
            try:
                zip_ref.extractall(pwd=password.encode('utf-8'))
                print(f"\Contraseña para \"{zip_file}\" encontrada en \"{txt_file}\": {password}")
                return password
            except Exception as e:
                pass
    print(f"\Contraseña para \"{zip_file}\" no encontrada en \"{txt_file}\"." )
    return None

def main():
    if len(sys.argv) == 3:
        zip_file = sys.argv[1]
        txt_file = sys.argv[2]
        
        if(not zip_file.endswith(".zip") or not txt_file.endswith(".txt")):
            if(not zip_file.endswith(".zip")):
                print(f"\tError: El primer argumento \"{zip_file}\" no es un archivo .zip.")
            if(not txt_file.endswith(".txt")):
                print(f"\tError: El segundo argumento \"{txt_file}\" no es un archivo .txt.")
        elif(not os.path.exists(zip_file) or not os.path.exists(txt_file)):
            if(not os.path.exists(zip_file)):
                print(f"\tError: El archivo \"{zip_file}\" no existe.")
            if(not os.path.exists(txt_file)):
                print(f"\tError: El archivo \"{txt_file}\" no existe.")
            
            
        else: test_passwords(zip_file, txt_file)
        
    else: print("python ZipCracker.py <zip_file> <txt_file>\n<zip_file> -> Localización del archivo ZIP protegido por contraseña.\n<txt_file> -> Localización del archivo TXT que contiene las contraseñas a probar.")
if __name__ == "__main__":
    main()