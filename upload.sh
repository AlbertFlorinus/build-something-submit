docker build -t albertflorinus/book-app:latest -f book/Dockerfile ./book
docker build -t albertflorinus/book-db:latest -f db/Dockerfile ./db
docker build -t albertflorinus/book-auth:latest -f book-auth/Dockerfile ./book-auth

docker push albertflorinus/book-app:latest
docker push albertflorinus/book-db:latest
docker push albertflorinus/book-auth:latest