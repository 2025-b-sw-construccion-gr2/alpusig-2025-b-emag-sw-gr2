# Guía de Pull Requests y Revisiones

Este documento explica el flujo de trabajo para contribuir al proyecto usando Pull Requests.

## 📋 Flujo de Trabajo

### 1. Estructura de Ramas

```
main            # Rama principal de producción
  └── develop   # Rama de desarrollo
        └── feature/*  # Ramas de funcionalidades
```

### 2. Crear una Nueva Funcionalidad

#### Paso 1: Sincronizar con develop
```bash
git checkout develop
git pull origin develop
```

#### Paso 2: Crear rama feature
```bash
git checkout -b feature/nombre-descriptivo
```

**Convención de nombres:**
- `feature/agregar-validaciones`
- `feature/mejorar-tests`
- `feature/actualizar-docs`

#### Paso 3: Hacer cambios
```bash
# Editar archivos
# ...

# Verificar calidad antes de commit
flake8 src/
black --check .
pytest tests/ -v
```

#### Paso 4: Commit
```bash
git add .
git commit -m "tipo: descripción breve"
```

**Tipos de commit:**
- `feat:` nueva funcionalidad
- `fix:` corrección de bug
- `docs:` cambios en documentación
- `test:` agregar o modificar tests
- `refactor:` refactorización de código
- `style:` cambios de formato

#### Paso 5: Push
```bash
git push -u origin feature/nombre-descriptivo
```

### 3. Crear Pull Request

#### En GitHub:

1. **Ir a la página del repositorio**
   - URL: https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2

2. **Hacer clic en "Pull requests" > "New pull request"**

3. **Configurar el PR:**
   - **Base:** `develop` (rama destino)
   - **Compare:** `feature/tu-rama` (rama origen)

4. **Completar información:**
   ```markdown
   ## Descripción
   Breve descripción de los cambios realizados
   
   ## Cambios realizados
   - Item 1
   - Item 2
   
   ## Testing
   - [ ] Todos los tests pasan
   - [ ] Linter sin errores
   - [ ] Formato verificado
   
   ## Capturas (opcional)
   [Si aplica]
   ```

5. **Asignar revisores:**
   - Seleccionar al menos 1 compañero como reviewer

6. **Crear el Pull Request**

### 4. Revisión de Código

#### Como Revisor:

1. **Ir al Pull Request asignado**

2. **Revisar los cambios:**
   - Ver archivos modificados
   - Leer el código línea por línea
   - Verificar que el pipeline CI/CD pase ✅

3. **Comentar si es necesario:**
   - Hacer clic en la línea específica
   - Agregar comentario constructivo
   - Sugerir mejoras

4. **Aprobar o Solicitar Cambios:**
   - **Approve:** Si todo está correcto
   - **Request changes:** Si necesita modificaciones
   - **Comment:** Solo comentarios sin bloquear

#### Como Autor del PR:

1. **Responder a comentarios**

2. **Hacer cambios solicitados:**
   ```bash
   # En la misma rama feature
   git add .
   git commit -m "fix: corregir observaciones del review"
   git push
   ```

3. **El PR se actualiza automáticamente**

### 5. Merge del Pull Request

Una vez aprobado:

1. **Verificar que el pipeline esté ✅**

2. **Hacer merge:**
   - Opción 1: **Merge commit** (recomendado)
   - Opción 2: **Squash and merge** (simplifica historial)

3. **Eliminar la rama feature** (opcional pero recomendado)

4. **Actualizar rama local:**
   ```bash
   git checkout develop
   git pull origin develop
   ```

## ✅ Checklist Pre-PR

Antes de crear un Pull Request, asegúrate de:

- [ ] El código pasa `flake8 src/`
- [ ] El código está formateado con `black .`
- [ ] Todos los tests pasan `pytest tests/ -v`
- [ ] Se agregaron tests para el nuevo código
- [ ] Se actualizó la documentación si es necesario
- [ ] El commit tiene un mensaje descriptivo
- [ ] La rama está actualizada con develop

## 🚫 Errores Comunes a Evitar

1. **❌ Hacer merge sin aprobación**
   - Siempre esperar al menos 1 aprobación

2. **❌ PR muy grande**
   - Mantener PRs pequeños y enfocados
   - Un cambio = Un PR

3. **❌ No probar localmente**
   - Siempre ejecutar linter, format y tests antes de push

4. **❌ Mensajes de commit poco descriptivos**
   - ❌ "cambios"
   - ✅ "feat: agregar validación de títulos vacíos"

5. **❌ Hacer push directo a main o develop**
   - Siempre usar ramas feature

## 📊 Ejemplo de PR Exitoso

### Rama: `feature/agregar-ejemplo-uso`

**Commit:**
```
feat: agregar ejemplo de uso del sistema de gestión de tareas

- Se crea example.py con casos de uso completos
- Demuestra todas las funcionalidades del TaskManager
- Incluye output formateado para mejor visualización
```

**PR Description:**
```markdown
## Descripción
Agrega un archivo de ejemplo que demuestra cómo usar el sistema de gestión de tareas.

## Cambios realizados
- Archivo example.py con casos de uso completos
- Demuestra: agregar, listar, completar y eliminar tareas
- Output con formato visual mejorado

## Testing
- [x] Todos los tests pasan
- [x] Linter sin errores (flake8)
- [x] Formato verificado (black)
- [x] Ejemplo ejecutado correctamente

## Capturas
[Captura del output del ejemplo]
```

**Timeline:**
1. ✅ Pipeline CI/CD pasa automáticamente
2. 👤 Compañero revisa el código
3. ✅ Compañero aprueba el PR
4. 🔀 Merge a develop
5. 🗑️ Eliminación de la rama feature

## 🔗 Enlaces Útiles

- [Repositorio](https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2)
- [Pull Requests](https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2/pulls)
- [GitHub Actions](https://github.com/2025-b-sw-construccion-gr2/alpusig-2025-b-emag-sw-gr2/actions)

---

**Nota:** Esta guía es parte del examen de Construcción y Evolución de Software y debe seguirse para todas las contribuciones al proyecto.
