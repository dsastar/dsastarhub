builder="ansoncar"
projectName="dsastar"
version="1"
port="3000"

image=$builder/$projectName:v$version

docker build -t $iamge .
docker run -p $port:$prot $image

# docker tag ansoncar/atomt:v$1 ansoncar/atomt:v$1
# docker build --platform linux/amd64 -t ansoncar/atomt:v$1 .
# docker push ansoncar/atomt:v$1

# docker pull ansoncar/atomt:v3.2.3
# docker run -d -p 5004:5004 ansoncar/atomt:v3.2.3
