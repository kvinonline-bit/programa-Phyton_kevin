#problema #1
#curso:fundamentos de programacion
#tarea #5
#codigo de autoria propia


sesiones = [
    [101, 240, 12],  
    [102, 45, 2],    
    [103, 120, 5],   
    [104, 200, 8],   
    [105, 75, 3],    
]

def clasificar_compromiso(duracion_segundos, clics):
   
    if duracion_segundos > 180 and clics > 8:
        return "Alto"
    if duracion_segundos < 60 or clics < 3:
        return "Bajo"
    return "Medio"

def sesiones_int():
  
    sesiones = []
    while True:
        entrada = input("Sesión (ID,duración,clics): ").strip()
        if entrada == "":
            break
        elif "," not in entrada:
            print("valor no valido")
            continue
        elif entrada.count(",") != 2:
            print("Formato incorrecto. Debe ser: ID,Duración,Clics")
            continue
        
        cliente_id, duracion, clics = entrada.split(",")
        sesiones.append([int(cliente_id), int(duracion), int(clics)])

    return sesiones


if __name__ == "__main__":
    sesiones += sesiones_int()
    print("\nInforme de compromiso de sesiones")
    print("ID Cliente | Clasificación")
    print("--------------------------")
    for session in sesiones:
        cliente_id, duracion, clics = session
        clasificacion = clasificar_compromiso(duracion, clics)
        
        print(f"{cliente_id} | {clasificacion}")