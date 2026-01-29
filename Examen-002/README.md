# Sistema de Gestión de Tareas

![CI Pipeline](https://github.com/TU_USUARIO/TU_REPO/workflows/CI%20Pipeline/badge.svg)

Sistema sencillo de gestión de tareas desarrollado en Python con integración continua usando GitHub Actions.

## 📋 Características

- ✅ Agregar tareas con título y descripción
- ✅ Listar todas las tareas
- ✅ Marcar tareas como completadas
- ✅ Eliminar tareas
- ✅ Filtrar tareas por estado (pendientes/completadas)
- ✅ Pruebas unitarias completas
- ✅ Pipeline de CI/CD con GitHub Actions

## 🚀 Instalación y Ejecución Local

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Examen-002
   ```

2. **Crear un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

### Ejecutar el Proyecto

Puedes usar el sistema de gestión de tareas de la siguiente manera:

```python
from src.logic import TaskManager

# Crear instancia del gestor
manager = TaskManager()

# Agregar tareas
task1 = manager.add_task("Completar proyecto", "Proyecto de CI/CD")
task2 = manager.add_task("Estudiar Python")

# Listar todas las tareas
print(manager.get_all_tasks())

# Completar una tarea
manager.complete_task(1)

# Obtener tareas pendientes
print(manager.get_pending_tasks())
```

## 🧪 Pruebas

### Ejecutar todas las pruebas:
```bash
pytest tests/ -v
```

### Ejecutar pruebas con reporte de cobertura:
```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

### Generar reporte HTML de cobertura:
```bash
pytest tests/ --cov=src --cov-report=html
```

El reporte se generará en la carpeta `htmlcov/index.html`

## 🔍 Linter y Formato

### Verificar estilo de código con Flake8:
```bash
flake8 src/ --count --show-source --statistics
```

### Verificar formato con Black:
```bash
black --check .
```

### Formatear código automáticamente:
```bash
black .
```

## 🏗️ Build del Proyecto

Para construir el paquete distribuible:

```bash
python -m build
```

Los archivos generados estarán en la carpeta `dist/`

## 🔄 Pipeline de CI/CD

El proyecto utiliza GitHub Actions para automatizar el proceso de integración continua. El pipeline se ejecuta automáticamente en cada push o pull request.

### Estructura del Pipeline

El pipeline consta de **4 jobs** que se ejecutan en secuencia:

#### 1️⃣ **Lint (Flake8)**
- **Propósito:** Verificar la calidad del código y detectar errores de sintaxis
- **Herramienta:** Flake8
- **Qué valida:**
  - Errores de sintaxis
  - Código no utilizado
  - Importaciones incorrectas
  - Convenciones de estilo PEP 8

#### 2️⃣ **Format (Black)**
- **Propósito:** Validar que el código sigue un formato consistente
- **Herramienta:** Black
- **Qué valida:**
  - Formato de código consistente
  - Longitud de líneas
  - Espaciado e indentación
  - Si falla, muestra las diferencias

#### 3️⃣ **Test (Pytest)**
- **Propósito:** Ejecutar todas las pruebas unitarias y generar reporte de cobertura
- **Herramienta:** Pytest + pytest-cov
- **Qué valida:**
  - Todas las pruebas pasan correctamente
  - Cobertura de código (qué porcentaje está probado)
- **Depende de:** Lint y Format deben pasar primero
- **Artefactos generados:** Reporte HTML de cobertura

#### 4️⃣ **Build**
- **Propósito:** Construir el paquete distribuible de Python
- **Herramienta:** setuptools + build
- **Qué valida:**
  - El proyecto se puede empaquetar correctamente
  - Se generan archivos .whl y .tar.gz
- **Depende de:** Test debe pasar primero
- **Artefactos generados:** Paquetes Python en `dist/`

### Flujo de Ejecución

```
┌──────────┐    ┌──────────┐
│   Lint   │    │  Format  │
│ (Flake8) │    │ (Black)  │
└────┬─────┘    └────┬─────┘
     │               │
     └───────┬───────┘
             ▼
      ┌─────────────┐
      │    Test     │
      │  (Pytest)   │
      └──────┬──────┘
             ▼
      ┌─────────────┐
      │    Build    │
      │ (setuptools)│
      └─────────────┘
```

### Triggers del Pipeline

El pipeline se activa en:
- **Push** a las ramas: `main`, `develop`, `feature/*`
- **Pull Requests** hacia: `main`, `develop`

### Ver Resultados del Pipeline

1. Ve a la pestaña **Actions** en GitHub
2. Selecciona el workflow **CI Pipeline**
3. Haz clic en la ejecución específica
4. Revisa los logs de cada job
5. Descarga artefactos (reportes de cobertura y paquetes build)

## 📁 Estructura del Proyecto

```
Examen-002/
├── .github/
│   └── workflows/
│       └── ci.yml              # Configuración del pipeline CI/CD
├── docs/
│   └── PULL_REQUESTS.md        # Guía de Pull Requests
├── src/
│   ├── __init__.py
│   └── logic.py                # Lógica principal del gestor de tareas
├── tests/
│   ├── __init__.py
│   └── test_logic.py           # Pruebas unitarias
├── example.py                  # Ejemplo de uso del sistema
├── requirements.txt            # Dependencias del proyecto
├── setup.py                    # Configuración para build
├── setup.cfg                   # Configuración de herramientas
└── README.md                   # Este archivo
```

## 🔀 Flujo de Trabajo Git

**📖 Para una guía completa, consulta: [docs/PULL_REQUESTS.md](docs/PULL_REQUESTS.md)**

### Crear una nueva funcionalidad:

1. **Crear rama feature:**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/nueva-funcionalidad
   ```

2. **Hacer cambios y commit:**
   ```bash
   # Verificar calidad
   flake8 src/
   black --check .
   pytest tests/ -v
   
   # Commit
   git add .
   git commit -m "feat: descripción de la funcionalidad"
   ```

3. **Subir rama:**
   ```bash
   git push origin feature/nueva-funcionalidad
   ```

4. **Crear Pull Request:**
   - Ve a GitHub
   - Crea un Pull Request desde `feature/nueva-funcionalidad` hacia `develop`
   - Espera que el pipeline pase todas las validaciones
   - Solicita revisión de al menos un compañero
   - Fusiona después de la aprobación

## 📊 Cobertura de Pruebas

El proyecto cuenta con una cobertura completa de pruebas que incluye:

- ✅ Agregar tareas (casos exitosos y errores)
- ✅ Obtener todas las tareas
- ✅ Buscar tareas por ID
- ✅ Completar tareas
- ✅ Eliminar tareas
- ✅ Filtrar tareas por estado
- ✅ Validación de entradas
- ✅ Casos edge

Objetivo: **100% de cobertura**

## 🛠️ Tecnologías Utilizadas

- **Python 3.11+**: Lenguaje de programación
- **Pytest**: Framework de pruebas
- **Flake8**: Linter para validación de código
- **Black**: Formateador automático de código
- **GitHub Actions**: CI/CD
- **setuptools**: Empaquetado de Python

## 👥 Autor

Desarrollado como proyecto de evaluación para el curso de **Construcción y Evolución de Software**.

## 📝 Licencia

MIT License

---

**Nota:** Recuerda actualizar el badge del pipeline con la URL correcta de tu repositorio en GitHub.
