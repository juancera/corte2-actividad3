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

print("Valores de tipo de maleta:")
for tipo in vuelo["Tipo_Maleta"]:
    print(tipo)
