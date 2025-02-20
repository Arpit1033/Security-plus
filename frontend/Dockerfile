# Stage 0: Build the Vite app
FROM node:18-alpine as build

# Set working directory
WORKDIR /app

# Copy dependency files first for caching
COPY package.json package-lock.json* ./

# Install dependencies (if you're using yarn, change accordingly)
RUN npm install

# Copy the rest of your source files
COPY . .

# Build the app; this generates the production assets in the "dist" folder
RUN npm run build

# Stage 1: Serve with Nginx
FROM nginx:alpine

# Remove default Nginx static assets
RUN rm -rf /usr/share/nginx/html/*

# Copy built assets from the build stage into Nginx's static folder
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 for the container
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
