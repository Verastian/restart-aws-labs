# ── Stage 1: Build ──────────────────────────────────────────
FROM node:20-alpine AS builder

WORKDIR /app

# Copiar dependencias primero para aprovechar cache de Docker
COPY website/package*.json ./website/
RUN cd website && npm ci --prefer-offline

# Copiar contenido de labs y el sitio web
COPY LABS/ ./LABS/
COPY website/ ./website/

# Build estático de Docusaurus
RUN cd website && npm run build

# ── Stage 2: Serve ──────────────────────────────────────────
FROM nginx:1.27-alpine

# Copiar build generado
COPY --from=builder /app/website/build /usr/share/nginx/html

# Copiar configuración de nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
