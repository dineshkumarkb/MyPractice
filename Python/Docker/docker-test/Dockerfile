FROM node:alpine as mybuild
WORKDIR /usr/webapp
COPY ./client/package.json ./
RUN npm install 
COPY ./client/ ./
RUN npm run build


FROM nginx
COPY from=mybuild /usr/webapp/build /usr/share/nginx/html