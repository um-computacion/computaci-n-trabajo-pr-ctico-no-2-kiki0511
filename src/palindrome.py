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
