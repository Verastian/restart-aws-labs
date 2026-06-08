---
sidebar_position: 3
title: Incidente — Pérdida de Conectividad en VPS
description: Análisis del incidente de conectividad total en el VPS de Hostinger, soluciones aplicadas y comandos de diagnóstico.
---

# 🚨 Incidente: Pérdida de Conectividad en VPS (Hostinger)

📅 **Fecha:** 2026-06-08 &nbsp;|&nbsp; 🏷️ **Proyecto:** `restart-labs.devera.cloud` &nbsp;|&nbsp; 🔴 **Severidad:** Alta

---

## 🧩 Resumen ejecutivo

El VPS de Hostinger perdió conectividad total — todos los proyectos desplegados (n8n, Nginx Proxy Manager, restart-labs) dejaron de responder desde el exterior. El incidente se desencadenó al configurar un nuevo proyecto con GitHub Actions y Docker, lo que expuso dos problemas independientes que se combinaron:

1. Un fallo en el healthcheck del contenedor `restart-labs-docs` causado por la resolución IPv6 de `localhost` en Alpine Linux.
2. El firewall de **infraestructura de Hostinger** bloqueaba todos los puertos externos antes de que el tráfico llegara al sistema operativo del VPS.

---

## 🔍 Problemas identificados

### Problema 1 — Contenedor en estado `unhealthy`

**Síntoma:** `docker ps` mostraba el contenedor `restart-labs-docs` con estado `Up X minutes (unhealthy)`.

**Causa raíz:**
El healthcheck estaba configurado con `http://localhost/`. En imágenes basadas en Alpine Linux, la resolución de `localhost` devuelve `::1` (IPv6). Sin embargo, nginx solo escuchaba en IPv4 (`0.0.0.0:80`), por lo que la conexión siempre fallaba y el contenedor nunca pasaba a estado `healthy`.

**Solución:** Cambiar `localhost` por `127.0.0.1` explícito en el healthcheck:

```yaml
healthcheck:
  test: ["CMD", "wget", "-q", "--spider", "http://127.0.0.1/"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 15s
```

---

### Problema 2 — Firewall de infraestructura Hostinger bloqueando todos los puertos

**Síntoma:** Ningún proyecto del VPS respondía desde el exterior (timeouts en `http://IP:80`, `http://IP:81`, `http://IP:443`, SSH).

**Lo que NO era la causa:**
- Las reglas de `nftables` (firewall del SO) eran correctas.
- Docker creaba sus propias cadenas de iptables/nftables correctamente.
- El contenedor nginx respondía bien desde dentro del VPS (`curl http://127.0.0.1:8080`).
- El VPS tenía conectividad saliente (ping a `8.8.8.8` funcionaba).

**Causa raíz:**
Hostinger gestiona un **firewall de infraestructura** (capa de red) separado del firewall del sistema operativo. Este firewall actúa antes de que el tráfico llegue al VPS. Por defecto, todos los puertos estaban bloqueados.

**Solución:** Crear un firewall en el panel de Hostinger con las siguientes reglas:

| Puerto | Protocolo | Acción  | Uso |
|--------|-----------|---------|-----|
| 22     | TCP       | ACEPTAR | SSH |
| 80     | TCP       | ACEPTAR | HTTP |
| 81     | TCP       | ACEPTAR | Nginx Proxy Manager UI |
| 443    | TCP       | ACEPTAR | HTTPS |
| —      | ICMP      | ACEPTAR | Ping / diagnóstico |

---

### Problema 3 — Hostinger deploy API no clona el repositorio completo

**Síntoma:** Al crear el proyecto con la API de Hostinger, el contenedor fallaba al iniciar porque no encontraba el `Dockerfile` ni el código fuente.

**Causa raíz:**
La API `VPS_createNewProjectV1` de Hostinger solo copia el archivo `docker-compose.yml`. No clona el repositorio completo. Por lo tanto, la directiva `build: context: .` en el compose fallaba porque el `Dockerfile` no existía en el servidor.

**Solución:** Separar build y deploy:
1. GitHub Actions construye la imagen Docker y la publica en GHCR (GitHub Container Registry).
2. El `docker-compose.yml` usa `image: ghcr.io/verastian/restart-aws-labs:latest` en lugar de `build: context: .`.
3. El VPS solo necesita descargar la imagen pre-construida.

---

## ✅ Solución final implementada

### Arquitectura del flujo de despliegue

```
GitHub (push a main)
       │
       ▼
GitHub Actions
  ├─ Checkout del repositorio
  ├─ Login a GHCR
  ├─ docker build + push → ghcr.io/verastian/restart-aws-labs:latest
  └─ Hostinger deploy API → copia docker-compose.yml al VPS
              │
              ▼
     VPS Hostinger (147.93.10.106)
       docker compose up -d
              │
              ▼
  restart-labs-docs:80 ──→ red nginx-proxy (externa)
              │
              ▼
  Nginx Proxy Manager
  reverse proxy con SSL
              │
              ▼
  https://restart-labs.devera.cloud
```

### Configuración final del `docker-compose.yml`

```yaml
services:
  docs:
    image: ghcr.io/verastian/restart-aws-labs:latest
    container_name: restart-labs-docs
    ports:
      - "8080:80"
    restart: always
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://127.0.0.1/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 15s
    networks:
      - nginx-proxy

networks:
  nginx-proxy:
    external: true
```

> **Importante:** La red `nginx-proxy` es propiedad del proyecto Nginx Proxy Manager. Siempre debe declararse como `external: true`. Si se redefine como una red nueva, Docker intentará eliminar y recrear la red, lo que fallará si hay otros contenedores conectados (n8n, postgres, etc.).

### Configuración de Nginx Proxy Manager (UI)

Para agregar el proxy host desde la interfaz web de NPM (`http://IP:81`):

| Campo | Valor |
|-------|-------|
| Domain Names | `restart-labs.devera.cloud` |
| Scheme | `http` |
| Forward Hostname / IP | `restart-labs-docs` |
| Forward Port | `80` |
| Block Common Exploits | ✅ |

> Se usa el nombre del contenedor (`restart-labs-docs`) como hostname ya que ambos contenedores comparten la red `nginx-proxy`. Docker resuelve automáticamente el nombre al IP interno del contenedor.

En la pestaña **SSL:**

| Campo | Valor |
|-------|-------|
| SSL Certificate | Request a new SSL Certificate |
| Force SSL | ✅ |
| HTTP/2 Support | ✅ |
| Email | verastian0908@gmail.com |
| I Agree to ToS | ✅ |

---

## 🔧 Comandos de diagnóstico

### Verificar estado de los contenedores

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

Respuesta esperada (servicio sano):

```
NAMES                    STATUS                    PORTS
restart-labs-docs        Up 2 hours (healthy)      0.0.0.0:8080->80/tcp
```

---

### Inspeccionar el estado de salud del contenedor

```bash
docker inspect --format='{{.State.Health.Status}}' restart-labs-docs
```

Respuesta esperada: `healthy`

---

### Verificar que nginx responde dentro del contenedor

```bash
docker exec restart-labs-docs wget -q --spider http://127.0.0.1/
echo "Código de salida: $?"
```

Respuesta esperada: `Código de salida: 0`

---

### Revisar los logs del contenedor

```bash
docker logs restart-labs-docs --tail 30
```

Respuesta esperada (nginx iniciado correctamente):

```
/docker-entrypoint.sh: Configuration complete; ready for start up
```

---

### Verificar la red nginx-proxy y sus contenedores

```bash
docker network inspect nginx-proxy --format='{{range .Containers}}{{.Name}} {{end}}'
```

Respuesta esperada: lista de nombres de contenedores conectados, incluyendo `restart-labs-docs`.

---

### Probar acceso HTTP desde el VPS

```bash
curl -I http://127.0.0.1:8080
```

Respuesta esperada:

```
HTTP/1.1 200 OK
Server: nginx/1.27.x
```

---

### Verificar las reglas de firewall del SO (nftables)

```bash
nft list ruleset | grep -A5 "chain DOCKER"
```

Respuesta esperada: cadenas Docker con reglas de MASQUERADE y ACCEPT para el tráfico de contenedores.

---

### Verificar conectividad saliente del VPS

```bash
ping -c 3 8.8.8.8
```

Respuesta esperada: 3 paquetes enviados, 3 recibidos, 0% pérdida.

---

### Verificar IP pública del VPS

```bash
curl -4 ifconfig.me
```

Respuesta esperada: `147.93.10.106` (o la IP actual del VPS).

---

### Limpiar caché DNS local (Windows — desde CMD)

```cmd
ipconfig /flushdns
```

Respuesta esperada: `Vaciado correctamente la caché de resolución DNS.`

---

### Ver todos los proyectos Docker activos en el VPS

```bash
docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"
```

Respuesta esperada: lista con todos los contenedores y su estado.

---

## 📋 Lecciones aprendidas

| # | Lección | Detalle |
|---|---------|---------|
| 1 | **Alpine Linux resuelve `localhost` como IPv6** | Usar siempre `127.0.0.1` en healthchecks de imágenes Alpine. |
| 2 | **Hostinger tiene dos capas de firewall independientes** | El firewall de infraestructura (panel Hostinger) bloquea antes de llegar al SO. El `nftables` del SO y el de Hostinger son independientes. |
| 3 | **Hostinger deploy API ≠ git clone** | La API solo copia el `docker-compose.yml`. Siempre usar imágenes pre-construidas en un registry (GHCR, Docker Hub). |
| 4 | **Red `nginx-proxy` es `external: true`** | Esta red pertenece al proyecto NPM. Otros proyectos deben unirse con `external: true`, nunca redefinirla. |
| 5 | **Caché DNS local** | Si el sitio funciona desde datos móviles pero no desde WiFi, el problema puede ser caché DNS en el cliente. |
| 6 | **Snapshot como plan de recuperación** | Mantener un snapshot reciente del VPS permite restaurar el estado anterior si los cambios rompen el entorno. |
