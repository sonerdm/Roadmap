FROM golang:1.17-alpine as build
WORKDIR /app
COPY go.mod ./
RUN go mod download
COPY . .
RUN go build -o main .

FROM alpine
COPY --from=build /app/main .
CMD ["./main"]