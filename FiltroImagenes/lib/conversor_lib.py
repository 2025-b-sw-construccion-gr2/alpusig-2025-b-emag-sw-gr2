"""
Módulo de conversión de imágenes.
Proporciona funcionalidades para convertir imágenes a escala de grises.
"""

from PIL import Image
import os


class ConversorImagenes:
    """Clase para realizar conversiones de imágenes."""
    
    def __init__(self):
        """Inicializa el conversor de imágenes."""
        pass
    
    def cargar_imagen(self, ruta_imagen):
        """
        Carga una imagen desde el disco.
        
        Args:
            ruta_imagen (str): Ruta de la imagen a cargar
            
        Returns:
            PIL.Image: Objeto imagen cargado
            
        Raises:
            FileNotFoundError: Si el archivo no existe
            IOError: Si hay error al abrir la imagen
        """
        if not os.path.exists(ruta_imagen):
            raise FileNotFoundError(f"No se encontró el archivo: {ruta_imagen}")
        
        try:
            imagen = Image.open(ruta_imagen)
            return imagen
        except Exception as e:
            raise IOError(f"Error al abrir la imagen: {str(e)}")
    
    def convertir_a_gris(self, imagen):
        """
        Convierte una imagen a escala de grises.
        
        Args:
            imagen (PIL.Image): Imagen a convertir
            
        Returns:
            PIL.Image: Imagen convertida a escala de grises
        """
        # Método eficiente usando el modo 'L' de Pillow
        # 'L' = 8-bit pixels, escala de grises
        imagen_gris = imagen.convert('L')
        return imagen_gris
    
    def guardar_imagen(self, imagen, ruta_salida):
        """
        Guarda una imagen en el disco.
        
        Args:
            imagen (PIL.Image): Imagen a guardar
            ruta_salida (str): Ruta donde guardar la imagen
            
        Raises:
            IOError: Si hay error al guardar la imagen
        """
        try:
            # Crear directorio de salida si no existe
            directorio = os.path.dirname(ruta_salida)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)
            
            imagen.save(ruta_salida)
        except Exception as e:
            raise IOError(f"Error al guardar la imagen: {str(e)}")
    
    def procesar_imagen(self, ruta_entrada, ruta_salida):
        """
        Procesa una imagen completa: carga, convierte y guarda.
        
        Args:
            ruta_entrada (str): Ruta de la imagen de entrada
            ruta_salida (str): Ruta donde guardar la imagen procesada
            
        Returns:
            dict: Diccionario con información del procesamiento
        """
        # Cargar imagen
        imagen_original = self.cargar_imagen(ruta_entrada)
        
        # Obtener información original
        info = {
            'tamaño_original': imagen_original.size,
            'modo_original': imagen_original.mode,
            'formato_original': imagen_original.format
        }
        
        # Convertir a escala de grises
        imagen_gris = self.convertir_a_gris(imagen_original)
        
        # Guardar imagen procesada
        self.guardar_imagen(imagen_gris, ruta_salida)
        
        # Agregar información del resultado
        info['tamaño_final'] = imagen_gris.size
        info['modo_final'] = imagen_gris.mode
        info['ruta_salida'] = ruta_salida
        
        return info
    
    def obtener_info_imagen(self, ruta_imagen):
        """
        Obtiene información detallada de una imagen.
        
        Args:
            ruta_imagen (str): Ruta de la imagen
            
        Returns:
            dict: Diccionario con información de la imagen
        """
        imagen = self.cargar_imagen(ruta_imagen)
        
        info = {
            'ruta': ruta_imagen,
            'tamaño': imagen.size,
            'ancho': imagen.width,
            'alto': imagen.height,
            'modo': imagen.mode,
            'formato': imagen.format
        }
        
        return info
