"""
Módulo de logging para el sistema de filtro de imágenes.
Proporciona funcionalidades para registrar eventos y errores.
"""

from datetime import datetime


class Logger:
    """Clase para gestionar el registro de eventos del sistema."""
    
    def __init__(self, archivo_log="filtro_imagenes.log"):
        """
        Inicializa el logger.
        
        Args:
            archivo_log (str): Nombre del archivo donde se guardarán los logs
        """
        self.archivo_log = archivo_log
    
    def registrar(self, mensaje, tipo="INFO"):
        """
        Registra un mensaje con timestamp.
        
        Args:
            mensaje (str): Mensaje a registrar
            tipo (str): Tipo de mensaje (INFO, ERROR, WARNING)
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea_log = f"[{timestamp}] [{tipo}] {mensaje}"
        
        # Escribir en archivo
        with open(self.archivo_log, "a", encoding="utf-8") as archivo:
            archivo.write(linea_log + "\n")
        
        # Mostrar en consola
        print(linea_log)
    
    def info(self, mensaje):
        """Registra un mensaje informativo."""
        self.registrar(mensaje, "INFO")
    
    def error(self, mensaje):
        """Registra un mensaje de error."""
        self.registrar(mensaje, "ERROR")
    
    def warning(self, mensaje):
        """Registra un mensaje de advertencia."""
        self.registrar(mensaje, "WARNING")
