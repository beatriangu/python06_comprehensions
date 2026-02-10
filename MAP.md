🧭 MAP.md — Python Module 06 · The Codex 🧪
Mastering Python Imports & Packages


Este documento es mi mapa de aprendizaje y diseño.
No describe ejercicios sueltos: explica cómo se construye una arquitectura de imports sana en Python.

Sirve para comprensión, defensa y evolución del código.

🌱 IDEA CENTRAL DEL MÓDULO

Pasar de:

❌ “importo archivos y rezo”
a
✅ “defino interfaces claras y controlo qué expone cada parte del sistema”

Los imports no son sintaxis: son arquitectura.

🧠 OBJETIVO REAL

Dominar el sistema de imports de Python construyendo un package real y entendiendo:

qué es público y qué es interno

cómo __init__.py define una API

cómo escalar un proyecto sin romper dependencias

cómo evitar circular imports de forma consciente

El foco del módulo no es la lógica, sino la organización del código.

🧩 CONCEPTOS CLAVE TRABAJADOS

Módulo vs package

__init__.py como interfaz pública

Acceso a nivel módulo vs nivel package

Estilos de import:

módulo completo

funciones específicas

alias

imports múltiples

Imports absolutos vs relativos

Subpackages y jerarquía

Dependencias circulares y late imports

🗂️ ESTRUCTURA DEL REPOSITORIO (ARQUITECTURA)
python06_import_codex/
├── alchemy/
│   ├── __init__.py          ← API pública
│   ├── elements.py          ← implementación interna
│   └── transmutation/
│       ├── __init__.py
│       ├── basic.py
│       └── advanced.py
├── ft_sacred_scroll.py
├── ft_import_transmutation.py
├── ft_pathway_debate.py
├── ft_circular_curse.py
├── README.md
└── MAP.md


🧠 Clave mental:
Los scripts usan el package.
El package controla qué se expone.

🟢 Part I — The Sacred Scroll
🎯 FOCO

Definir la API pública de un package.

🧠 APRENDO

Un módulo puede contener muchas funciones

Un package no tiene por qué exponerlas todas

__init__.py decide qué existe a nivel package

🧩 CLAVE MENTAL

👉 Lo que no está en __init__.py no existe para el exterior.

alchemy.elements.create_earth()   ✔
alchemy.create_earth()            ✖ AttributeError


El error se gestiona sin crash.

🟢 Part II — Import Transmutation
🎯 FOCO

Comprender los estilos de import y sus consecuencias.

🧠 APRENDO

Importar módulos completos vs funciones

Uso de alias

Imports múltiples

Impacto en:

legibilidad

namespace

acoplamiento

🧩 CLAVE MENTAL

👉 Importar también es una decisión de diseño.

🟢 Part III — The Great Pathway Debate
🎯 FOCO

Comparar imports absolutos vs relativos.

🧠 APRENDO

Absolutos: más explícitos, más claros

Relativos: más concisos, más frágiles si crece el proyecto

Subpackages bien definidos

Exposición controlada vía __init__.py

🧩 CLAVE MENTAL

👉 Ambos funcionan.
👉 La elección depende de escala y claridad, no de gustos.

🟢 Part IV — Breaking the Circular Curse
🎯 FOCO

Evitar dependencias circulares sin hacks.

🧠 APRENDO

Qué es una dependencia circular

Por qué Python falla al cargar módulos cíclicos

Uso de late imports para romper el ciclo

Mantener responsabilidades separadas

🧩 CLAVE FINAL

👉 El diseño evita el problema.
👉 El late import resuelve cuando el diseño lo permite.

El sistema:

detecta el problema

no crashea

sigue funcionando

🧠 VISIÓN GLOBAL DEL MÓDULO
archivo → módulo → package → subpackage → sistema estable


No son scripts sueltos.
Es una arquitectura de imports consciente.

📌 CONCEPTOS CLAVE PARA DEFENSA

Un módulo se carga entero al importarse

Un package expone solo lo definido en __init__.py

__init__.py define la API pública

Los imports forman parte de la arquitectura

Las dependencias circulares se evitan con diseño, no con magia

✅ CHECKLIST FINAL

 Scripts ejecutables desde la raíz

 Sin errores de import

 APIs públicas explícitas

 flake8 limpio (# noqa: F401 usado de forma intencional)

 Código claro, simple y defendible

▶️ TESTS MANUALES
python3 ft_sacred_scroll.py
python3 ft_import_transmutation.py
python3 ft_pathway_debate.py
python3 ft_circular_curse.py


Este módulo demuestra cómo diseñar paquetes Python con interfaces claras, imports controlados y dependencias seguras, entendiendo que los imports forman parte de la arquitectura del sistema y no son un detalle de sintaxis.
