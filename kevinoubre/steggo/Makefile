hello:
	echo "Steg thing go fast"

build:
	go build -o bin/cracksteg cracksteg.go
	go build -o bin/steg steg.go

compile:
	echo "Compiling for every OS and Platform"
	GOOS=linux GOARCH=amd64 go build -o bin/cracksteg-linux cracksteg.go
	GOOS=windows GOARCH=amd64 go build -o bin/cracksteg-windows cracksteg.go
