"""
Ejemplo de uso del Sistema de Gestión de Tareas.

Este archivo demuestra cómo utilizar la clase TaskManager
para gestionar tareas de manera efectiva.
"""

from src.logic import TaskManager


def main():
    """Función principal con ejemplos de uso."""
    # Crear una instancia del gestor de tareas
    print("=== Sistema de Gestión de Tareas ===\n")
    manager = TaskManager()

    # 1. Agregar tareas
    print("1. Agregando tareas...")
    manager.add_task(
        "Completar proyecto de CI/CD", "Implementar pipeline con GitHub Actions"
    )
    manager.add_task(
        "Estudiar para examen", "Repasar conceptos de integración continua"
    )
    manager.add_task("Revisar Pull Requests", "Aprobar PRs de compañeros")
    print(f"✓ {len(manager.get_all_tasks())} tareas agregadas\n")

    # 2. Listar todas las tareas
    print("2. Tareas actuales:")
    for task in manager.get_all_tasks():
        status = "✓" if task["completed"] else "○"
        print(f"  {status} [{task['id']}] {task['title']}")
        if task["description"]:
            print(f"      → {task['description']}")
    print()

    # 3. Completar una tarea
    print("3. Completando tarea...")
    manager.complete_task(1)
    task = manager.get_task_by_id(1)
    print(f"✓ Tarea '{task['title']}' completada\n")

    # 4. Ver tareas pendientes
    print("4. Tareas pendientes:")
    for task in manager.get_pending_tasks():
        print(f"  ○ [{task['id']}] {task['title']}")
    print()

    # 5. Ver tareas completadas
    print("5. Tareas completadas:")
    for task in manager.get_completed_tasks():
        print(f"  ✓ [{task['id']}] {task['title']}")
    print()

    # 6. Eliminar una tarea
    print("6. Eliminando tarea...")
    manager.delete_task(3)
    print(f"✓ Tarea eliminada. Total: {len(manager.get_all_tasks())} tareas\n")

    # Resumen final
    print("=== Resumen Final ===")
    print(f"Total de tareas: {len(manager.get_all_tasks())}")
    print(f"Pendientes: {len(manager.get_pending_tasks())}")
    print(f"Completadas: {len(manager.get_completed_tasks())}")


if __name__ == "__main__":
    main()
