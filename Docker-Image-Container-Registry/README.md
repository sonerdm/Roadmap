# Basic demo with JS and Dockerhub

**Firstly try to build the app and check at localhost:8080**
```
docker build . -t nodejs-demo
docker run --rm -p 8080:3000 nodejs-demo
```

**Create Docker Hub(hub.docker.com) account and login from command line**
```
docker login --username=your_username
docker push nodejs-demo
```

**Delete all related images and try to get the image on Docker Hub**
```
docker run --rm -p 8080:3000 nodejs-demo
```

For more;
[Resource](https://medium.com/aws-certified-user-group-turkey/docker-%C3%BCzerine-genel-bak%C4%B1%C5%9F-image-container-ve-registry-kullan%C4%B1m%C4%B1-c37eba74b203)