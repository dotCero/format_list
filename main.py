from controller.read_list_controller import ReadListController

ubication = '_____'
route = input("Hola, ingrese ruta de documento de texto: ")

rlc = ReadListController(route)

chain = input("Ingrese cadena de texto que contendrá la lista, para ubicarla, ingrese " + ubication + " sin las comilas: ")

chain = chain.replace(ubication, rlc.get_formatted_list(True))

print(chain)
