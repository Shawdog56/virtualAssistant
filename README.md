# Asistente Huesos: Orquestador Universal IoT

[![Licencia](https://img.shields.io/badge/Licencia-Apache--2.0-blue.svg)](LICENSE)
[![Estado](https://img.shields.io/badge/Status-Finalizado-success)](https://github.com/Shawdog56/virtualAssistant)
[![Institución](https://img.shields.io/badge/ESCOM-IPN-blue)](https://www.escom.ipn.mx/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0%2B-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)

**Asistente Huesos** es un asistente virtual de código abierto diseñado para resolver la fragmentación en el ecosistema de la domótica. A diferencia de las soluciones comerciales cerradas, este sistema actúa como un **hub centralizado e interoperable** capaz de integrar dispositivos heterogéneos mediante una arquitectura abierta y protocolos ligeros.

---

## Características Principales

* **Arquitectura Abierta:** Diseñado para evitar las "islas tecnológicas", permitiendo la integración de hardware de diferentes fabricantes sin obsolescencia programada.
* **Procesamiento de Lenguaje Natural (PLN):** Motor de interpretación basado en expresiones regulares para el control preciso de dispositivos mediante comandos de voz.
* **Comunicación de Baja Latencia:** Implementación del protocolo **MQTT** (Message Queuing Telemetry Transport) para una gestión eficiente de sensores y actuadores.
* **Automatización Inteligente:** Ejecución de acciones basada en umbrales de métricas ambientales (ej. temperatura, humedad) y comandos directos.
* **Interfaz Web Moderna:** Panel de control desarrollado con Django y Bootstrap 5 para la gestión visual del ecosistema.

---

## Arquitectura del Sistema

El sistema se basa en un modelo de **Computación en el Borde (Edge Computing)** organizado en cuatro capas:

1.  **Capa de Dispositivos (Nodos):** Microcontroladores (ESP-32) que actúan como sensores y actuadores.
2.  **Capa de Transporte:** Red local que utiliza el protocolo MQTT bajo un modelo de Publicación/Suscripción.
3.  **Núcleo de Procesamiento (Hub):** Una Raspberry Pi que aloja el Broker MQTT y la lógica del asistente virtual.
4.  **Capa de Acción:** Ejecución física de tareas (relés, circuitos eléctricos) y respuesta por voz.

---

## Stack Tecnológico

### Software
* **Backend:** Python 3.11+ / Django 5.0+
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Middleware:** Broker MQTT (Mosquitto)
* **Base de Datos:** SQLite (desarrollo) / PostgreSQL (producción)

### Hardware Recomendado
* **Servidor Central:** Raspberry Pi (con Raspberry Pi OS).
* **Nodos IoT:** ESP-32 / ESP-8266.
* **Periféricos:** Sensores de temperatura, módulos de relé, micrófono y altavoces.

---

## Instalación y Configuración

Sigue estos pasos para desplegar el entorno de desarrollo localmente:

### Clonar el repositorio
```bash
git clone [https://github.com/Shawdog56/virtualAssistant.git](https://github.com/Shawdog56/virtualAssistant.git)
cd virtualAssistant
```

### Archivo .env
```bash
SECRET_KEY=TU-LLAVE-SEGURA

# Configuración de la base de datos
DB=BD
USER=USUARIO
PASSWORD=CONTRASENHA
HOST=HOST
PORT=PORT
ENGINE=ENGINE

# Configuración del servicio de email
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST=EHOST
EMAIL_PORT=EPORT
EMAIL_USE_TLS=True
EMAIL_HOST_USER=EHOST-USER
EMAIL_HOST_PASSWORD=EPASSWORD # No spaces

# Localhost con puerto
LOCALHOST="http://localhost:8000"
# Aquí va la url de tu servidor
SERVER="192.168.137.123"
```
