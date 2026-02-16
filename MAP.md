🧭 MAP.md — Python Module 06 · The Codex
Arquitectura de Imports & Diseño de Packages
🌱 IDEA CENTRAL DEL MÓDULO

Pasar de:

❌ “importo cosas y si funciona, perfecto”
a
✅ “controlo qué expone mi sistema y cómo se conecta cada parte”

Los imports no son sintaxis.
Son arquitectura invisible.

🧠 VISIÓN GLOBAL DEL RECORRIDO

El módulo progresa desde:

ex0 → exponer una API pública
ex1 → decidir cómo importar
ex2 → organizar jerarquías reales
ex3 → resolver dependencias circulares

No es un módulo de “imports”.
Es un módulo de control de dependencias y diseño modular.

🟢 ex0 — Diseñar una API pública (The Sacred Scroll)
🎯 FOCO

Entender que un package no es una carpeta:
es una interfaz pública controlada.

📐 Arquitectura mental
alchemy/
 ├── __init__.py  ← API pública
 ├── elements.py  ← implementación interna

🧠 CONCEPTOS CLAVE

Módulo vs package

__init__.py como frontera

Qué se expone y qué no

Namespace controlado

🧩 CLAVE MENTAL

👉 Todo existe dentro del módulo.
👉 Solo existe fuera lo que tú decides exportar.

# alchemy/__init__.py
from .elements import create_earth


Si no lo exportas → no forma parte del contrato.

Esto es diseño de API.

🔗 Prepara para → entender acoplamiento real

🟢 ex1 — Estilos de import (Import Transmutation)
🎯 FOCO

Comprender que importar también es una decisión de diseño.

📐 Formas de importar
import alchemy
from alchemy import create_earth
import alchemy as alc
from alchemy import create_earth as ce

🧠 CONCEPTOS CLAVE

Namespace

Legibilidad

Acoplamiento

Claridad vs comodidad

🧩 CLAVE MENTAL

👉 Cuanto más específico el import,
👉 más estrecho el acoplamiento.

Importar un módulo completo:

Más explícito

Más claro

Importar funciones directas:

Más corto

Más frágil si cambia la API

Esto ya es arquitectura.

🔗 Depende de → ex0
🔗 Prepara para → diseño escalable

🟢 ex2 — Absoluto vs Relativo (The Great Pathway Debate)
🎯 FOCO

Organizar jerarquías reales con subpackages.

📐 Arquitectura mental
alchemy/
 ├── __init__.py
 ├── elements.py
 └── transmutation/
      ├── __init__.py
      ├── basic.py
      └── advanced.py

🧠 CONCEPTOS CLAVE

Imports absolutos:

from alchemy.transmutation.basic import ...


Imports relativos:

from .basic import ...

🧩 CLAVE MENTAL

👉 Absoluto = claridad global
👉 Relativo = comodidad local

Cuando el proyecto crece:
los absolutos escalan mejor.

Aquí empiezas a pensar como diseñador de paquetes.

🔗 Prepara para → evitar dependencias circulares

🟢 ex3 — Dependencias circulares (Breaking the Circular Curse)
🎯 FOCO

Entender cómo Python carga módulos.

🧠 Qué ocurre realmente

Cuando haces:

import module_a


Python:

Crea el objeto módulo

Lo añade a sys.modules

Ejecuta su código

Si module_a importa module_b
y module_b importa module_a
→ uno se ejecuta incompleto
→ error.

🧩 CLAVE MENTAL

👉 El problema no es el import.
👉 Es el diseño de dependencias.

Soluciones:

Reorganizar responsabilidades

Extraer lógica común

Usar late imports si el diseño lo permite

def function():
    from module_b import something


Late import = herramienta de emergencia, no parche permanente.

🔁 EVOLUCIÓN DEL DISEÑO
Nivel	Concepto	Ejercicio
Base	Exponer API	ex0
Intermedio	Diseñar imports	ex1
Estructural	Organizar jerarquía	ex2
Arquitectónico	Resolver dependencias	ex3
🧠 MAPA GLOBAL
archivo → módulo → package → subpackage → sistema modular estable

🧩 DECISIONES DE DISEÑO (CON INTENCIÓN)

__init__.py define contrato

Scripts usan el package, no archivos internos

Imports absolutos para claridad global

Evitar dependencias bidireccionales

Pensar en dependencias antes de escribir código

🎯 IDEA FINAL DEL MÓDULO

El módulo 6 no trata de imports.

Trata de:

Diseño modular

Control de dependencias

Definición de API

Escalabilidad futura

Un sistema bien importado es:

predecible

estable

mantenible

🧠 FRASE RESUMEN 

El módulo progresa desde comprender qué es un módulo hasta diseñar una arquitectura de paquetes con APIs explícitas y dependencias controladas, entendiendo que los imports forman parte del diseño estructural del sistema y no son solo sintaxis.
