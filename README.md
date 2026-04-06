Descripción
Este sistema fue desarrollado para reemplazar procesos manuales y planillas de cálculo (Excel) propensas a la pérdida de datos y falta de trazabilidad. Permite la creación, seguimiento y cierre de Órdenes de Trabajo en un entorno de planta de manufactura, garantizando la integridad de la información mediante una base de datos relacional.

 Tecnologías utilizadas
Lenguaje: Python 3.7

Interfaz Gráfica: Tkinter / CustomTkinter

Base de Datos: SQLite 3

Arquitectura: Patrón de diseño MVC (Modelo-Vista-Controlador)

Librerías extra: tkcalendar para manejo de fechas.

 Características principales
Arquitectura Robusta: Separación clara entre la lógica de negocio y la interfaz de usuario.

Persistencia de Datos: Eliminación de errores de guardado comunes en hojas de cálculo mediante transacciones SQL.

Seguridad de Datos: El sistema incluye validaciones de campos y manejo de estados (habilitar/deshabilitar campos según el proceso).

Escalabilidad: Diseñado para implementarse en múltiples plantas (actualmente operativo en 2 plantas industriales).

 Estructura del Proyecto
principalvista.py: Definición de la interfaz gráfica y componentes.

controlador.py: Lógica de conexión entre la UI y la base de datos.

estructura.sql: Esquema de la base de datos (se omite el archivo .db por razones de confidencialidad de datos industriales).

 Instalación
Clonar el repositorio.

Instalar dependencias: pip install tkcalendar.

Ejecutar el script estructura.sql en un gestor SQLite para generar las tablas.

Ejecutar el archivo principal de Python.
