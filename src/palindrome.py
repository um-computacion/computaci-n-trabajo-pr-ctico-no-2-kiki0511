# Implementar función is_palindrome
def is_palindrome(text: str) -> bool:
    """
    Verifica si el texto dado es un palíndromo.
    Esta función utiliza dos funciones auxiliares:
      - clean_text: para limpiar el texto.
      - compare_characters: para comparar el texto limpio con su versión invertida.
    """
   
    cleaned = clean_text(text)  # Función Implementar limpieza de texto
    return compare_characters(cleaned)  # Función Implementar comparación de caracteres

#  definimos para evitar errores:
def clean_text(text: str) -> str:
    pass

def compare_characters(cleaned_text: str) -> bool:
    pass


#Implementar limpieza de texto

import string

def clean_text(text: str) -> str:
    """
    Limpia el texto eliminando espacios, signos de puntuación y convirtiendo todo a minúsculas.
    """
    #  un traductor para eliminar la puntuación
    translator = str.maketrans('', '', string.punctuation)
    # Se elimina la puntuación, se quitan los espacios y se transforma a minúsculas.
    cleaned = text.translate(translator).replace(" ", "").lower()
    return cleaned

# Implementar comparación de caracteres
def compare_characters(cleaned_text: str) -> bool:
    """
    Compara el texto limpio con su versión invertida para determinar si es un palíndromo.
    """
    return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    # Programa interactivo para probar el detector de palíndromos
    while True:
        try:
            entrada = input("Ingrese una palabra o frase: ")
            if entrada.strip() == "":
                print("Entrada vacía. Por favor, ingrese un texto.")
                continue
            if is_palindrome(entrada):
                print(f'"{entrada}" es un palíndromo')
            else:
                print(f'"{entrada}" no es un palíndromo')
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")
            break