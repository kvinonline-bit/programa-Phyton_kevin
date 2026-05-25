#Nombre Estudiante: Harnol Kevin Vargas Ferreira 
#Grupo : 614
#Programa: Fundamentos de programacion
#Codigo Fuente: Autoria Propia 
#ejercicio 1
"""
Problema 1: Una matriz almacena datos de sesiones de clientes con el 
formato: [ID Cliente, Duración (segundos), Eventos Clics].  
Se necesita una herramienta para evaluar el nivel de compromiso de 
cada sesión.
Requisitos de Desarrollo: - Datos Iniciales: Una matriz con al menos 5 filas de datos. 
- Módulos: Se requiere un módulo (función) para calcular la clasificación de compromiso de una sesión basándose en su duración y clics. 
- Lógica de Negocio: 
✓ Clasificar como "Alto" (si Duración > 180s y Clics > 8).  
✓ Clasificar como "Bajo" (si Duración < 60s o Clics < 3). 
✓ Clasificar como "Medio" en todos los demás casos. 
- Salida: Generar un informe listando el ID del cliente y su 
clasificación final."""

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
    print("Informe de compromiso de sesiones")
    print('''
╔══════════════╦══════════════╗
║ID Cliente    ║ Clasificación║
╠══════════════╬══════════════╣''')
   
    for session in sesiones:
        cliente_id, duracion, clics = session
        clasificacion = clasificar_compromiso(duracion, clics)
       
        print(f"║{cliente_id:<13} ║ {clasificacion:<13}║")
    print('''╚══════════════╩══════════════╝''')