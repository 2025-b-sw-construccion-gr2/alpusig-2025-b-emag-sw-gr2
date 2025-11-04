# Clase 006 - Taller: Aplicando Principios de Código Limpio en Proyectos Reales

**Repositorio analizado:** [cesaralvrz/recursos-programación](https://github.com/Acadeller/recursos-programacion)  
**Lenguaje:** SQL  
**Estudiante:** Erick Alpusig - Claudio Peñaherrera - Saúl Tualombo  
**Fecha:** 4 de noviembre de 2025

---

## 1️⃣ Introducción

Este taller tiene como objetivo aplicar los principios de **Código Limpio** en código real proveniente de un repositorio público.  
Se busca identificar olores de código, proponer refactorizaciones y justificar cómo dichas mejoras aumentan la mantenibilidad, legibilidad y claridad del software.

---

## 2️⃣ Archivos seleccionados

| Archivo | Ruta en el repositorio | Descripción |
|---|---|---|
| `ClaveUnica.sql` | `/src/` | Identificación del nombre de la columna de la clave única. |
| `DoublyLinkedList.js` | `/src/data-structures/linked-list/doubly-linked-list/DoublyLinkedList.js` | Implementa una lista doblemente enlazada. |
| `DoublyLinkedList.js` | `/src/data-structures/linked-list/doubly-linked-list/DoublyLinkedList.js` | Implementa una lista doblemente enlazada. |

---

## 3️⃣ Análisis del archivo 1: `ClaveUnica.sql`

### Código original
```sql
USE Northwind
GO
DECLARE @key_column sysname
SET @key_column = Col_Name(Object_Id('Categories'),
ObjectProperty(Object_id('Categories'),
'TableFulltextKeyColumn')
)
print @key_column
EXECUTE ('SELECT Description, KEY_TBL.RANK
FROM Categories FT_TBL
INNER JOIN
FreetextTable (Categories, Description,
''How can I make my own beers and ales?'') AS KEY_TBL
ON FT_TBL.'
+ @key_column
+' = KEY_TBL.[KEY]
WHERE KEY_TBL.RANK >= 10
ORDER BY KEY_TBL.RANK DESC
')
GO
```
---

### 🔹 Observaciones según principios de Código Limpio

| Principio | Observación |
|---|---|
| **Nombres significativos** | El nombre `@key_column` es adecuado, pero el script carece de comentarios que indiquen su propósito. |
| **Funciones cortas / consultas claras** | Todo el proceso (declaración, obtención y ejecución dinámica) está en un solo bloque; podría separarse lógicamente. |
| **Responsabilidad única** | Mezcla lógica de metadatos (`ObjectProperty`) con consulta dinámica (`EXECUTE`). |
| **Comentarios** | No existen comentarios que expliquen el objetivo de cada sección. |
| **Legibilidad y formato** | La indentación es inconsistente, lo que dificulta la lectura. |
| **Validaciones** | No se verifica si la tabla o columna existen antes de ejecutar la consulta dinámica. |

---

### 🔹 Olores de código detectados

- **Consulta dinámica compleja** y poco legible.  
- **Dependencia directa** de nombres de tabla sin validación.  
- **Ausencia de control de errores** (si `@key_column` es `NULL`, el EXEC fallará).  
- **Falta de comentarios explicativos.**  
- **Estructura poco modular**, mezcla obtención de datos y ejecución en un solo bloque.  

### 🔹 Propuestas de mejora

| Nº | Mejora | Descripción | Justificación |
|---:|---|---|---|
| 1 | Validar existencia de la tabla | Verificar que `Categories` exista antes de ejecutar. | Evita errores en bases distintas o ausentes. |
| 2 | Validar `@key_column` | Confirmar que la columna de clave única no sea `NULL`. | Previene fallos en ejecución dinámica. |
| 3 | Separar secciones lógicas | Dividir la obtención de la columna y la ejecución del `SELECT`. | Mejora comprensión y mantenimiento. |
| 4 | Añadir comentarios | Explicar el propósito de cada parte del script. | Facilita el entendimiento de otros desarrolladores. |
| 5 | Mejorar formato e indentación | Aplicar sangría coherente y líneas espaciadas. | Incrementa legibilidad. |

### 🔹 Versión refactorizada propuesta

```sql
-- ==============================================
-- Script: ClaveUnica.sql
-- Descripción: Identifica la columna de clave única de la tabla Categories
-- y realiza una búsqueda Full-Text sobre la columna Description.
-- ==============================================

USE Northwind;
GO

DECLARE @table_name sysname = 'Categories';
DECLARE @key_column sysname;

-- ✅ Verificar que la tabla exista
IF OBJECT_ID(@table_name) IS NULL
BEGIN
    PRINT '❌ La tabla especificada no existe.';
    RETURN;
END;

-- ✅ Obtener el nombre de la columna de clave única
SET @key_column = COL_NAME(
    OBJECT_ID(@table_name),
    OBJECTPROPERTY(OBJECT_ID(@table_name), 'TableFulltextKeyColumn')
);

-- ✅ Validar que la clave única se haya obtenido correctamente
IF @key_column IS NULL
BEGIN
    PRINT '❌ No se encontró columna de clave única para la tabla ' + @table_name;
    RETURN;
END;

PRINT '✅ Columna de clave única: ' + @key_column;

-- ✅ Ejecutar consulta dinámica con mejor formato y control
DECLARE @query NVARCHAR(MAX);

SET @query = N'
SELECT 
    FT_TBL.Description, 
    KEY_TBL.RANK
FROM ' + QUOTENAME(@table_name) + N' AS FT_TBL
INNER JOIN FREETEXTTABLE(' + QUOTENAME(@table_name) + N', Description,
    ''How can I make my own beers and ales?'') AS KEY_TBL
ON FT_TBL.' + QUOTENAME(@key_column) + N' = KEY_TBL.[KEY]
WHERE KEY_TBL.RANK >= 10
ORDER BY KEY_TBL.RANK DESC;
';

EXEC sp_executesql @query;
GO

  ```

### 🔹 Conclusión (ClaveUnica.sql)

El script **`ClaveUnica.sql`** cumple su función original, pero su estructura puede mejorarse para aumentar **claridad, seguridad y mantenibilidad**.  
Las mejoras aplicadas (validaciones, comentarios y formato limpio) aseguran que el código sea más **robusto**, **comprensible** y siga los principios de **código limpio y responsabilidad única**.

---

## 4️⃣ Análisis del archivo 2: `DoublyLinkedList.js`

### Código original (simplificado)
```js
  export default class DoublyLinkedList {
    constructor() {
      this.head = null;
      this.tail = null;
    }

    append(value) {
      const newNode = { value, next: null, prev: this.tail };
      if (this.tail) {
        this.tail.next = newNode;
      } else {
        this.head = newNode;
      }
      this.tail = newNode;
      return this;
    }

    prepend(value) {
      const newNode = { value, next: this.head, prev: null };
      if (this.head) {
        this.head.prev = newNode;
      } else {
        this.tail = newNode;
      }
      this.head = newNode;
      return this;
    }

    delete(value) {
      if (!this.head) return null;
      let current = this.head;
      while (current) {
        if (current.value === value) {
          if (current.prev) current.prev.next = current.next;
          if (current.next) current.next.prev = current.prev;
          if (current === this.head) this.head = current.next;
          if (current === this.tail) this.tail = current.prev;
          return current;
        }
        current = current.next;
      }
      return null;
    }
  }
  ```

  ### 🔹 Observaciones según principios de Código Limpio

  | Principio | Observación |
  |---|---|
  | Nombres descriptivos | Correctos en su mayoría (`append`, `prepend`, `delete`). |
  | Responsabilidad única | Cada método cumple un propósito claro, pero puede documentarse mejor. |
  | Evitar repetición | La creación de nodos podría centralizarse en un método auxiliar. |
  | Validaciones | No se validan los valores antes de insertarlos o eliminarlos. |
  | Comentarios | No hay comentarios explicativos sobre el flujo de los enlaces. |

  ### 🔹 Olores de código detectados

  - Código duplicado en la creación de nodos (append y prepend).  
  - Falta de validación de entrada (null, undefined).  
  - Ausencia de documentación sobre cómo se gestionan los enlaces.  
  - No se maneja el caso de eliminar valores inexistentes con mensajes o excepciones.  

  ### 🔹 Propuestas de mejora

  | Nº | Mejora | Descripción | Justificación |
  |---:|---|---|---|
  | 1 | Centralizar creación de nodos | Crear método `createNode(value, prev, next)`. | Evita duplicación. |
  | 2 | Validar valores | Asegurar que `value` no sea `null` o `undefined`. | Previene errores. |
  | 3 | Agregar comentarios | Explicar cómo se enlazan y desenlazan los nodos. | Mejora comprensión. |
  | 4 | Métodos auxiliares | Agregar `isEmpty()`, `size()` o `toArray()`. | Aumenta reutilización y facilita pruebas. |

  ### 🔹 Versión refactorizada propuesta

  ```js
  class DoublyLinkedListNode {
    constructor(value, prev = null, next = null) {
      this.value = value;
      this.prev = prev;
      this.next = next;
    }
  }

  export default class DoublyLinkedList {
    constructor() {
      this.head = null;
      this.tail = null;
      this._size = 0;
    }

    createNode(value, prev = null, next = null) {
      if (value === null || value === undefined) {
        throw new Error('Node value cannot be null or undefined');
      }
      return new DoublyLinkedListNode(value, prev, next);
    }

    append(value) {
      const newNode = this.createNode(value, this.tail);
      if (this.tail) this.tail.next = newNode;
      else this.head = newNode;
      this.tail = newNode;
      this._size++;
      return this;
    }

    prepend(value) {
      const newNode = this.createNode(value, null, this.head);
      if (this.head) this.head.prev = newNode;
      else this.tail = newNode;
      this.head = newNode;
      this._size++;
      return this;
    }

    delete(value) {
      if (!this.head) return null;
      let current = this.head;
      while (current) {
        if (current.value === value) {
          if (current.prev) current.prev.next = current.next;
          if (current.next) current.next.prev = current.prev;
          if (current === this.head) this.head = current.next;
          if (current === this.tail) this.tail = current.prev;
          this._size--;
          return current;
        }
        current = current.next;
      }
      return null;
    }

    isEmpty() {
      return this._size === 0;
    }

    toArray() {
      const elements = [];
      let current = this.head;
      while (current) {
        elements.push(current.value);
        current = current.next;
      }
      return elements;
    }

    size() {
      return this._size;
    }
  }
  ```

  ### 🔹 Conclusión (DoublyLinkedList)

  El archivo `DoublyLinkedList.js` presenta una buena estructura, pero puede mejorarse mediante la centralización de la creación de nodos, validación de valores y agregación de métodos utilitarios.  
  Estas mejoras refuerzan los principios de Código Limpio, favoreciendo la reutilización, modularidad y claridad del código.

  ---

  ## ✅ Conclusión general del taller

  Tras analizar ambos archivos, se evidencia que incluso proyectos bien estructurados pueden beneficiarse de aplicar los principios de Código Limpio. En particular:

  - La modularización y nombres descriptivos facilitan la comprensión.  
  - La validación de datos y comentarios breves previenen errores.  
  - La claridad del flujo lógico reduce la deuda técnica y mejora la mantenibilidad.


  Un código limpio no solo funciona bien: se entiende, se extiende y se mantiene con facilidad.

