temperaturas = []

for i in range(1,6):
	temperatura = []
	temperatura.append(int(input("Día %d. Temperatura máxima: " % i)))
	temperatura.append(int(input("Día %d. Temperatura mínima: " % i)))
	temperaturas.append(temperatura)

print("Temperaturas medias")
print("--------------------")

i = 1
for temperatura in temperaturas:
	print("Día %d. Temperatura media: %f: " % (i,sum(temperatura)/len(temperatura)))
	i += 1

temMinima = temperaturas[0][1];

for temperatura in temperaturas:
	if temperatura[1] < temMinima:
		temMinima = temperatura[1]

print("Días con menos temperatura")
print("--------------------")

i = 1
for temperatura in temperaturas:
	if temperatura[1] == temMinima:
		print("Día %d " % i)
	i +=1
	
exisTemperatura = False
print("Días con temperatura máxima")
print("---------------------")
temMaxima = int(input("Introduce una temperatura: "))

i = 1
for temperatura in temperaturas:
	if temperatura[0] == temMaxima:
		print("Día %d" % i)
		exisTemperatura = True
	i +=1
if not exisTemperatura:
	print("No hay ningún día con dicha temperatura. ")
