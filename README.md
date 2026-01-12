# Asistente Huesos: Asistente Virtual Universal IoT



## Requirements

- python 13+
- pip 24+
- Django 5+
- Bootstrap 5



![Status](https://img.shields.io/badge/Status-Finalizado-success)
![Institution](https://img.shields.io/badge/ESCOM-IPN-blue)
![Area](https://img.shields.io/badge/Sistemas%20Embebidos-IoT-orange)

## Descripción del Proyecto
[cite_start]Proyecto enfocado en desarrollar un asistente virtual tipo alexa, con Procesamiento del Lenguaje Natural por medio de expresiones regulares diseñado bajo una **arquitectura abierta** para resolver la falta de interoperabilidad en la domótica actual[cite: 25, 27, 36]. [cite_start]A diferencia de los ecosistemas cerrados comerciales que generan "islas tecnológicas" y obsolescencia programada, este sistema actúa como un orquestador universal capaz de integrar dispositivos electrónicos heterogéneos. Está dirijido a usuarios con un nivel medio de conocieminto en diseño y desarrollo de Circuitos eléctricos.[cite: 24, 30].

[cite_start]El núcleo del sistema reside en una **Raspberry Pi** que funciona como servidor central, gestionando la comunicación entre sensores y actuadores mediante el protocolo ligero **MQTT**[cite: 45, 47]. [cite_start]Esto permite automatizar tareas domésticas y controlar circuitos mediante comandos de voz, sin depender de un único fabricante[cite: 53].

---

## Características Técnicas Destacadas

* [cite_start]**Arquitectura de Hardware Abierto:** Permite la integración de componentes de distinta procedencia y marcas mediante APIs y estándares abiertos, combatiendo la obsolescencia tecnológica[cite: 41, 58].
* [cite_start]**Comunicación Ligera (MQTT):** Implementación del protocolo *Message Queuing Telemetry Transport* (Pub/Sub) para garantizar baja latencia y mínimo consumo de ancho de banda en la comunicación con microcontroladores[cite: 47, 48].
* [cite_start]**Procesamiento Centralizado:** Una Raspberry Pi actúa como el "cerebro" del sistema, procesando los comandos de voz y orquestando la lógica de control hacia los nodos de la red[cite: 45].
* **Automatización Híbrida:** Capacidad de ejecutar acciones mediante:
    * [cite_start]**Comandos de Voz:** Interpretación directa para control de actuadores (ON/OFF)[cite: 39, 52].
    * [cite_start]**Métricas Ambientales:** Automatización basada en datos de sensores (ej. temperatura)[cite: 40, 51].
* [cite_start]**Interoperabilidad:** Capacidad de reutilizar hardware existente y mezclar tecnologías, reduciendo costos y basura electrónica[cite: 57, 58].

---

## Arquitectura del Sistema

1.  [cite_start]**Nodos Periféricos (Edge):** Microcontroladores y sensores heterogéneos que actúan como publicadores/suscriptores[cite: 48].
2.  [cite_start]**Transporte:** Red local sobre protocolo MQTT[cite: 47].
3.  **Procesamiento (Hub Central):** Raspberry Pi ejecutando:
    * [cite_start]**Broker MQTT:** Gestión de mensajes y colas[cite: 45].
    * [cite_start]**Interfaz de Voz:** Motor de reconocimiento y procesamiento de comandos[cite: 39, 45].
4.  [cite_start]**Acción:** Actuadores físicos (relés/circuitos) que ejecutan las órdenes del usuario[cite: 50].

---

## Lista de Materiales (Hardware Propuesto)

| Cant. | Componente | Descripción / Nota Técnica |
| :---: | :--- | :--- |
| 1 | **Raspberry Pi** |Servidor Central, Broker MQTT y Procesamiento de Voz. |
| 1 | **Tarjeta MicroSD** | Almacenamiento para el S.O. y scripts del servidor. |
| 1 | **Microcontroladores** | ESP-32. |
| 1 | **Fuente de Alimentación** | Adecuada para la Raspberry Pi y etapas de potencia. |

---

## Stack de Software

* **S.O.:** Raspberry Pi OS (Linux).
* [cite_start]**Protocolo de Comunicación:** MQTT (Message Queuing Telemetry Transport)[cite: 47].
* [cite_start]**Middleware:** Broker MQTT (ej. Mosquitto) para arquitectura Publicación/Suscripción[cite: 47].
* [cite_start]**Backend:** Scripts de orquestación para traducción de voz a *payloads* MQTT[cite: 45].
* [cite_start]**Integración:** APIs para compatibilidad con dispositivos de terceros[cite: 41].

---

## Galería de Evidencias

*(Sección reservada para capturas de pantalla del funcionamiento, fotos del montaje físico y diagramas de conexión del proyecto "Asistente Huesos" una vez implementado).*

### 1. Diagrama de Arquitectura
![Arquitectura MQTT](https://via.placeholder.com/600x300?text=Diagrama+Arquitectura+MQTT+Raspberry)

### 2. Prototipo Físico
![Montaje Hardware](https://via.placeholder.com/600x300?text=Foto+Prototipo+Raspberry+y+Circuitos)

---

## Instalación y Reproducción (Guía General)

### 1. Configuración del Servidor (Raspberry Pi)
* Instalar Raspberry Pi OS.
* Instalar y configurar el Broker MQTT (Mosquitto) para aceptar conexiones locales.
    ```bash
    sudo apt install mosquitto mosquitto-clients
    ```

### 2. Configuración de Nodos
* Programar los microcontroladores para conectarse a la red WiFi local.
* [cite_start]Configurar los *topics* de suscripción para recibir comandos (ej. encender luces)[cite: 50].
* [cite_start]Configurar los *topics* de publicación para enviar telemetría (ej. temperatura)[cite: 51].

### 3. Interfaz de Texto
* Ejecutar el script principal de "Asistente Huesos" en la Raspberry Pi.

---

## Autores
[cite_start]Proyecto desarrollado para la unidad de aprendizaje **Sistemas Embebidos - IoT** en la **Escuela Superior de Cómputo (ESCOM - IPN)**[cite: 4, 6].

* [cite_start]**García Martínez Arturo** [cite: 11]
* [cite_start]**López Salinas Eduardo** [cite: 12]
* [cite_start]**Jiménez Ramirez Victor Emmanuel** [cite: 13]
* [cite_start]**Rodríguez Jiménez Yahel Eduardo** [cite: 13]

[cite_start]**Grupo:** 6CM3 [cite: 15]
[cite_start]**Profesor:** Arce Aleman Miguel Angel [cite: 8]
