# decimal_a_binario
#Cristopher_Venegas
#Kevin Almache
#Esteban Trujillo


numero = int(input("Ingrese un número decimal de dos cifras (00–99): "))


if 0 <= numero <= 99:
    binario = ""   
    n = numero     

    
    while n > 0:
        residuo = n % 2          
        binario = str(residuo) + binario  
        n = n // 2               

    
    while len(binario) < 8:
        binario = "0" + binario

    
    print("El número", numero, "en binario de 8 bits es:", binario)


else:
    print("Error: el número debe estar entre 0 y 99.")