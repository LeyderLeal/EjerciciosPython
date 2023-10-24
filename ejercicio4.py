#  La pizzería Napolitana de la Ciudad de Neiva ofrece pizzas vegetarianas y no vegetarianas a
# sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación:
# • Ingredientes vegetarianos: Pimiento y tofu.
# • Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función
# de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se
# puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los
# ingredientes que lleva.

print("Pizzería Napolitana")
print("--------------------")
print("Que tipo de pizza quiere")
pizza = int(input(" precione 1 para vegetariana \n precione 2 para opciones no vegetarianas: "))

if pizza == 1:
    print("Ingredientes de pizzas vegetarianas")
    print(" 1- Pimiento\n 2- Tofu")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == 1:
        print("Pimiento")
    else:
        print("tofu")
elif pizza == 2:
    print("Ingredientes de pizzas no vegetarianas")
    print(" 1- Peperoni\n 2- Jamón \n 3- Salmón")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == 1:
        print("Peperoni")
    elif ingrediente == 2:
        print("Jamón")
    elif ingrediente == 3:
        print("Salmón")

