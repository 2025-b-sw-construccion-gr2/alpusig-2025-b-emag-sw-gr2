"""
Módulo de lógica para el Sistema de Gestión de Tareas.
Proporciona funciones para crear, listar, completar y eliminar tareas.
"""


class TaskManager:
    """Gestor de tareas con operaciones CRUD básicas."""

    def __init__(self):
        """Inicializa el gestor con una lista vacía de tareas."""
        self.tasks = []

    def add_task(self, title, description=""):
        """
        Agrega una nueva tarea a la lista.

        Args:
            title (str): Título de la tarea
            description (str): Descripción opcional de la tarea

        Returns:
            dict: La tarea creada con id, title, description y completed

        Raises:
            ValueError: Si el título está vacío
        """
        if not title or not title.strip():
            raise ValueError("El título de la tarea no puede estar vacío")

        task = {
            "id": len(self.tasks) + 1,
            "title": title.strip(),
            "description": description.strip(),
            "completed": False,
        }
        self.tasks.append(task)
        return task

    def get_all_tasks(self):
        """
        Obtiene todas las tareas.

        Returns:
            list: Lista de todas las tareas
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id):
        """
        Busca una tarea por su ID.

        Args:
            task_id (int): ID de la tarea a buscar

        Returns:
            dict: La tarea encontrada o None si no existe
        """
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def complete_task(self, task_id):
        """
        Marca una tarea como completada.

        Args:
            task_id (int): ID de la tarea a completar

        Returns:
            bool: True si se completó, False si no se encontró

        Raises:
            ValueError: Si el task_id no es válido
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("El ID debe ser un número entero positivo")

        task = self.get_task_by_id(task_id)
        if task:
            task["completed"] = True
            return True
        return False

    def delete_task(self, task_id):
        """
        Elimina una tarea de la lista.

        Args:
            task_id (int): ID de la tarea a eliminar

        Returns:
            bool: True si se eliminó, False si no se encontró

        Raises:
            ValueError: Si el task_id no es válido
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("El ID debe ser un número entero positivo")

        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def get_pending_tasks(self):
        """
        Obtiene todas las tareas pendientes (no completadas).

        Returns:
            list: Lista de tareas pendientes
        """
        return [task for task in self.tasks if not task["completed"]]

    def get_completed_tasks(self):
        """
        Obtiene todas las tareas completadas.

        Returns:
            list: Lista de tareas completadas
        """
        return [task for task in self.tasks if task["completed"]]

    def clear_all_tasks(self):
        """Elimina todas las tareas de la lista."""
        self.tasks.clear()
