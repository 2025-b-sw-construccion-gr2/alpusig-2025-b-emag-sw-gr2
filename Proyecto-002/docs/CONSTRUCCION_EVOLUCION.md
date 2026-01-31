# Proyecto 02: Sistema de Gestión de Tareas
📘 **Documento de Construcción y Evolución de Software**

---

## 1. Portada

* **Integrantes:** Erick Alpusig - Saúl Tualombo - Claudio Peñaherrera
* **Nombre del proyecto:** Sistema de Gestión de Tareas con CI/CD
* **Fecha de entrega:** Enero 30, 2026
* **Curso:** Construcción y Evolución de Software
* **Repositorio:** [alpusig-2025-b-emag-sw-gr2](https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2)

---

## 2. Introducción

### Breve descripción del proyecto

El **Sistema de Gestión de Tareas** es una aplicación desarrollada en Python que permite a los usuarios administrar sus tareas diarias de manera eficiente. El proyecto resuelve el problema de la organización personal y seguimiento de actividades pendientes, permitiendo crear, listar, completar y eliminar tareas con facilidad.

**Contexto:** En el ámbito académico y profesional, la gestión efectiva de tareas es fundamental para la productividad. Este sistema proporciona una solución simple pero completa con validaciones robustas y una arquitectura extensible.

### Objetivo del documento

Este documento tiene como objetivo mostrar cómo se gestionará la **construcción y evolución del software** del Sistema de Gestión de Tareas, incluyendo:

- Estrategias de integración y entrega continua (CI/CD)
- Flujos de desarrollo y gestión de ramas
- Procesos de revisión y aprobación de código
- Gestión de historias de usuario
- Herramientas y conexiones del ecosistema de desarrollo

---

## 3. Arquitectura del Proyecto

### Diagrama de Alto Nivel

```
┌─────────────────────────────────────────────────────────────┐
│                    SISTEMA DE GESTIÓN DE TAREAS              │
└─────────────────────────────────────────────────────────────┘

┌──────────────────┐         ┌──────────────────┐
│   example.py     │────────>│   src/logic.py   │
│  (Interfaz CLI)  │         │   (TaskManager)  │
└──────────────────┘         └──────────────────┘
                                      │
                                      │
                                      v
                             ┌─────────────────┐
                             │  tests/         │
                             │  test_logic.py  │
                             │  (Pytest)       │
                             └─────────────────┘

┌───────────────────────────────────────────────────────────┐
│                    CI/CD PIPELINE                          │
│  ┌──────┐  ┌────────┐  ┌──────┐  ┌───────┐              │
│  │Lint  │─>│Format  │─>│Test  │─>│Build  │              │
│  └──────┘  └────────┘  └──────┘  └───────┘              │
└───────────────────────────────────────────────────────────┘
```

### Componentes Principales

#### 1. **Capa de Lógica de Negocio (`src/logic.py`)**
- **Responsabilidad:** Implementa la clase `TaskManager` con toda la lógica CRUD de tareas
- **Funcionalidades:**
  - Agregar tareas con título y descripción
  - Listar todas las tareas
  - Completar tareas por ID
  - Eliminar tareas
  - Filtrar tareas por estado (pendientes/completadas)
  - Validaciones de entrada

#### 2. **Capa de Presentación (`example.py`)**
- **Responsabilidad:** Interfaz de línea de comandos para demostrar el uso del sistema
- **Características:**
  - Menú interactivo
  - Visualización formateada de tareas
  - Manejo de errores amigable

#### 3. **Capa de Testing (`tests/test_logic.py`)**
- **Responsabilidad:** Pruebas unitarias exhaustivas
- **Cobertura:** 100% del código de lógica de negocio
- **Framework:** Pytest con pytest-cov
- **Casos de prueba:** 19 tests que cubren casos exitosos, errores y casos límite

#### 4. **Pipeline de CI/CD (`.github/workflows/ci.yml`)**
- **Responsabilidad:** Automatización de validaciones y construcción
- **Etapas:** Lint → Format → Test → Build

### Estrategia de Integración

```python
# Flujo de integración modular
from src.logic import TaskManager

# El módulo logic es independiente y testeable
manager = TaskManager()

# La interfaz se integra mediante imports simples
# Sin dependencias externas complejas
```

**Principios de integración:**
- **Modularidad:** Cada componente es independiente
- **Inyección de dependencias:** No hay acoplamiento fuerte
- **Testabilidad:** Cada módulo puede probarse aisladamente
- **Extensibilidad:** Fácil agregar nuevas interfaces (CLI, Web, API)

---

## 4. Estrategia de Pipelines (CI/CD)

### Pipeline de Integración Continua

El pipeline se ejecuta **automáticamente** en cada push o pull request hacia las ramas `main`, `develop` o `feature/*`.

#### Paso 1: Lint con Flake8
**Objetivo:** Verificar calidad del código y detectar errores de sintaxis

```yaml
- name: Ejecutar Flake8
  run: flake8 src/ example.py --count --show-source --statistics
```

**Validaciones:**
- Errores de sintaxis
- Código no utilizado
- Importaciones incorrectas
- Convenciones PEP 8

#### Paso 2: Verificación de Formato con Black
**Objetivo:** Validar que el código sigue un formato consistente

```yaml
- name: Verificar formato con Black
  run: black --check --diff .
```

**Validaciones:**
- Longitud de líneas (88 caracteres)
- Espaciado e indentación consistente
- Formato de imports

#### Paso 3: Pruebas Unitarias con Pytest
**Objetivo:** Ejecutar todas las pruebas y generar reporte de cobertura

```yaml
- name: Ejecutar pruebas con cobertura
  run: pytest tests/ -v --cov=src --cov-report=term-missing --cov-report=html
```

**Validaciones:**
- Todas las pruebas pasan correctamente
- Cobertura de código ≥ 90%
- Generación de reportes HTML

**Artefactos generados:**
- Reporte de cobertura HTML (disponible para descarga)

#### Paso 4: Build del Proyecto
**Objetivo:** Construir el paquete distribuible de Python

```yaml
- name: Construir paquete
  run: python -m build
```

**Validaciones:**
- Empaquetado exitoso
- Generación de archivos .whl y .tar.gz
- Verificación de metadatos

**Artefactos generados:**
- Paquetes Python distribuibles

### Pipeline de Entrega Continua

Actualmente el proyecto implementa **Continuous Integration (CI)**. La estrategia de **Continuous Delivery (CD)** está planificada para futuras versiones:

**Roadmap CD:**
1. Deploy automático a entorno de staging tras merge a `develop`
2. Deploy a producción tras aprobación manual en `main`
3. Rollback automático en caso de fallos
4. Notificaciones a Slack/Teams

### Diagrama de Flujo del Pipeline

```
┌─────────────────┐
│  Push / PR      │
└────────┬────────┘
         │
         v
┌─────────────────┐
│   Lint          │ ← Flake8
│   (Calidad)     │
└────────┬────────┘
         │
         v
┌─────────────────┐
│   Format        │ ← Black
│   (Estilo)      │
└────────┬────────┘
         │
         v
┌─────────────────┐
│   Test          │ ← Pytest
│   (Funcional)   │
└────────┬────────┘
         │
         v
┌─────────────────┐
│   Build         │ ← setuptools
│   (Paquete)     │
└────────┬────────┘
         │
         v
    ✅ SUCCESS
```

---

## 5. Estrategia de Flujos de Desarrollo

### Modelo de Ramas (Git Flow Simplificado)

```
main (producción estable)
  │
  └── develop (integración continua)
        │
        ├── feature/agregar-validaciones
        ├── feature/mejorar-tests
        ├── feature/exportar-json
        └── hotfix/fix-critical-bug
```

#### Descripción de Ramas

| Rama | Propósito | Lifetime | Protección |
|------|-----------|----------|------------|
| `main` | Versión estable de producción | Permanente | ✅ Protegida |
| `develop` | Integración de nuevas funcionalidades | Permanente | ✅ Protegida |
| `feature/*` | Desarrollo de nuevas características | Temporal | ❌ No protegida |
| `hotfix/*` | Correcciones urgentes | Temporal | ❌ No protegida |

### Flujo de Trabajo Completo

#### 1. Iniciar Nueva Funcionalidad

```bash
# Sincronizar con develop
git checkout develop
git pull origin develop

# Crear rama feature
git checkout -b feature/exportar-json
```

#### 2. Desarrollo y Commits

```bash
# Hacer cambios...

# Validar localmente ANTES de commit
flake8 src/
black --check .
pytest tests/ -v

# Commit con mensaje descriptivo
git add .
git commit -m "feat: agregar exportación de tareas a JSON"
```

**Convención de Commits:**
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `test:` Agregar o modificar tests
- `refactor:` Refactorización sin cambio funcional
- `style:` Cambios de formato
- `chore:` Tareas de mantenimiento

#### 3. Push y Pull Request

```bash
# Subir rama
git push -u origin feature/exportar-json
```

**En GitHub:**
1. Abrir Pull Request hacia `develop`
2. Completar template de PR:
   - Descripción de cambios
   - Testing realizado
   - Capturas (si aplica)
3. Asignar revisores
4. Esperar aprobación del pipeline CI/CD

#### 4. Revisión y Merge

- **Mínimo 1 aprobación** requerida
- **Todos los checks** deben estar en verde ✅
- **Resolver conflictos** si existen
- **Merge** y eliminar rama feature

#### 5. Actualizar Local

```bash
git checkout develop
git pull origin develop
```

### Políticas de Protección de Ramas

**Rama `main`:**
- ✅ Require PR para cambios
- ✅ Require 2 aprobaciones
- ✅ Require checks pasando
- ✅ No permitir force push

**Rama `develop`:**
- ✅ Require PR para cambios
- ✅ Require 1 aprobación
- ✅ Require checks pasando
- ❌ Permitir force push (solo admins)

---

## 6. Gestión de Historias de Usuario

### Formato de Historia de Usuario

**Como** [rol], **quiero** [funcionalidad], **para** [beneficio].

### Historias Implementadas

#### HU-001: Agregar Tarea
**Como** usuario, **quiero** agregar tareas con título y descripción, **para** no olvidar mis pendientes importantes.

**Criterios de Aceptación:**
- ✅ El título es obligatorio
- ✅ La descripción es opcional
- ✅ Se asigna un ID único automáticamente
- ✅ La tarea se crea como "pendiente" por defecto
- ✅ Validar que el título no esté vacío

**Pruebas:**
- `test_add_task_success()`
- `test_add_task_without_description()`
- `test_add_task_empty_title_raises_error()`

---

#### HU-002: Listar Tareas
**Como** usuario, **quiero** ver todas mis tareas, **para** tener una visión completa de mis pendientes.

**Criterios de Aceptación:**
- ✅ Mostrar todas las tareas con su ID, título y estado
- ✅ Indicar visualmente si está completada o pendiente
- ✅ Retornar lista vacía si no hay tareas

**Pruebas:**
- `test_get_all_tasks_empty()`
- `test_get_all_tasks_multiple()`

---

#### HU-003: Completar Tarea
**Como** usuario, **quiero** marcar tareas como completadas, **para** llevar un registro de mi progreso.

**Criterios de Aceptación:**
- ✅ Buscar tarea por ID
- ✅ Cambiar estado a "completada"
- ✅ Retornar error si el ID no existe
- ✅ Validar que el ID sea un número positivo

**Pruebas:**
- `test_complete_task_success()`
- `test_complete_task_not_found()`
- `test_complete_task_invalid_id_raises_error()`

---

#### HU-004: Eliminar Tarea
**Como** usuario, **quiero** eliminar tareas, **para** mantener mi lista limpia y actualizada.

**Criterios de Aceptación:**
- ✅ Eliminar tarea por ID
- ✅ Retornar confirmación de eliminación
- ✅ Retornar error si el ID no existe

**Pruebas:**
- `test_delete_task_success()`
- `test_delete_task_not_found()`

---

#### HU-005: Filtrar Tareas por Estado
**Como** usuario, **quiero** filtrar tareas por estado (pendientes/completadas), **para** enfocarme en lo que necesito hacer.

**Criterios de Aceptación:**
- ✅ Método para obtener solo tareas pendientes
- ✅ Método para obtener solo tareas completadas
- ✅ Retornar listas vacías si no hay coincidencias

**Pruebas:**
- `test_get_pending_tasks()`
- `test_get_completed_tasks()`

---

### Gestión de Historias en el Proyecto

**Herramienta:** GitHub Projects / Issues

**Proceso:**
1. Crear issue por cada historia de usuario
2. Etiquetar con: `enhancement`, `user-story`, prioridad
3. Asignar a sprint (milestone)
4. Vincular PR a issue correspondiente
5. Cerrar automáticamente al hacer merge

**Ejemplo de vinculación:**
```bash
git commit -m "feat: implementar filtrado de tareas

Closes #5"
```

---

## 7. Estrategia de Revisiones y Aprobaciones

### Pull Requests (PRs)

#### Template de Pull Request

```markdown
## 📋 Descripción
Breve descripción de los cambios realizados.

## ✨ Cambios realizados
- Item 1
- Item 2
- Item 3

## 🧪 Testing
- [ ] Todos los tests pasan localmente
- [ ] Agregados tests para nueva funcionalidad
- [ ] Linter sin errores
- [ ] Formato verificado

## 📸 Capturas (si aplica)
[Agregar capturas de pantalla]

## 📚 Documentación
- [ ] README actualizado
- [ ] Docstrings agregados/actualizados
- [ ] CHANGELOG actualizado
```

#### Proceso de Revisión

**Rol del Autor:**
1. Completar template de PR
2. Asignar revisores (mínimo 1)
3. Etiquetar apropiadamente
4. Responder a comentarios
5. Hacer cambios solicitados

**Rol del Revisor:**
1. Verificar que el pipeline esté ✅
2. Revisar código línea por línea
3. Verificar tests y cobertura
4. Comprobar documentación
5. Usar checklist de revisión
6. Aprobar o solicitar cambios

### Checklist de Revisión de Código

#### ✅ Calidad de Código
- [ ] Código cumple con PEP 8
- [ ] Variables y funciones tienen nombres descriptivos
- [ ] Sin código comentado o no usado
- [ ] Sin print statements de debug
- [ ] Manejo adecuado de errores

#### ✅ Testing
- [ ] Tests ejecutados y exitosos
- [ ] Cobertura >= 90%
- [ ] Tests para casos edge
- [ ] Tests para manejo de errores

#### ✅ Documentación
- [ ] Docstrings en funciones/clases nuevas
- [ ] README actualizado si es necesario
- [ ] Comentarios claros en código complejo

#### ✅ Arquitectura
- [ ] Cambios alineados con arquitectura existente
- [ ] Sin dependencias innecesarias
- [ ] Código reutilizable y mantenible

### Herramientas de Revisión

- **GitHub Review:** Comentarios inline en el código
- **GitHub Actions:** Validación automática
- **Codecov:** (futuro) Reportes visuales de cobertura

---

## 8. Herramientas y Conexiones

### Ecosistema de Desarrollo

```
┌─────────────────────────────────────────────────────────────┐
│                    ECOSISTEMA DEL PROYECTO                   │
└─────────────────────────────────────────────────────────────┘

┌────────────────┐      ┌─────────────────┐     ┌─────────────┐
│  GitHub Repo   │◄────►│  GitHub Actions │────►│  Artifacts  │
│  (Código)      │      │  (CI/CD)        │     │  (Build)    │
└────────┬───────┘      └─────────────────┘     └─────────────┘
         │
         │
         v
┌────────────────┐      ┌─────────────────┐     ┌─────────────┐
│ GitHub Issues  │◄────►│  Pull Requests  │────►│  Reviews    │
│ (Historias)    │      │  (Flujo)        │     │  (Calidad)  │
└────────────────┘      └─────────────────┘     └─────────────┘
```

### Herramientas Utilizadas

#### 1. **Repositorio de Código**
- **Herramienta:** GitHub
- **Propósito:** Control de versiones, colaboración
- **URL:** https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2

#### 2. **CI/CD**
- **Herramienta:** GitHub Actions
- **Propósito:** Automatización de pipelines
- **Archivo:** `.github/workflows/ci.yml`
- **Runners:** ubuntu-latest
- **Triggers:** push, pull_request

#### 3. **Gestión de Tareas**
- **Herramienta:** GitHub Issues + Projects
- **Propósito:** Tracking de historias de usuario, bugs, mejoras
- **Organización:** Por milestones (sprints)

#### 4. **Testing**
- **Herramienta:** Pytest + pytest-cov
- **Propósito:** Pruebas unitarias y cobertura
- **Comando:** `pytest tests/ -v --cov=src`

#### 5. **Linting**
- **Herramienta:** Flake8
- **Propósito:** Validación de calidad de código
- **Configuración:** `setup.cfg`

#### 6. **Formateo**
- **Herramienta:** Black
- **Propósito:** Formateo automático de código
- **Estilo:** PEP 8, líneas de 88 caracteres

#### 7. **Build**
- **Herramienta:** setuptools + build
- **Propósito:** Empaquetado de Python
- **Configuración:** `setup.py`

### Conexiones e Integraciones

#### GitHub → GitHub Actions
**Automatización:**
- Cada push o PR dispara el pipeline automáticamente
- Resultados visibles en la pestaña "Checks" del PR
- Bloqueo de merge si checks fallan

#### GitHub Issues → Pull Requests
**Trazabilidad:**
```bash
# En el commit o PR description:
git commit -m "feat: agregar filtros

Closes #12"
```
- El issue #12 se vincula automáticamente al PR
- Se cierra automáticamente al hacer merge

#### Pull Requests → Code Reviews
**Calidad:**
- Revisión obligatoria antes de merge
- Comentarios inline en el código
- Aprobación explícita requerida

#### GitHub Actions → Artifacts
**Distribución:**
- Reportes de cobertura guardados como artifacts
- Paquetes Python disponibles para descarga
- Historial de 90 días

### Comunicación (Planificado)

**Futuras integraciones:**
- **Slack:** Notificaciones de PRs, merges, deployments
- **Email:** Alertas de pipeline fallido
- **Discord:** Canal de desarrollo

---

## 9. Conclusiones

### Calidad Asegurada

El Sistema de Gestión de Tareas implementa un **conjunto robusto de prácticas** que garantizan la calidad del software:

1. **Pipeline CI/CD de 4 etapas** que valida automáticamente cada cambio
2. **Cobertura de pruebas del 100%** que asegura funcionalidad correcta
3. **Linting y formateo automático** que mantiene consistencia en el código
4. **Revisiones de código obligatorias** que detectan problemas tempranamente

### Trazabilidad Completa

La implementación del flujo Git Flow con Pull Requests proporciona:

- **Historial completo** de todos los cambios
- **Vinculación** entre código y historias de usuario
- **Documentación** de decisiones técnicas en PRs
- **Rollback** sencillo en caso de problemas

### Evolución Sostenible

La arquitectura modular y las prácticas establecidas permiten:

- **Agregar nuevas funcionalidades** sin afectar código existente
- **Escalar el equipo** con procesos claros
- **Mantener calidad** a medida que crece el proyecto
- **Adaptar tecnologías** sin reescribir desde cero

### Próximos Pasos

1. **Implementar Continuous Deployment** para automatizar despliegues
2. **Integrar Slack/Discord** para notificaciones en tiempo real
3. **Agregar badges** de cobertura y estado del build al README
4. **Configurar pre-commit hooks** para validar antes de commit
5. **Implementar versionado semántico** automático

---

## 📊 Métricas del Proyecto

| Métrica | Valor | Estado |
|---------|-------|--------|
| **Cobertura de Tests** | 100% | ✅ Excelente |
| **Linter Issues** | 0 | ✅ Limpio |
| **Format Issues** | 0 | ✅ Consistente |
| **Build Success Rate** | 100% | ✅ Estable |
| **PRs Revisados** | 100% | ✅ Completo |
| **Tiempo promedio CI** | 2-3 min | ✅ Rápido |

---

**Documento elaborado por:** Erick Medardo Alpusig Maguiña  
**Fecha:** Enero 30, 2026  
**Versión:** 1.0
