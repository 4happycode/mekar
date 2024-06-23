# Stage 1: Build the Vue.js application
FROM node:14 as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve the Vue.js application with a production-ready web server
FROM nginx:1.21.3-alpine
COPY --from=build-stage /app/dist /usr/share/nginx/html
# COPY .env /app           # Copy .env into the Docker image
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]