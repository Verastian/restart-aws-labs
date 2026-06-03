const glossary = {
  firewall: {
    term: 'Firewall',
    definition:
      'Barrera de seguridad (software o hardware) que monitorea y controla el tráfico de red según reglas predefinidas. Decide qué conexiones se permiten y cuáles se bloquean, protegiendo los sistemas de accesos no autorizados.',
  },
  http: {
    term: 'HTTP',
    definition:
      'HyperText Transfer Protocol. Protocolo de comunicación que define cómo los navegadores web solicitan páginas y cómo los servidores las entregan. Opera en el puerto 80 y no cifra los datos.',
  },
  https: {
    term: 'HTTPS',
    definition:
      'HTTP Secure. Versión cifrada de HTTP que usa SSL/TLS para proteger los datos en tránsito. Opera en el puerto 443 y muestra el candado en el navegador.',
  },
  apache: {
    term: 'Apache (httpd)',
    definition:
      'Servidor web de código abierto ampliamente utilizado. Recibe peticiones HTTP de los navegadores y responde con el contenido solicitado (HTML, imágenes, etc.). "httpd" significa HTTP Daemon.',
  },
  servidor_web: {
    term: 'Servidor web',
    definition:
      'Software (o máquina) que almacena y sirve contenido web a los clientes (navegadores). Escucha peticiones en un puerto (generalmente 80 o 443) y responde con los recursos solicitados.',
  },
  ip: {
    term: 'Dirección IP',
    definition:
      'Identificador numérico único asignado a cada dispositivo en una red. Similar a una dirección postal: permite que los datos sepan a dónde ir. Ejemplo: 192.168.1.1 (privada) o 54.210.23.87 (pública).',
  },
  puerto: {
    term: 'Puerto (Port)',
    definition:
      'Número que identifica un servicio específico dentro de una misma dirección IP. El puerto 80 es HTTP, el 443 es HTTPS, el 22 es SSH. Permite que un servidor atienda múltiples servicios simultáneamente.',
  },
  dns: {
    term: 'DNS',
    definition:
      'Domain Name System. Sistema que traduce nombres de dominio legibles por humanos (como google.com) a direcciones IP numéricas. Funciona como la "agenda telefónica" de Internet.',
  },
  ssh: {
    term: 'SSH',
    definition:
      'Secure Shell. Protocolo cifrado para acceder y administrar servidores de forma remota desde una terminal. Reemplaza a Telnet al agregar cifrado completo de la sesión.',
  },
  protocolo: {
    term: 'Protocolo',
    definition:
      'Conjunto de reglas y estándares que definen cómo se comunican dos sistemas. Define el formato de los mensajes, el orden de las operaciones y cómo manejar errores. Ejemplos: HTTP, SSH, TCP/IP.',
  },
  sistema_operativo: {
    term: 'Sistema Operativo (SO)',
    definition:
      'Software base que gestiona el hardware de una computadora y proporciona servicios a los programas. Ejemplos: Windows, macOS, Linux. En AWS, Amazon Linux 2023 es el SO usado en este laboratorio.',
  },
  virtualizacion: {
    term: 'Virtualización',
    definition:
      'Tecnología que permite crear versiones virtuales de recursos físicos (servidores, almacenamiento, red). Permite ejecutar múltiples "computadoras virtuales" en un solo hardware físico.',
  },
  instancia: {
    term: 'Instancia',
    definition:
      'Servidor virtual que se ejecuta en la nube. Una instancia EC2 es una máquina virtual con recursos de cómputo (CPU, RAM) asignados, que funciona como un servidor independiente.',
  },
  ebs: {
    term: 'Volumen EBS',
    definition:
      'Elastic Block Store. Disco virtual persistente que se adjunta a instancias EC2. Similar a un disco duro externo: los datos persisten aunque se detenga la instancia. Se cobra por GiB reservado.',
  },
  cifrado: {
    term: 'Cifrado (Encryption)',
    definition:
      'Proceso de transformar datos legibles en un formato ininteligible usando un algoritmo matemático. Solo quien tenga la clave correcta puede descifrarlos. Protege la información en tránsito y en reposo.',
  },
  ami: {
    term: 'AMI',
    definition:
      'Amazon Machine Image. Plantilla preconfigurada que contiene el sistema operativo y software necesario para lanzar una instancia EC2. Es el punto de partida de cualquier servidor en AWS.',
  },
  vpc: {
    term: 'VPC',
    definition:
      'Virtual Private Cloud. Red virtual privada e aislada dentro de AWS donde se despliegan los recursos. Proporciona control completo sobre el entorno de red: rangos de IP, subredes y enrutamiento.',
  },
  script: {
    term: 'Script',
    definition:
      'Archivo de texto que contiene una secuencia de comandos ejecutados automáticamente por el sistema. En este laboratorio, el script de User Data instala y configura Apache al iniciar la instancia.',
  },
  cli: {
    term: 'CLI',
    definition:
      'Command Line Interface. Interfaz de texto donde se escriben comandos para interactuar con el sistema. Alternativa a las interfaces gráficas (GUI). Más poderosa y automatizable para administración de servidores.',
  },
  grupo_seguridad: {
    term: 'Grupo de seguridad',
    definition:
      'Firewall virtual a nivel de instancia en AWS. Define reglas de entrada (inbound) y salida (outbound) que controlan qué tráfico puede llegar o salir de la instancia por protocolo, puerto y origen.',
  },
};

export default glossary;
