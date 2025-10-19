"""
Filtro de Imágenes - Proyecto Principal
Sistema de conversión de imágenes a color a escala de grises usando Pillow.

"""

import sys
import os

# Agregar el directorio lib al path para imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from lib.conversor_lib import ConversorImagenes
from lib.logger import Logger
from lib.input import ValidadorEntrada


def mostrar_menu():
    """Muestra el menú principal de la aplicación."""
    print("\n" + "="*50)
    print("FILTRO DE IMÁGENES - CONVERSOR A ESCALA DE GRISES")
    print("="*50)
    print("\nOpciones:")
    print("1. Convertir imagen a escala de grises")
    print("2. Ver información de una imagen")
    print("3. Salir")
    print("-"*50)


def convertir_imagen_interactivo(conversor, logger):
    """
    Proceso interactivo para convertir una imagen a escala de grises.
    
    Args:
        conversor (ConversorImagenes): Instancia del conversor
        logger (Logger): Instancia del logger
    """
    logger.info("Iniciando proceso de conversión de imagen")
    
    # Obtener ruta de entrada
    ruta_entrada = ValidadorEntrada.obtener_ruta_imagen()
    if not ruta_entrada:
        logger.error("Ruta de entrada inválida")
        return
    
    logger.info(f"Imagen de entrada: {ruta_entrada}")
    
    # Obtener ruta de salida
    ruta_salida = ValidadorEntrada.obtener_ruta_salida(ruta_entrada)
    logger.info(f"Imagen de salida: {ruta_salida}")
    
    try:
        # Procesar imagen
        print("\nProcesando imagen...")
        info = conversor.procesar_imagen(ruta_entrada, ruta_salida)
        
        # Mostrar resultados
        print("\n✓ Conversión exitosa!")
        print(f"\nInformación del procesamiento:")
        print(f"  - Tamaño: {info['tamaño_original']}")
        print(f"  - Modo original: {info['modo_original']}")
        print(f"  - Modo final: {info['modo_final']}")
        print(f"  - Archivo guardado en: {info['ruta_salida']}")
        
        logger.info(f"Conversión exitosa: {ruta_entrada} -> {ruta_salida}")
        
    except Exception as e:
        print(f"\n✗ Error al procesar la imagen: {str(e)}")
        logger.error(f"Error en conversión: {str(e)}")


def ver_info_imagen(conversor, logger):
    """
    Muestra información detallada de una imagen.
    
    Args:
        conversor (ConversorImagenes): Instancia del conversor
        logger (Logger): Instancia del logger
    """
    logger.info("Consultando información de imagen")
    
    ruta_entrada = ValidadorEntrada.obtener_ruta_imagen()
    if not ruta_entrada:
        logger.error("Ruta de entrada inválida")
        return
    
    try:
        info = conversor.obtener_info_imagen(ruta_entrada)
        
        print("\nInformación de la imagen:")
        print(f"  - Ruta: {info['ruta']}")
        print(f"  - Dimensiones: {info['ancho']} x {info['alto']} píxeles")
        print(f"  - Tamaño: {info['tamaño']}")
        print(f"  - Modo de color: {info['modo']}")
        print(f"  - Formato: {info['formato']}")
        
        logger.info(f"Información consultada para: {ruta_entrada}")
        
    except Exception as e:
        print(f"\n✗ Error al obtener información: {str(e)}")
        logger.error(f"Error al consultar información: {str(e)}")


def main():
    """Función principal del programa."""
    # Inicializar componentes
    logger = Logger()
    conversor = ConversorImagenes()
    
    logger.info("="*50)
    logger.info("Iniciando aplicación Filtro de Imágenes")
    logger.info("="*50)
    
    # Crear directorio de salida si no existe
    if not os.path.exists("salida"):
        os.makedirs("salida")
        logger.info("Directorio 'salida' creado")
    
    # Loop principal
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == '1':
            convertir_imagen_interactivo(conversor, logger)
        elif opcion == '2':
            ver_info_imagen(conversor, logger)
        elif opcion == '3':
            print("\n¡Hasta luego!")
            logger.info("Aplicación finalizada por el usuario")
            break
        else:
            print("\n✗ Opción inválida. Por favor, seleccione 1, 2 o 3.")
            logger.warning(f"Opción inválida seleccionada: {opcion}")
        
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
