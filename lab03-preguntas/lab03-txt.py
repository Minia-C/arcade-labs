import random
lista_diccionario=[]
def extraer_pregunta(pregunta:str)->dict:
    partes=pregunta.split("|")
    preguntas=partes[0]
    lista=partes[1:]
    verdadera=lista[0]
    falsa=lista[0:]
    return{
        "pregunta":preguntas,
        "correcta":verdadera,
        "opciones":falsa,

    }
preguntas_txt=[
"¿Cuál es la capital de España?|Madrid|Barcelona|Sevilla|Toledo",
"¿Cuántos continentes hay?|5|7|6|3",
"¿Qué lenguaje se usa para programar en Arcade?Python|Java|JavaScript|C",
"¿La tortilla de patata lleva cebolla?|Jamás|Si|No con excepciones|Tal vez"
]
for linea in preguntas_txt:
    resultado=extraer_pregunta(linea)
    lista_diccionario.append(resultado)
tope=len(lista_diccionario)
contador=0
puntos=0
while contador<tope:
 opciones1=(lista_diccionario[contador]["opciones"])
 random.shuffle(opciones1)
 print(lista_diccionario[contador]["pregunta"])
 print(opciones1)
 patata=input(("escribe la correcta: "))
 correcta=(lista_diccionario[contador]["correcta"])
 if patata==correcta:
    print("felicidades")
    puntos+=10
 else:
    print("fallaste")
    puntos-=5
 contador+=1
print(puntos)
if puntos<0:
   print("subnormal")