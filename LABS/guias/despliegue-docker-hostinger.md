---
sidebar_position: 2
title: Despliegue en Hostinger con Docker
---

# Despliegue en Hostinger con Docker

Guía para desplegar esta documentación en un VPS de Hostinger usando Docker Compose y Nginx Proxy Manager.

## Prerrequisitos

- VPS de Hostinger con Docker Manager habilitado
- Dominio apuntando al VPS (registro `A` en DNS)
- Repositorio en GitHub con `Dockerfile` y `docker-compose.yml`

## 1. Configurar el registro DNS

En **hPanel → Dominios → DNS Records**, agregar:

| Campo | Valor |
|-------|-------|
| Type | `A` |
| Name | `restart-labs` (subdominio deseado) |
| Points to | IP pública del VPS |
| TTL | `3600` |

Verificar propagación en [dnschecker.org](https://dnschecker.org).

## 2. Desplegar desde GitHub con Docker Manager

1. En **hPanel → VPS → Docker**, ir a **Docker Compose**
2. Seleccionar **Deploy from URL**
3. Pegar la URL del `docker-compose.yml` en GitHub:
   ```
   https://github.com/<usuario>/<repo>/blob/main/docker-compose.yml
   ```
4. Hacer clic en **Deploy**

El proceso clona el repositorio, construye la imagen (multi-stage) y levanta el contenedor. El build tarda ~2–3 minutos.

### Verificar que el contenedor está corriendo

Desde SSH:

```bash
docker ps
```

La salida debe mostrar el contenedor `restart-labs-docs` con estado `Up` y el puerto `8080` expuesto.

## 3. Configurar el reverse proxy (Nginx Proxy Manager)

Nginx Proxy Manager ya viene desplegado en el VPS de Hostinger. Acceder al panel:

```
http://<IP-del-VPS>:32774
```

### Agregar Proxy Host

1. Ir a **Proxy Hosts → Add Proxy Host**
2. Completar la pestaña **Details:**

| Campo | Valor |
|-------|-------|
| Domain Names | `restart-labs.devera.cloud` |
| Scheme | `http` |
| Forward Hostname/IP | `172.17.0.1` |
| Forward Port | `8080` |
| Block Common Exploits | ✅ Activado |

> `172.17.0.1` es la IP del host Docker, accesible desde dentro de la red de contenedores.

3. Ir a la pestaña **SSL:**

| Campo | Valor |
|-------|-------|
| SSL Certificate | Request a new SSL Certificate |
| Force SSL | ✅ Activado |
| HTTP/2 Support | ✅ Activado |
| Email | tu@email.com |
| I Agree to ToS | ✅ |

4. Hacer clic en **Save**

NPM solicita el certificado a Let's Encrypt automáticamente y recarga nginx.

## 4. Verificar el despliegue

Acceder en el navegador a:

```
https://restart-labs.devera.cloud
```

El sitio debe cargar con HTTPS activo (candado en el navegador).

## Actualizar el sitio

Cuando se realicen cambios en el repositorio, volver a Docker Manager y hacer **Redeploy** del compose. El proceso reconstruye la imagen con el contenido actualizado.
