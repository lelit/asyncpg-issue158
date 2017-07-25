set -x

docker build -t issue158 .


pg9c=`docker run --name pg9 -e POSTGRES_USER=pgu -e POSTGRES_PASSWORD=ugp -d postgres:9.6.3`

docker run --rm -ti --link pg9:pg issue158 pg

docker stop $pg9c
docker rm -v $pg9c


pg10c=`docker run --name pg10 -e POSTGRES_USER=pgu -e POSTGRES_PASSWORD=ugp -d postgres:10-beta2`

docker run --rm -ti --link pg10:pg issue158 pg

docker stop $pg10c
docker rm -v $pg10c
