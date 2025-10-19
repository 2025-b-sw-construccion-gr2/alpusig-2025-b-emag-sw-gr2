"""
Módulo de entrada y validación para el sistema de filtro de imágenes.
Maneja la interacción con el usuario y validación de archivos.
"""

import os


class ValidadorEntrada:
    """Clase para validar entradas de usuario y archivos."""
    
    EXTENSIONES_VALIDAS = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'}
    
    @staticmethod
    def validar_archivo_existe(ruta_archivo):
        """
        Verifica si un archivo existe.
        
        Args:
            ruta_archivo (str): Ruta del archivo a verificar
            
        Returns:
            bool: True si el archivo existe, False en caso contrario
        """
        return os.path.isfile(ruta_archivo)
    
    @staticmethod
    def validar_extension(ruta_archivo):
        """
        Verifica si la extensión del archivo es válida.
        
        Args:
            ruta_archivo (str): Ruta del archivo a verificar
            
        Returns:
            bool: True si la extensión es válida, False en caso contrario
        """
        _, extension = os.path.splitext(ruta_archivo)
        return extension.lower() in ValidadorEntrada.EXTENSIONES_VALIDAS
    
    @staticmethod
    def obtener_ruta_imagen():
        """
        Solicita al usuario la ruta de una imagen y la valida.
        
        Returns:
            str: Ruta válida de la imagen o None si hay error
        """
        ruta = input("Ingrese la ruta de la imagen a convertir: ").strip()
        
        if not ValidadorEntrada.validar_archivo_existe(ruta):
            print(f"Error: El archivo '{ruta}' no existe.")
            return None
        
        if not ValidadorEntrada.validar_extension(ruta):
            print(f"Error: Extensión de archivo no válida. Extensiones permitidas: {', '.join(ValidadorEntrada.EXTENSIONES_VALIDAS)}")
            return None
        
        return ruta
    
    @staticmethod
    def obtener_ruta_salida(ruta_entrada):
        """
        Genera o solicita la ruta de salida para la imagen procesada.
        
        Args:
            ruta_entrada (str): Ruta de la imagen de entrada
            
        Returns:
            str: Ruta de salida para la imagen procesada
        """
        directorio, nombre_archivo = os.path.split(ruta_entrada)
        nombre_base, extension = os.path.splitext(nombre_archivo)
        
        # Sugerir ruta por defecto
        ruta_default = os.path.join("salida", f"{nombre_base}_gris{extension}")
        
        print(f"\nRuta de salida sugerida: {ruta_default}")
        respuesta = input("¿Desea usar esta ruta? (s/n): ").strip().lower()
        
        if respuesta == 's' or respuesta == '':
            return ruta_default
        else:
            ruta_personalizada = input("Ingrese la ruta de salida: ").strip()
            return ruta_personalizada
