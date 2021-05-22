# Basic demo with Python, Docker, Nginx

**On flask_app1 folder:**
```
docker build . -t web_app1
docker run -d -p 5001:5000 web_app1
```
**On flask_app2 folder:**
```
docker build . -t web_app2
docker run -d -p 5002:5000 web_app2
```
**On nginx_load_balancer folder:**
```
docker build . -t nginx_load_balancer
docker run -d -p 8080:80 nginx_load_balancer
```
**You can test with via browser or this bash command:**
```
while true; do curl http://localhost:8080 && sleep 2; done;
```
For more;
[Resource](https://alperenhasanselcuk.medium.com/docker-ve-nginx-kullanarak-load-balancer-konfig%C3%BCrasyonu-3aa2fa89e33c)
