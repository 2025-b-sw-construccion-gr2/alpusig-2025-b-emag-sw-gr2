# Sistema de Gestión de Tareas - Proyecto 02

![CI Pipeline](https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2/workflows/CI%20Pipeline/badge.svg)

**Proyecto 02 - Construcción y Evolución de Software**

Sistema sencillo de gestión de tareas desarrollado en Python que demuestra la implementación completa de un proceso de desarrollo de software profesional, incluyendo arquitectura documentada, pipeline de CI/CD, gestión de historias de usuario, flujos de trabajo con Git, y estrategias de revisión de código.

**Integrantes:** Erick Alpusig - Saúl Tualombo - Claudio Peñaherrera  
**Fecha:** Enero 2026  
**Repositorio:** [alpusig-2025-b-emag-sw-gr2](https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2/edit/develop/Proyecto-002)

---

### Objetivo del documento

Este documento tiene como objetivo mostrar cómo se gestionará la **construcción y evolución del software** del Sistema de Gestión de Tareas, incluyendo:

- Estrategias de integración y entrega continua (CI/CD)
- Flujos de desarrollo y gestión de ramas
- Procesos de revisión y aprobación de código
- Gestión de historias de usuario
- Herramientas y conexiones del ecosistema de desarrollo

---

## 📚 Documentación Principal

### 📖 **[Documento de Construcción y Evolución de Software](docs/CONSTRUCCION_EVOLUCION.md)** ⭐

**Este es el documento central del proyecto** que incluye:

#### 1. **Portada**
- Información del proyecto y equipo
- Contexto y objetivos

#### 2. **Introducción**
- Descripción del problema a resolver
- Objetivos del documento

#### 3. **Arquitectura del Proyecto**
- Diagramas de componentes
- Estrategia de integración modular
- Descripción de capas (Lógica, Presentación, Testing, CI/CD)

#### 4. **Estrategia de Pipelines (CI/CD)**
- Pipeline de Integración Continua (4 etapas)
- Diagrama de flujo del pipeline
- Roadmap de Continuous Delivery

#### 5. **Flujos de Desarrollo**
- Modelo de ramas (Git Flow)
- Convenciones de commits
- Políticas de protección de ramas

#### 6. **Gestión de Historias de Usuario**
- 5 historias de usuario completas
- Criterios de aceptación
- Vinculación con tests

#### 7. **Estrategia de Revisiones y Aprobaciones**
- Template de Pull Requests
- Checklist de revisión
- Proceso de aprobación

#### 8. **Herramientas y Conexiones**
- Ecosistema de desarrollo
- Integraciones (GitHub, Actions, Issues)
- Diagramas de conexiones

#### 9. **Conclusiones**
- Calidad asegurada
- Trazabilidad completa
- Evolución sostenible
- Métricas del proyecto

### 📖 Documentación Complementaria

- **[Guía de Pull Requests](docs/PULL_REQUESTS.md)** - Flujo detallado de trabajo con PRs
- **[Código de Ejemplo](example.py)** - Demostración del sistema funcionando

---

## 🏗️ Arquitectura Implementada

```
┌─────────────────────────────────────────────────────────────┐
│             SISTEMA DE GESTIÓN DE TAREAS                     │
└─────────────────────────────────────────────────────────────┘

┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  example.py  │───►│  src/logic.py│◄───│tests/test_   │
│  (CLI)       │    │  (TaskMgr)   │    │  logic.py    │
└──────────────┘    └──────────────┘    └──────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │   CI/CD      │
                    │   Pipeline   │
                    └──────────────┘
```

**Componentes:**
- **src/logic.py**: Lógica de negocio (TaskManager)
- **example.py**: Interfaz CLI de ejemplo
- **tests/**: Suite completa de pruebas (100% cobertura)
- **.github/workflows/**: Pipeline automatizado

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
   git clone https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2.git
   cd alpusig-2025-b-emag-sw-gr2/Proyecto-002
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

**Ver detalles completos en:** [Sección 4 del Documento Principal](docs/CONSTRUCCION_EVOLUCION.md#4-estrategia-de-pipelines-cicd)

El proyecto implementa un pipeline de 4 etapas que se ejecuta automáticamente en cada cambio:

### Flujo del Pipeline

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
Proyecto-002/
├── .github/
│   └── workflows/
│       └── ci.yml              # Configuración del pipeline CI/CD
├── docs/
│   ├── CONSTRUCCION_EVOLUCION.md  # 📘 Documento principal
│   └── PULL_REQUESTS.md        # Guía de Pull Requests
├── src/
│   ├── __init__.py
│   └── logic.py                # Lógica principal del gestor de tareas
├── tests/
│   ├── __init__.py
│   └── test_logic.py           # Pruebas unitarias (19 tests)
├── example.py                  # Ejemplo de uso del sistema
├── requirements.txt            # Dependencias del proyecto
├── setup.py                    # Configuración para build
├── setup.cfg                   # Configuración de herramientas
└── README.md                   # Este archivo
```

---

## 🎯 Criterios de Evaluación Cumplidos

Este proyecto cumple con todos los requisitos establecidos:

### ✅ Documentación Completa
- ✅ Portada con información del proyecto
- ✅ Introducción y contexto
- ✅ Arquitectura con diagramas
- ✅ Estrategia de pipelines documentada
- ✅ Flujos de desarrollo explicados
- ✅ Historias de usuario gestionadas (5 HU)
- ✅ Estrategia de revisiones establecida
- ✅ Herramientas y conexiones descritas
- ✅ Conclusiones y métricas

### ✅ Implementación Técnica
- ✅ Pipeline CI/CD funcionando (4 etapas)
- ✅ Tests unitarios con 100% cobertura
- ✅ Linter y formateo automático
- ✅ Flujo Git con feature branches
- ✅ Pull Requests con revisiones
- ✅ Build del proyecto exitoso

### ✅ Evidencias
- ✅ Capturas de pipeline exitoso
- ✅ Comentarios de revisión documentados
- ✅ PR aprobado y fusionado
- ✅ Historial de GitHub Actions

---

## 📊 Métricas del Proyecto

| Aspecto | Resultado | Estado |
|---------|-----------|--------|
| **Cobertura de Tests** | 100% | ✅ Excelente |
| **Linter Issues** | 0 | ✅ Limpio |
| **Format Issues** | 0 | ✅ Consistente |
| **Build Success** | 100% | ✅ Estable |
| **PRs Revisados** | 100% | ✅ Completo |
| **Historias de Usuario** | 5 implementadas | ✅ Documentadas |
| **Pipeline Stages** | 4 etapas | ✅ Completo |

---

## 🔗 Enlaces Importantes

- **[Documento Principal](docs/CONSTRUCCION_EVOLUCION.md)** - Documento completo de construcción y evolución
- **[Guía de PRs](docs/PULL_REQUESTS.md)** - Proceso de Pull Requests
- **[Repositorio](https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2)** - Código fuente
- **[GitHub Actions](https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2/actions)** - Historial de CI/CD

## 🔀 Flujo de Trabajo Git Flow

**📖 Ver documentación completa:** [Sección 5 del Documento Principal](docs/CONSTRUCCION_EVOLUCION.md#5-flujos-de-desarrollo-git-flow)

Este proyecto implementa **Git Flow** con las siguientes ramas:

| Rama | Propósito | Vida útil |
|------|-----------|-----------|
| `main` | Producción estable | Permanente |
| `develop` | Integración de cambios | Permanente |
| `feature/*` | Nueva funcionalidad | Temporal |
| `hotfix/*` | Correcciones urgentes | Temporal |

### Crear una nueva funcionalidad:

1. **Crear rama feature desde develop:**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/nombre-funcionalidad
   ```

2. **Desarrollar y validar cambios:**
   ```bash
   # Verificar calidad antes de commit
   flake8 src/
   black --check .
   pytest tests/ -v --cov=src
   
   # Commit con mensaje descriptivo
   git add .
   git commit -m "feat: descripción de la funcionalidad"
   ```

3. **Subir rama y crear Pull Request:**
   ```bash
   git push origin feature/nombre-funcionalidad
   ```
   - Ir a GitHub y crear PR hacia `develop`
   - El pipeline CI/CD se ejecutará automáticamente
   - Solicitar revisión de al menos un compañero
   - Fusionar después de aprobación y checks verdes

**Guía de Pull Requests:** [docs/PULL_REQUESTS.md](docs/PULL_REQUESTS.md)

## 📊 Cobertura de Pruebas

**Objetivo:** 100% de cobertura  
**Resultado:** ✅ 100% alcanzado  

El proyecto cuenta con **19 pruebas unitarias** que cubren:

- ✅ Agregar tareas (casos exitosos y validación de errores)
- ✅ Obtener todas las tareas (lista completa y copias inmutables)
- ✅ Buscar tareas por ID (encontradas y no encontradas)
- ✅ Completar tareas (éxito y errores)
- ✅ Eliminar tareas (éxito y errores)
- ✅ Filtrar por estado (pendientes y completadas)
- ✅ Validación de entradas (títulos vacíos, IDs inválidos)
- ✅ Casos edge (listas vacías, operaciones múltiples)

**Ver implementación:** [tests/test_logic.py](tests/test_logic.py)

## � Evidencias del Pipeline y Pull Requests

### ✅ Pipeline CI/CD Exitoso

**Todos los checks pasaron correctamente:**

![Checks Pasando](https://github.com/ElErick-MG/mi-sitio/blob/dc91d990e6de4053af9ac72eac0f2a1368949f6b/img/Test-Pasados.png)

*Captura mostrando los 4 jobs completados exitosamente: Lint, Format, Test y Build.*

---

### 💬 Revisión de Código

**Comentarios en el Pull Request:**

![Revisión de Código](https://github.com/ElErick-MG/mi-sitio/blob/dc91d990e6de4053af9ac72eac0f2a1368949f6b/img/comentario1.png)
![Revisión de Código2](https://github.com/ElErick-MG/mi-sitio/blob/dc91d990e6de4053af9ac72eac0f2a1368949f6b/img/comentario2.png)

*Captura mostrando los comentarios realizados durante la revisión del código en archivos como example.py y PULL_REQUESTS.md.*

---

### 🎉 Pull Request Aprobado y Fusionado

**Merge exitoso hacia develop:**

![PR Aprobado](https://github.com/ElErick-MG/mi-sitio/blob/dc91d990e6de4053af9ac72eac0f2a1368949f6b/img/PULL-ACCEPTED.png)

*Captura del Pull Request aprobado sin conflictos y fusionado exitosamente a la rama develop.*

---

### 📊 Resumen de Ejecuciones del Pipeline

**GitHub Actions - Historial:**

![Historial Actions](https://github.com/ElErick-MG/mi-sitio/blob/dc91d990e6de4053af9ac72eac0f2a1368949f6b/img/ACTION-COMPLETO.png)

---

## 📋 Gestión de Historias de Usuario

**📖 Ver detalle completo:** [Sección 6 del Documento Principal](docs/CONSTRUCCION_EVOLUCION.md#6-gestión-de-historias-de-usuario)

El proyecto incluye **5 Historias de Usuario** completas:

| ID | Historia | Tests Relacionados | Estado |
|----|----------|-------------------|--------|
| HU-001 | Crear nueva tarea | `test_add_task`, `test_add_task_with_description` | ✅ Implementada |
| HU-002 | Visualizar tareas | `test_get_all_tasks`, `test_get_all_tasks_empty` | ✅ Implementada |
| HU-003 | Marcar tarea completada | `test_complete_task`, `test_complete_nonexistent_task` | ✅ Implementada |
| HU-004 | Eliminar tarea | `test_delete_task`, `test_delete_nonexistent_task` | ✅ Implementada |
| HU-005 | Filtrar tareas | `test_get_pending_tasks`, `test_get_completed_tasks` | ✅ Implementada |

Cada historia incluye:
- Criterios de aceptación
- Pruebas unitarias mapeadas
- Definición de Done
- Trazabilidad código-tests

Ejemplo de como crearlas:
![Historia de Usuario HU-001](https://github.com/ElErick-MG/mi-sitio/blob/88ae0a561d03c31c28faeca67b8054020f79f7e8/img/historia_usuario.png).

Tablero de GitHub Issues
![Tablero de GitHub Issues](https://github.com/ElErick-MG/mi-sitio/blob/ad1f87416104939917b5628386e32b9ae719b760/img/issue.png).

---

## 🛠️ Tecnologías Utilizadas

**Ver ecosistema completo:** [Sección 8 del Documento Principal](docs/CONSTRUCCION_EVOLUCION.md#8-herramientas-y-conexiones)

### Core
- **Python 3.11+**: Lenguaje de programación
- **Git**: Control de versiones
- **GitHub**: Plataforma de repositorio y CI/CD

### Testing & Quality
- **Pytest 7.4.0+**: Framework de pruebas con fixtures
- **pytest-cov 4.1.0+**: Medición de cobertura
- **Flake8 6.1.0+**: Análisis estático (PEP 8)
- **Black 23.7.0+**: Formateo automático

### CI/CD & Build
- **GitHub Actions**: Pipeline de integración continua
- **setuptools + build**: Empaquetado de distribuciones
- **ubuntu-latest runners**: Entorno de ejecución del pipeline

---

## 👥 Equipo de Desarrollo

**Integrantes:**
- Erick Medardo Alpusig Maguiña
- Saúl Tualombo
- Claudio Peñaherrera

**Curso:** Construcción y Evolución de Software  
**Período:** 2025-B  
**Grupo:** 2  
**Institución:** [Nombre de la Institución]

---

## 📄 Documentación del Proyecto

Este README proporciona una guía rápida de instalación y uso. Para la documentación completa del proyecto, consulta:

### 📘 [Documento Principal: CONSTRUCCION_EVOLUCION.md](docs/CONSTRUCCION_EVOLUCION.md)

Incluye:
1. Portada del proyecto
2. Introducción y contexto
3. Arquitectura de la solución (diagramas)
4. Estrategia de pipelines CI/CD
5. Flujos de desarrollo (Git Flow)
6. Gestión de historias de usuario
7. Estrategia de revisiones de código
8. Herramientas y conexiones
9. Conclusiones y métricas

### 📝 [Guía de Pull Requests](docs/PULL_REQUESTS.md)
Proceso detallado para crear y revisar Pull Requests.

---

## 🎯 Criterios de Evaluación Cumplidos

Este proyecto cumple con **todos** los requisitos establecidos por el instructor:

### ✅ Documentación Completa (9/9 secciones)
- ✅ Portada con información del proyecto y equipo
- ✅ Introducción con contexto y objetivos
- ✅ Arquitectura documentada con diagramas ASCII
- ✅ Estrategia de pipelines CI/CD explicada (4 etapas)
- ✅ Flujos de desarrollo Git Flow detallados
- ✅ 5 Historias de usuario con criterios de aceptación
- ✅ Estrategia de revisiones de código establecida
- ✅ Herramientas y conexiones del ecosistema
- ✅ Conclusiones con tabla de métricas

### ✅ Implementación Técnica
- ✅ Pipeline CI/CD funcionando (Lint → Format → Test → Build)
- ✅ 19 Tests unitarios con 100% cobertura
- ✅ Linter (Flake8) sin errores
- ✅ Formateo (Black) consistente
- ✅ Git Flow implementado con feature branches
- ✅ Pull Requests con revisiones completas
- ✅ Build exitoso del paquete Python

### ✅ Evidencias
- ✅ Capturas del pipeline exitoso en GitHub Actions
- ✅ Comentarios de revisión en Pull Requests
- ✅ PR aprobado y fusionado a develop
- ✅ Historial de ejecuciones visible

---

## 📝 Licencia

MIT License

---

**🔗 Enlaces Rápidos:**
- [Repositorio GitHub](https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2)
- [GitHub Actions](https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2/actions)
- [Documento Principal](docs/CONSTRUCCION_EVOLUCION.md)
- [Guía de PRs](docs/PULL_REQUESTS.md)
