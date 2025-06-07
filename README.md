# API de Cotizaciones Legales + IA

Este proyecto implementa una **API REST** para gestionar cotizaciones de servicios legales y un microservicio de IA que analiza cada cotización usando el asistente virtual de OpenAI. Incluye además un frontend Angular sencillo listo para usar.


## Mejoras pendientes

- Rediseñar y optimizar la interfaz visual, separando el frontend en un repositorio y proyecto independiente para mejorar la modularidad y facilitar el mantenimiento.
- Integrar servicios de IA adicionales en contenedores dedicados, permitiendo especializar las respuestas según el tipo de consulta o área legal.
- Evaluar la implementación de un contenedor remoto que ejecute modelos de IA open source como Ollama o Deepseek, eliminando la dependencia de servicios de pago y aumentando la autonomía del sistema.

## ¿Qué hace la API?

- Permite **crear, listar, obtener y actualizar cotizaciones** legales.
- Calcula precios según el tipo de servicio.
- El microservicio de IA analiza cada cotización y sugiere ajustes de precio, complejidad y servicios adicionales usando GPT (OpenAI).
- Todo el sistema es **modular y desacoplado**: backend, IA y frontend corren en contenedores separados.

---

## Tutorial de despliegue rápido

### Requisitos previos

- Tener instalado **Docker** y **Docker Compose**
- (Para el frontend) Tener instalado **Node.js** y **Angular CLI** (`npm install -g @angular/cli`)

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/delgado-capital-farmer-exam.git
cd delgado-capital-farmer-exam
```

### 2. Configura tu clave de OpenAI

Debes tener una clave válida de OpenAI.
Cópiala en el archivo `.env` de cada microservicio que use GPT, por ejemplo:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. Despliega los servicios con Docker Compose

```bash
docker compose up --build
```

Esto levantará:
- La base de datos MySQL
- El microservicio de cotizaciones legales (FastAPI)
- El microservicio de IA (FastAPI + OpenAI)

### 4. Prueba la API con Postman

En la raíz del proyecto tienes el archivo `postman_collection.json` con ejemplos de pruebas para todos los endpoints. 
Importa ese archivo en Postman y prueba los endpoints fácilmente.

---

## Frontend (Angular)

El frontend está en la carpeta `frontend/legal_service/`.

### Pasos para ejecutarlo en modo desarrollo

1. Instala las dependencias (debes tener Node.js y Angular CLI):

    ```bash
    cd frontend/legal_service/
    npm install
    ```

2. Ejecuta el servidor de desarrollo:

    ```bash
    ng serve
    ```

3. Accede a la app en [http://localhost:4200](http://localhost:4200)

---

## Notas importantes

- **Recuerda:** Debes tener una clave válida de OpenAI para que el microservicio de IA funcione.
- Los tres contenedores deben estar corriendo antes de usar el frontend.
- El archivo `postman_collection.json` te permite probar la API fácilmente.

---

**Respuestas:**

1. **Arquitectura Modular:**  
   Modularizaría el sistema usando microservicios, donde cada módulo (cotizaciones, tickets, expedientes, etc.) sería un servicio independiente, desplegado en su propio contenedor Docker. Cada microservicio tendría su propia base de datos o esquema, y se comunicarían entre sí mediante APIs REST o mensajería (por ejemplo, usando RabbitMQ). Así, cada módulo puede evolucionar, escalar y mantenerse de forma independiente, pero seguir conectado al ecosistema general.

2. **Escalabilidad:**
   Si el sistema crece de 10 a 100 usuarios, ajustaría la base de datos optimizando índices, usando réplicas para balancear la carga de lectura, y separando la base de datos por módulos si es necesario (por ejemplo, una base para cotizaciones y otra para expedientes). También consideraría usar un servicio de base de datos gestionado en la nube para facilitar el escalado vertical y horizontal.

3. **Integraciones:**
   Para automatizar el guardado de documentos legales en Google Drive o Dropbox, implementaría un microservicio dedicado a la gestión de documentos. Este servicio usaría las APIs oficiales de Google Drive o Dropbox, autenticando con OAuth2. Cuando se genere o suba un documento, el microservicio lo enviaría automáticamente a la nube, almacenando el enlace de acceso en la base de datos del sistema.

4. **Deployment:**
   El frontend Angular se desplegaría en un bucket S3 de Amazon Web Services, configurado para servir contenido estático y con CloudFront para distribución global. La API y los microservicios se ejecutarían en una instancia EC2 de AWS, usando Docker Compose o Kubernetes para orquestar los contenedores. Así, la aplicación sería accesible desde computadoras y celulares, con bajo costo de mantenimiento y alta disponibilidad.

5. **Seguridad:**
   Para la seguridad básica de los datos, implementaría autenticación y autorización usando OAuth2 y JWT (JSON Web Tokens) en todos los endpoints de la API. Además, usaría HTTPS para cifrar las comunicaciones, restringiría el acceso a la base de datos solo a los servicios necesarios y almacenaría las claves sensibles en variables de entorno seguras.
