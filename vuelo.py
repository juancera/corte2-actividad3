vuelo = {
    "Aerolinea": "Avianca",
    "Vuelo": "AV3102",
    "Origen": "CTG",
    "Destino": "MDE",
    "Tipo_Maleta": ["Cabina", "Mano", "Bodega"]
}

print("Aerolinea:", vuelo["Aerolinea"])
print("Vuelo:", vuelo["Vuelo"])
print("Origen:", vuelo["Origen"])
print("Destino:", vuelo["Destino"])
print("Tipo de maleta:", vuelo["Tipo_Maleta"])

print("Tipos de maleta permitidos:")
print(vuelo["Tipo_Maleta"])