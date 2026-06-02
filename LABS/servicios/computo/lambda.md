---
sidebar_position: 2
title: AWS Lambda
---

# AWS Lambda

AWS Lambda es un servicio de cómputo **sin servidor (serverless)** que ejecuta código en respuesta a eventos, gestionando automáticamente la infraestructura subyacente.

## ¿Cómo funciona?

```
Evento → Trigger → Función Lambda → Respuesta
```

1. Se sube el código (función) con su configuración
2. Se define un **trigger** — el evento que la invoca
3. Lambda escala automáticamente según la demanda
4. Se paga únicamente por el tiempo de ejecución real

## Conceptos clave

### Función
Unidad de despliegue. Contiene el código, el runtime y la configuración de memoria/timeout.

### Triggers (Disparadores)

| Trigger | Evento |
|---------|--------|
| **API Gateway** | Petición HTTP/REST |
| **S3** | Archivo subido, modificado o eliminado |
| **DynamoDB Streams** | Cambio en una tabla |
| **EventBridge** | Regla programada (tipo cron) |
| **SNS / SQS** | Mensaje en cola o tópico |
| **Cognito** | Evento de autenticación |

### Runtimes disponibles
Python, Node.js, Java, Go, Ruby, .NET y custom runtimes.

### Límites importantes

| Parámetro | Límite |
|-----------|--------|
| Tiempo máximo de ejecución | 15 minutos |
| Memoria configurable | 128 MB – 10 GB |
| Tamaño del paquete (zip) | 50 MB |
| Tamaño descomprimido | 250 MB |
| Concurrencia por defecto | 1,000 ejecuciones simultáneas |

## Modelo de precios

- **Capa gratuita:** 1 millón de solicitudes/mes y 400,000 GB-segundo/mes
- **Solicitudes adicionales:** $0.20 por millón
- **Duración:** $0.0000166667 por GB-segundo

> Lambda suele ser la opción más económica para cargas con tráfico irregular o bajo.

## Diferencias con EC2

| Característica | EC2 | Lambda |
|----------------|-----|--------|
| Gestión del servidor | Usuario | AWS |
| Escalado | Manual / Auto Scaling | Automático |
| Disponibilidad | Continua | Solo al ejecutarse |
| Tiempo máximo | Ilimitado | 15 minutos |
| Facturación | Por hora/segundo activo | Por milisegundo de ejecución |

## Casos de uso
- APIs y backends ligeros
- Procesamiento de eventos en tiempo real (S3, Kinesis)
- Automatización y scripts programados
- Transformación de datos ETL
- Chatbots e integraciones con servicios externos
