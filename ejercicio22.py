def contar_palabra(texto, palabra):
    contador = 0
    palabras = texto.split()
    for p in palabras:
        if p == palabra:
            contador += 1
    return contador

texto = """Por presumir, a mis amigos les conté
Que en el amor ninguna pena me aniquila
Que pa' probarles, de tus besos me olvide
Y me bastaron unos tragos de tequila

Les platique que me encontré con otro amor
Y que en sus brazos fui dejando de quererte
Que te aborrasco desde el día de tu traición
Y que hay momentos que he deseado hasta tu muerte

Acá entre nos, quiero que sepas la verdad
No te he dejado de adorar, allá en mi triste soledad
Me han dado ganas de gritar, salir corriendo
Y preguntar qué es lo que ha sido de tu vida

Acá entre nos, Siempre te voy a recordar
Y hoy que a mi lado ya no estas no queda más confesar
Que ya no puedo soportar, que estoy odiando sin odiar
Porque respiro por la herida

Y ay Martin no cabe duda que también de dolor se canta
Cuando llorar no se puede

Acá entre Nos, Quiero que sepas la verdad
No te he dejado de adorar, allá en mi triste soledad
Me han dado ganas de gritar salir corriendo
Y preguntar qué es lo que ha sido de tu vida

Aca entre nos, Siempre te voy a recordar
Y hoy que a mi lado ya no estas no queda más confesar
Que ya no puedo soportar que estoy odiando sin odiar
Porque respiro por la herida"""

palabra = input("Ingresa la palabra de la que quieres saber sus repeticiones: ")

print("La palabra existe",contar_palabra(texto, palabra), "veces")
