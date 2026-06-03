---
sidebar_position: 5
title: Glosario
description: Definiciones de términos técnicos para personas que se inician en el mundo TI y cloud computing.
---

# 📖 Glosario de Términos

Definiciones de conceptos técnicos orientadas a personas que se inician en el mundo TI y cloud computing. Los términos subrayados con línea punteada en los documentos muestran su definición al pasar el cursor.

---

<a id="ami" />

## AMI

**Amazon Machine Image.** Plantilla preconfigurada que contiene el sistema operativo y el software necesario para lanzar una instancia EC2. Es el punto de partida de cualquier servidor en AWS. Una AMI puede incluir Amazon Linux, Ubuntu, Windows Server, entre otros.

---

<a id="apache" />

## Apache (httpd)

Servidor web de código abierto ampliamente utilizado en el mundo. Recibe peticiones HTTP de los navegadores y responde con el contenido solicitado (HTML, imágenes, archivos). El nombre `httpd` significa *HTTP Daemon* — un proceso que corre en segundo plano atendiendo solicitudes web.

---

<a id="cifrado" />

## Cifrado (Encryption)

Proceso de transformar datos legibles en un formato ininteligible usando un algoritmo matemático y una clave. Solo quien posea la clave correcta puede descifrar y leer la información. Se usa para proteger datos en tránsito (como HTTPS) y datos en reposo (como volúmenes EBS cifrados).

---

<a id="cli" />

## CLI

**Command Line Interface.** Interfaz de texto donde el usuario escribe comandos para interactuar con el sistema, en lugar de usar botones o menús gráficos. Es más poderosa y automatizable que las interfaces gráficas (GUI). Ejemplo: la terminal de Linux o el símbolo del sistema de Windows.

---

<a id="ip" />

## Dirección IP

Identificador numérico único asignado a cada dispositivo conectado a una red. Funciona como una dirección postal: permite que los datos sepan a dónde ir. Existen dos tipos:
- **IP privada:** usada dentro de redes locales o VPCs (no accesible desde Internet)
- **IP pública:** accesible desde Internet (ej: `54.210.23.87`)

---

<a id="dns" />

## DNS

**Domain Name System.** Sistema que traduce nombres de dominio legibles por humanos (como `restart-labs.devera.cloud`) a direcciones IP numéricas que los computadores entienden. Funciona como la "agenda telefónica" de Internet.

---

<a id="ebs" />

## EBS — Volumen EBS

**Elastic Block Store.** Disco virtual persistente que se adjunta a instancias EC2. Similar a un disco duro externo: los datos persisten aunque la instancia se detenga o reinicie. Se factura por GiB reservado, independientemente de si la instancia está en ejecución o detenida.

---

<a id="firewall" />

## Firewall

Barrera de seguridad (software o hardware) que monitorea y controla el tráfico de red según reglas predefinidas. Decide qué conexiones de entrada y salida se permiten y cuáles se bloquean, protegiendo los sistemas de accesos no autorizados. En AWS, los **grupos de seguridad** actúan como firewalls virtuales.

---

<a id="grupo_seguridad" />

## Grupo de seguridad

Firewall virtual a nivel de instancia en AWS. Define reglas de entrada (*inbound*) y salida (*outbound*) que controlan qué tráfico puede llegar o salir de la instancia, especificando protocolo, puerto y dirección IP de origen. Las reglas se aplican automáticamente a todas las instancias del grupo.

---

<a id="http" />

## HTTP

**HyperText Transfer Protocol.** Protocolo de comunicación que define cómo los navegadores web solicitan páginas y cómo los servidores las entregan. Opera en el **puerto 80** por defecto. No cifra los datos, por lo que la información viaja en texto plano y puede ser interceptada.

---

<a id="https" />

## HTTPS

**HTTP Secure.** Versión cifrada de HTTP que usa **SSL/TLS** para proteger los datos en tránsito entre el navegador y el servidor. Opera en el **puerto 443** y muestra el ícono de candado (🔒) en el navegador. Es el estándar actual para cualquier sitio web.

---

<a id="instancia" />

## Instancia

Servidor virtual que se ejecuta en la nube. Una instancia EC2 es una máquina virtual con recursos de cómputo asignados (CPU virtual, RAM, red) que funciona como un servidor independiente. Puede iniciarse, detenerse y terminarse según las necesidades.

---

<a id="protocolo" />

## Protocolo

Conjunto de reglas y estándares que definen cómo se comunican dos sistemas. Establece el formato de los mensajes, el orden de las operaciones y cómo manejar errores. Ejemplos: HTTP (web), SSH (acceso remoto seguro), TCP/IP (transporte de datos en Internet).

---

<a id="puerto" />

## Puerto (Port)

Número que identifica un servicio específico dentro de una misma dirección IP. Permite que un servidor atienda múltiples servicios simultáneamente en la misma IP.

| Puerto | Servicio |
|--------|----------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |

---

<a id="script" />

## Script

Archivo de texto que contiene una secuencia de comandos ejecutados automáticamente por el sistema, sin intervención manual. En este laboratorio, el script de *User Data* instala y configura Apache automáticamente al iniciar la instancia EC2.

---

<a id="servidor_web" />

## Servidor web

Software (o la máquina que lo ejecuta) que almacena y sirve contenido web a los clientes (navegadores). Escucha peticiones en un puerto (generalmente 80 o 443) y responde con los recursos solicitados: páginas HTML, imágenes, archivos CSS, etc.

---

<a id="sistema_operativo" />

## Sistema Operativo (SO)

Software base que gestiona el hardware de una computadora y proporciona servicios a los demás programas. Es la capa fundamental sobre la que corren las aplicaciones. Ejemplos: Windows, macOS, Linux. En AWS, **Amazon Linux 2023** es el sistema operativo usado en el laboratorio EC2.

---

<a id="ssh" />

## SSH

**Secure Shell.** Protocolo cifrado para acceder y administrar servidores de forma remota desde una terminal. Toda la comunicación viaja cifrada, a diferencia de Telnet (su predecesor inseguro). Opera en el **puerto 22** y usa pares de claves para autenticación.

---

<a id="virtualizacion" />

## Virtualización

Tecnología que permite crear versiones virtuales (software) de recursos físicos como servidores, almacenamiento y redes. Permite ejecutar múltiples "computadoras virtuales" (instancias) sobre un único hardware físico, optimizando el uso de recursos. Es la base del cloud computing.

---

<a id="vpc" />

## VPC

**Virtual Private Cloud.** Red virtual privada e aislada dentro de AWS donde se despliegan los recursos. Proporciona control completo sobre el entorno de red: rangos de direcciones IP, subredes, tablas de enrutamiento y gateways. Cada cuenta AWS tiene una VPC por defecto por región.

---

<a id="region" />

## Región AWS

Área geográfica independiente que contiene múltiples Zonas de Disponibilidad. AWS tiene más de 30 regiones en todo el mundo. Los datos almacenados en una región no salen de ella salvo configuración explícita. Factores clave para elegir región: cumplimiento normativo, latencia, servicios disponibles y costos.

---

<a id="az" />

## Zona de Disponibilidad (AZ)

Conjunto de uno o más centros de datos físicamente separados dentro de una Región AWS. Conectadas entre sí por redes privadas de fibra óptica de alta velocidad. Diseñadas para aislamiento de fallos: un desastre en una AZ no afecta a las demás. La latencia entre AZs de la misma región es inferior a 2 ms.

---

<a id="edge_location" />

## Edge Location

Punto de presencia distribuido globalmente usado por servicios como CloudFront, Route 53 y AWS WAF para entregar contenido con menor latencia al usuario final. Existen más de 400 Edge Locations en el mundo, más que las propias regiones AWS. No ejecutan cargas de trabajo completas como las regiones — solo cachean y procesan tráfico de red.

---

<a id="latencia" />

## Latencia

Tiempo que tarda un paquete de datos en viajar desde el origen hasta el destino. Se mide en milisegundos (ms). A menor latencia, más rápida es la experiencia del usuario. Es uno de los factores clave para seleccionar la región AWS donde desplegar una aplicación.

---

<a id="durabilidad" />

## Durabilidad

Probabilidad de que un dato NO se pierda permanentemente. Amazon S3 ofrece 99.999999999% (11 nueves) de durabilidad. Esto equivale estadísticamente a perder 1 objeto de cada 10 billones almacenados. Se logra replicando los datos en múltiples instalaciones físicas dentro de la región.

---

<a id="disponibilidad" />

## Disponibilidad

Porcentaje del tiempo que un servicio está operativo y accesible. S3 Standard ofrece 99.99% de disponibilidad, equivalente a menos de 53 minutos de inactividad al año. Es diferente a la durabilidad: un dato puede estar durablemente almacenado pero temporalmente inaccesible durante un incidente.

---

<a id="data_lake" />

## Data Lake

Repositorio centralizado que almacena grandes volúmenes de datos en su formato original (estructurados, semi-estructurados y no estructurados). Permite análisis posterior con herramientas de Big Data, Machine Learning e IA. Amazon S3 es el servicio de almacenamiento más utilizado para implementar Data Lakes en AWS.

---

<a id="bucket" />

## Bucket (S3)

Contenedor principal de Amazon S3 donde se almacenan los objetos. El nombre debe ser único globalmente en toda AWS (no solo en tu cuenta). Se crea en una región específica. Puede contener millones de objetos sin límite de tamaño total.

---

<a id="objeto_s3" />

## Objeto (S3)

Unidad básica de almacenamiento en Amazon S3. Compuesto por el contenido del archivo (hasta 5 TB), una clave única llamada Key (que identifica el objeto dentro del bucket), metadatos clave-valor y opcionalmente un ID de versión si el versionado está activo.

---

<a id="escalado_vertical" />

## Escalado Vertical (Scale Up)

Aumentar los recursos de una instancia EC2 existente: más vCPU, RAM o almacenamiento. Ejemplo: cambiar de `t3.micro` a `t3.large`. Requiere detener la instancia previamente. Tiene un límite máximo determinado por el tipo de instancia más grande disponible. También llamado "scale up".

---

<a id="escalado_horizontal" />

## Escalado Horizontal (Scale Out)

Agregar más instancias EC2 para distribuir la carga de trabajo entre varios servidores. Ejemplo: pasar de 1 a 10 servidores detrás de un Load Balancer. No requiere detener instancias existentes. Escala prácticamente sin límites. Es la estrategia preferida en arquitecturas cloud modernas. También llamado "scale out".

---

<a id="instance_store" />

## Instance Store

Almacenamiento temporal físicamente adjunto al servidor host de la instancia EC2. Ofrece muy alta velocidad de I/O porque los datos no viajan por la red. Sin embargo, los datos se pierden por completo al detener, hibernar o terminar la instancia. Ideal para caché, buffers y datos intermedios de procesamiento.

---

<a id="etiquetas" />

## Etiquetas (Tags)

Metadatos clave-valor que se agregan a recursos AWS para organizarlos, filtrarlos y gestionar costos. Ejemplo: `Environment=Production`, `Owner=DevOps`, `Project=Proyecto-Alpha`. Permiten analizar gastos por proyecto o equipo en AWS Cost Explorer y aplicar políticas de automatización basadas en etiquetas.
