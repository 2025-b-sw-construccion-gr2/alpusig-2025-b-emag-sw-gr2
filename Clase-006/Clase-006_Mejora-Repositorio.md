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
| `ClaveUnica.sql` | `/src/sql` | Identificación del nombre de la columna de la clave única. |
| `BúsquedasFechasAccess.sql` | `/src/sql` | Búsquedas con fechas en Access.sql. |
| `SQL_Quick_Reference.sql` | `/src/sql/` | Documento que reúne las principales sentencias SQL con su sintaxis general. |

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
---
### 🔹 Conclusión (ClaveUnica.sql)

El script **`ClaveUnica.sql`** cumple su función original, pero su estructura puede mejorarse para aumentar **claridad, seguridad y mantenibilidad**.  
Las mejoras aplicadas (validaciones, comentarios y formato limpio) aseguran que el código sea más **robusto**, **comprensible** y siga los principios de **código limpio y responsabilidad única**.

---

## 3️⃣ Análisis del archivo 2: `Búsquedas con fechas en Access.sql`

### Código original
```sql
SELECT * FROM vuelos WHERE
DateDiff('y',fechadesde,now())>=0
and DateDiff('y',fechahasta,nom())<=0
```
---
  ### 🔹 Observaciones según principios de Código Limpio
| Principio                               | Observación                                                                                                                                          |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombres significativos**              | Los nombres `fechadesde` y `fechahasta` son comprensibles, pero pueden mejorarse a `fecha_inicio` y `fecha_fin` para mantener coherencia y claridad. |
| **Funciones cortas / consultas claras** | La consulta cumple una sola función, pero el uso de `DateDiff()` hace que la intención sea menos directa y más difícil de leer.                      |
| **Responsabilidad única**               | El código mezcla la lógica de comparación con cálculos innecesarios; debería centrarse solo en evaluar si la fecha actual está dentro del rango.     |
| **Comentarios**                         | No hay comentarios que expliquen el propósito ni el contexto del código, lo que dificulta su mantenimiento.                                          |
| **Legibilidad y formato**               | La sintaxis es correcta, pero el error tipográfico (`nom()` en lugar de `now()`) y la complejidad de la función reducen la claridad.                 |
| **Validaciones**                        | No se contemplan casos de fechas nulas (`NULL`), lo que podría causar resultados inesperados o errores de ejecución.                                 |
---

  ### 🔹 Olores de código detectados

  - Uso innecesario de la función DateDiff() para comparaciones simples.  
  - Error de escritura (nom() en lugar de now()).  
  - Falta de validación ante valores NULL.  
  - Dependencia del idioma o formato regional de las fechas.
  - Ausencia de comentarios y documentación.  

  ### 🔹 Propuestas de mejora

| Nº | Mejora                        | Descripción                                                        | Justificación                           |
| -: | ----------------------------- | ------------------------------------------------------------------ | --------------------------------------- |
|  1 | Simplificar las comparaciones | Reemplazar `DateDiff()` por comparaciones directas (`<=`, `>=`).   | Mejora la legibilidad y precisión.      |
|  2 | Corregir función errónea      | Cambiar `nom()` por `now()`.                                       | Evita errores de ejecución.             |
|  3 | Validar fechas nulas          | Agregar condiciones `IS NOT NULL`.                                 | Evita resultados inesperados o errores. |
|  4 | Normalizar nombres            | Cambiar `fechadesde` → `fecha_inicio`, `fechahasta` → `fecha_fin`. | Facilita comprensión y coherencia.      |
|  5 | Agregar comentarios claros    | Incluir descripción del propósito de la consulta.                  | Mejora la mantenibilidad y comprensión. |


  ### 🔹 Versión refactorizada propuesta

  ```sql
-- ===========================================
-- Script: Búsqueda de vuelos activos por fecha actual
-- Objetivo: Obtener los registros de vuelos cuya fecha actual
-- se encuentre dentro del intervalo de validez.
-- ===========================================

SELECT *
FROM vuelos
WHERE fecha_inicio <= Date()
  AND fecha_fin >= Date()
  AND fecha_inicio IS NOT NULL
  AND fecha_fin IS NOT NULL;

  ```

  ### 🔹 Conclusión (Búsquedas con fechas en Access)

El código original logra la funcionalidad deseada, pero presenta baja legibilidad, errores menores y falta de claridad en la intención.
Con la refactorización propuesta, el código se alinea con los principios de Código Limpio, ofreciendo una consulta más simple, eficiente y comprensible, adecuada para entornos de trabajo colaborativos y mantenibles a largo plazo.

---

## 4️⃣ Análisis del archivo 3: `SQL_Quick_Reference.sql`  

### Código original (fragmento representativo)
```sql
AND / OR	SELECT column_name(s)
FROM table_name
WHERE condition
AND|OR condition

ALTER TABLE	ALTER TABLE table_name
ADD column_name datatype
or
ALTER TABLE table_name
DROP COLUMN column_name

DELETE	DELETE FROM table_name
WHERE some_column=some_value
or
DELETE FROM table_name
(Note: Deletes the entire table!!)
````

---

### 🔹 Observaciones según principios de Código Limpio

| Principio                      | Observación                                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **Nombres significativos**     | Las sentencias SQL son correctas, pero los ejemplos carecen de nombres descriptivos en tablas o columnas.                      |
| **Estructura clara**           | El archivo mezcla más de 30 comandos sin organización ni separación por categorías (DDL, DML, DCL, TCL).                       |
| **Comentarios útiles**         | No hay comentarios explicativos sobre el propósito o efecto de cada sentencia.                                                 |
| **Evitar duplicación**         | Varias instrucciones (`DELETE`, `ALTER TABLE`, `CREATE INDEX`) se repiten con mínimas variaciones.                             |
| **Consistencia de formato**    | El uso de mayúsculas, saltos de línea y espaciado es irregular, dificultando la lectura.                                       |
| **Legibilidad y presentación** | Al estar en formato de tabla plana sin encabezados o contextos, no resulta claro cuál es el objetivo educativo de cada bloque. |

---

### 🔹 Olores de código detectados

* **Duplicación** de ejemplos y sintaxis redundante.
* **Ausencia de estructura jerárquica** (mezcla de DDL, DML, DCL).
* **Falta de comentarios explicativos.**
* **Formato inconsistente** (uso errático de mayúsculas, espacios y saltos).
* **Ausencia de contexto práctico** (tablas o datos ficticios que faciliten comprensión).

---

### 🔹 Propuestas de mejora

| Nº | Mejora                               | Descripción                                              | Justificación                                        |
| -- | ------------------------------------ | -------------------------------------------------------- | ---------------------------------------------------- |
| 1  | **Organizar por categorías SQL**     | Dividir en secciones DDL, DML, DCL, TCL y Funciones.     | Facilita el estudio y comprensión.                   |
| 2  | **Estandarizar formato SQL**         | Mantener comandos en mayúsculas y nombres en minúsculas. | Aumenta la legibilidad y profesionalismo.            |
| 3  | **Eliminar redundancias**            | Consolidar ejemplos repetidos con notas aclaratorias.    | Reduce confusión y mejora la limpieza del documento. |
| 4  | **Agregar ejemplos reales**          | Usar tablas como `empleados`, `productos`, `clientes`.   | Facilita la comprensión práctica.                    |
| 5  | **Agregar comentarios explicativos** | Breves descripciones del objetivo de cada comando.       | Mejora la utilidad pedagógica.                       |

---

### 🔹 Versión refactorizada propuesta

```sql
-- ============================================================
-- SECCIÓN DDL (Data Definition Language)
-- ============================================================

-- Crear una nueva base de datos
CREATE DATABASE tienda;

-- Crear tabla de empleados
CREATE TABLE empleados (
  id INT PRIMARY KEY,
  nombre VARCHAR(100),
  cargo VARCHAR(50),
  salario DECIMAL(10,2)
);

-- Modificar tabla (añadir columna)
ALTER TABLE empleados
ADD COLUMN fecha_ingreso DATE;

-- Eliminar columna
ALTER TABLE empleados
DROP COLUMN fecha_ingreso;

-- Eliminar tabla
DROP TABLE empleados;

-- ============================================================
-- SECCIÓN DML (Data Manipulation Language)
-- ============================================================

-- Insertar un registro
INSERT INTO empleados (id, nombre, cargo, salario)
VALUES (1, 'Ana Torres', 'Analista', 1800.00);

-- Consultar datos
SELECT nombre, cargo, salario
FROM empleados
WHERE salario > 1500
ORDER BY salario DESC;

-- Actualizar registros
UPDATE empleados
SET salario = salario * 1.10
WHERE cargo = 'Analista';

-- Eliminar un registro
DELETE FROM empleados
WHERE id = 1;

-- Truncar tabla (eliminar todos los registros)
TRUNCATE TABLE empleados;

-- ============================================================
-- SECCIÓN DE FILTRADO Y CONDICIONES
-- ============================================================

-- Uso de AND / OR
SELECT * FROM empleados
WHERE cargo = 'Analista' OR salario > 2000;

-- Uso de BETWEEN
SELECT nombre, salario
FROM empleados
WHERE salario BETWEEN 1500 AND 2500;

-- Uso de IN
SELECT nombre
FROM empleados
WHERE cargo IN ('Analista', 'Gerente', 'Supervisor');

-- Uso de LIKE
SELECT nombre
FROM empleados
WHERE nombre LIKE 'A%';

-- ============================================================
-- SECCIÓN DE FUNCIONES Y AGRUPACIÓN
-- ============================================================

-- Agrupar por cargo
SELECT cargo, AVG(salario) AS promedio_salarial
FROM empleados
GROUP BY cargo
HAVING AVG(salario) > 1600;

-- ============================================================
-- SECCIÓN DE JOINS
-- ============================================================

-- INNER JOIN
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
INNER JOIN departamentos
ON empleados.id_departamento = departamentos.id;

-- LEFT JOIN
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
LEFT JOIN departamentos
ON empleados.id_departamento = departamentos.id;

-- RIGHT JOIN
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
RIGHT JOIN departamentos
ON empleados.id_departamento = departamentos.id;

-- FULL JOIN
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
FULL JOIN departamentos
ON empleados.id_departamento = departamentos.id;

-- ============================================================
-- SECCIÓN DCL (Data Control Language)
-- ============================================================

-- Conceder permisos
GRANT SELECT, INSERT ON empleados TO 'usuario_app';

-- Revocar permisos
REVOKE INSERT ON empleados FROM 'usuario_app';

-- ============================================================
-- SECCIÓN TCL (Transaction Control Language)
-- ============================================================

BEGIN TRANSACTION;
UPDATE empleados SET salario = salario * 1.05;
COMMIT;

-- ============================================================
-- SECCIÓN DE VISTAS E ÍNDICES
-- ============================================================

-- Crear una vista
CREATE VIEW vista_empleados AS
SELECT nombre, cargo, salario
FROM empleados
WHERE salario > 1500;

-- Crear índice
CREATE INDEX idx_empleados_salario
ON empleados (salario);

-- ============================================================
-- SECCIÓN DE OPERADORES Y UNIONES
-- ============================================================

-- UNION (elimina duplicados)
SELECT nombre FROM empleados
UNION
SELECT nombre FROM clientes;

-- UNION ALL (incluye duplicados)
SELECT nombre FROM empleados
UNION ALL
SELECT nombre FROM clientes;

-- SELECT DISTINCT (valores únicos)
SELECT DISTINCT cargo FROM empleados;

-- SELECT TOP (dependiendo del motor)
SELECT TOP 5 * FROM empleados;
```

---

### 🔹 Conclusión del análisis

El documento original **SQL Quick Reference** contiene información valiosa, pero su estructura era desordenada, con repeticiones y sin contexto.
Tras aplicar los principios de **Código Limpio**, el resultado es un archivo más didáctico, coherente y profesional.
La división por secciones, los ejemplos significativos y los comentarios facilitan el uso del material tanto en entornos educativos como técnicos.

---


