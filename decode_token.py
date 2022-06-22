import jwt
import json
import code_token
def buscarPalabraPorEntrada( arrayDatos, objetivo):
    num=0
    for entrada in arrayDatos:
        if( arrayDatos[entrada]== objetivo):
            num=num+1
        if( num  >0):
            print(arrayDatos[entrada])
    if( num  ==0):
         print("No encontrado")
try:
    search = jwt.decode(code_token.token, code_token.key, algorithms="HS256")
    searchWord =input("Ingrese el dato a buscar:  ")

    search = json.dumps(search)
    datosArray = json.loads(search)
    if( searchWord == ""):
        print(datosArray)
    else:
       buscarPalabraPorEntrada(datosArray, searchWord)

except:
    print("Firma incorrecta.")



