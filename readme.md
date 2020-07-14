# Mocking API Service with Wiremock & Charles Proxy

## Summary
This repository consists of two services [fruit](./fruit) and [botanical](./botanical) to illustrate and demo how to mock APIs. Both service can be built and run with docker. The [wiremock](./wiremock-docker) directory consists of sample mock API responses for [fruit](./wiremock-docker/samples/fruit) and [botanical](./wiremock-docker/samples/botanical)


## Getting started

#### Botanical Service
The service takes a fruit id and returns the botanical name of the fruit. > The service only returns botanical name for fruit with id 1

##### (1) Build Botanical Service
```sh
cd botanical
docker build -t botanical .
docker run -d -p 5000:5000 botanical
```
> Access [http://localhost:5000/api/v1/botanical?id=1](http://localhost:5000/api/v1/botanical?id=1) to view a sample response

### NOTE: Run botanical service and fruit service on different servers to illustrate mocking different services on different instances

#### Fruit Service
This service takes an id and returns a fruit
- `api/v1/fruits` return name, id, benefit and calories for a fruit
- `api/v2/fruits` call botanical service and returns name, id, benefit, calories and botanical_name for a fruit.

##### Build and run Fruit Service
```sh
cd fruit
docker build -t fruit .
docker run -d -p 5000:5000 -e "BOTANICAL_SERVICE_URL=<<ENTER-BOTANICAL-HOST>>/api/v1" fruit
```
> Access [http://localhost:5000/api/v1/fruits?id=1](http://localhost:5000/api/v1/fruits?id=1) to view a sample response

#### Wiremock docker
- Clone [wiremock docker repository](https://github.com/rodolpheche/wiremock-docker)
- Copy folders in [wiremock/samples](wiremock/samples) to wiremock-docker
```sh
cp -rf wiremock/samples/botanical wiremock-docker/samples
cp -rf wiremock/samples/fruit wiremock-docker/samples
```

##### Build and run wiremock-botanical
```sh
cd wiremock-docker
docker build -t wiremock-botanical samples/botanical
docker run -it --rm -p 8080:8080 wiremock-botanical
```

##### Build and run wiremock-fruit
```sh
cd wiremock-docker
docker build -t wiremock-fruit samples/fruit
docker run -it --rm -p 8081:8081 wiremock-fruit
```

#### Testing with wiremock
- To test with wiremock, you can change the botanical service url to point to wiremock-botanical [http://localhost:8080/api/v1/botanical](http://localhost:8080/api/v1/botanical)
- Alternatively, you can use [Charles Proxy](https://www.charlesproxy.com/) to forward requests for a specific id from botanical service to wiremock-botanical
    - To make Charles setting got to **_Tools_** -> **_Map Remote_** -> **_Add_**
    - ![Charles setting](https://github.com/seunoluwaloju/mock-api-demo/blob/master/charles/map-remote-settings.png?raw=true)