def crear_punts(llista):
    """Imprimeix tants punts com el valor de cada número de la llista, amb un salt de línia entre ells."""
    for num in llista:
        print("." * num)  # Imprimeix els punts corresponents

def dibuixar_imatge():
    """Dibuixa una imatge senzilla amb crear_punts()."""
    llista_piramide = [1, 2, 3, 4, 5]  # Altura de la piràmide
    crear_punts(llista_piramide)

# Prova de la funció
dibuixar_imatge()
