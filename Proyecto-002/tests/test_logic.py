"""
Pruebas unitarias para el módulo logic.py
"""

import pytest
from src.logic import TaskManager


class TestTaskManager:
    """Suite de pruebas para la clase TaskManager."""

    @pytest.fixture
    def task_manager(self):
        """Fixture que proporciona una instancia limpia de TaskManager."""
        return TaskManager()

    def test_add_task_success(self, task_manager):
        """Prueba agregar una tarea exitosamente."""
        task = task_manager.add_task("Comprar leche", "En el supermercado")

        assert task["id"] == 1
        assert task["title"] == "Comprar leche"
        assert task["description"] == "En el supermercado"
        assert task["completed"] is False

    def test_add_task_without_description(self, task_manager):
        """Prueba agregar una tarea sin descripción."""
        task = task_manager.add_task("Estudiar Python")

        assert task["title"] == "Estudiar Python"
        assert task["description"] == ""
        assert task["completed"] is False

    def test_add_task_empty_title_raises_error(self, task_manager):
        """Prueba que un título vacío lance una excepción."""
        with pytest.raises(
            ValueError, match="El título de la tarea no puede estar vacío"
        ):
            task_manager.add_task("")

    def test_add_task_whitespace_title_raises_error(self, task_manager):
        """Prueba que un título con solo espacios lance una excepción."""
        with pytest.raises(
            ValueError, match="El título de la tarea no puede estar vacío"
        ):
            task_manager.add_task("   ")

    def test_get_all_tasks_empty(self, task_manager):
        """Prueba obtener todas las tareas cuando no hay ninguna."""
        tasks = task_manager.get_all_tasks()
        assert tasks == []

    def test_get_all_tasks_multiple(self, task_manager):
        """Prueba obtener múltiples tareas."""
        task_manager.add_task("Tarea 1")
        task_manager.add_task("Tarea 2")
        task_manager.add_task("Tarea 3")

        tasks = task_manager.get_all_tasks()
        assert len(tasks) == 3

    def test_get_task_by_id_success(self, task_manager):
        """Prueba buscar una tarea por ID exitosamente."""
        task_manager.add_task("Tarea 1")
        task = task_manager.get_task_by_id(1)

        assert task is not None
        assert task["id"] == 1
        assert task["title"] == "Tarea 1"

    def test_get_task_by_id_not_found(self, task_manager):
        """Prueba buscar una tarea que no existe."""
        task = task_manager.get_task_by_id(999)
        assert task is None

    def test_complete_task_success(self, task_manager):
        """Prueba marcar una tarea como completada."""
        task_manager.add_task("Hacer ejercicio")
        result = task_manager.complete_task(1)

        assert result is True
        task = task_manager.get_task_by_id(1)
        assert task["completed"] is True

    def test_complete_task_not_found(self, task_manager):
        """Prueba completar una tarea que no existe."""
        result = task_manager.complete_task(999)
        assert result is False

    def test_complete_task_invalid_id_raises_error(self, task_manager):
        """Prueba completar una tarea con ID inválido."""
        with pytest.raises(
            ValueError, match="El ID debe ser un número entero positivo"
        ):
            task_manager.complete_task(0)

        with pytest.raises(
            ValueError, match="El ID debe ser un número entero positivo"
        ):
            task_manager.complete_task(-1)

    def test_delete_task_success(self, task_manager):
        """Prueba eliminar una tarea exitosamente."""
        task_manager.add_task("Tarea temporal")
        result = task_manager.delete_task(1)

        assert result is True
        assert len(task_manager.get_all_tasks()) == 0

    def test_delete_task_not_found(self, task_manager):
        """Prueba eliminar una tarea que no existe."""
        result = task_manager.delete_task(999)
        assert result is False

    def test_delete_task_invalid_id_raises_error(self, task_manager):
        """Prueba eliminar una tarea con ID inválido."""
        with pytest.raises(
            ValueError, match="El ID debe ser un número entero positivo"
        ):
            task_manager.delete_task(0)

    def test_get_pending_tasks(self, task_manager):
        """Prueba obtener solo las tareas pendientes."""
        task_manager.add_task("Tarea 1")
        task_manager.add_task("Tarea 2")
        task_manager.add_task("Tarea 3")
        task_manager.complete_task(2)

        pending = task_manager.get_pending_tasks()
        assert len(pending) == 2
        assert all(not task["completed"] for task in pending)

    def test_get_completed_tasks(self, task_manager):
        """Prueba obtener solo las tareas completadas."""
        task_manager.add_task("Tarea 1")
        task_manager.add_task("Tarea 2")
        task_manager.add_task("Tarea 3")
        task_manager.complete_task(1)
        task_manager.complete_task(3)

        completed = task_manager.get_completed_tasks()
        assert len(completed) == 2
        assert all(task["completed"] for task in completed)

    def test_clear_all_tasks(self, task_manager):
        """Prueba limpiar todas las tareas."""
        task_manager.add_task("Tarea 1")
        task_manager.add_task("Tarea 2")
        task_manager.clear_all_tasks()

        assert len(task_manager.get_all_tasks()) == 0

    def test_multiple_operations(self, task_manager):
        """Prueba múltiples operaciones en secuencia."""
        # Agregar tareas
        task_manager.add_task("Tarea 1")
        task_manager.add_task("Tarea 2")
        task_manager.add_task("Tarea 3")

        # Completar una tarea
        task_manager.complete_task(2)

        # Eliminar una tarea
        task_manager.delete_task(1)

        # Verificar estado final
        tasks = task_manager.get_all_tasks()
        assert len(tasks) == 2

        pending = task_manager.get_pending_tasks()
        assert len(pending) == 1

        completed = task_manager.get_completed_tasks()
        assert len(completed) == 1
