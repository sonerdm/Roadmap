# Bind mounts
 
When you use a [bind mount](https://docs.docker.com/storage/bind-mounts), a file or directory on the host machine is mounted into a container. The file or directory is referenced by its absolute path on the host machine. By contrast, when you use a volume, a new directory is created within Docker’s storage directory on the host machine, and Docker manages that directory’s contents.

With the below command we just pull the image from docker hub and forward to host port(8080) to docker port(80) 
```
docker run -d -p 8080:80 nginx
```
In the below command we use Dockerfile and our Html file to serve on the Nginx server.
```
docker run -d -p 8001:80 -v /home/soner/GitHub/Roadmap/Volume-Bind_Mount-Basic_Docker_Compose/nginx-html-test:/usr/share/nginx/html nginx
```