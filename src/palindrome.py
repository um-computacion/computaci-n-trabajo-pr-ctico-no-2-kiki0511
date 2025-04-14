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