
# Bu dockerfile bir NODE.js uygulamasını bir container üzerinde yayınlamak için düzenlenmiştir

# burada node offical image nın alpine branchi kullanılmıstır
FROM node:6-alpine
# Container 80 portundan yayın yapacak ama aslında host üzerinde 3000 portunu dinleyecektir

EXPOSE 3000
# alpine package manager üzerinden tini paketini yüklüyoruz

RUN apk add --update tini
# -  /usr/src/app klasörünü oluşturuyoruz'
RUN mkdir -p /usr/src/app
# package manager kullanarak package.json oluşturuluyor
WORKDIR /usr/src/app
COPY package.json package.json
# bağımlılıkları yüklemek adına npm install komutunu kullanıyoruz 
RUN npm install && npm cache clean

COPY . .
# sonrasında kontainerı ayağa kaldırmak için ilgili komut serisi  kullanılıyor.
CMD ["tini", "--", "node", "./bin/www"]

