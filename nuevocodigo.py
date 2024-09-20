
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all([celda == jugador for celda in fila]):
            return True

    # Verificar columnas
    for col in range(3):
        if all([tablero[fila][col] == jugador for fila in range(3)]):
            return True

    # Verificar diagonales
    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True

    return False

def tablero_lleno(tablero):
    return all([celda != " " for fila in tablero for celda in fila])

def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador_actual}, ingresa la fila (0, 1, 2): "))
        columna = int(input(f"Jugador {jugador_actual}, ingresa la columna (0, 1, 2): "))

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡Jugador {jugador_actual} ha ganado!")
                break
            elif tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print("¡Es un empate!")
                break
            jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("Esa celda ya está ocupada. Intenta de nuevo.")

if __name__ == "__main__":
    jugar()
