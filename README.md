To start the server run

```bash
docker build . -t raffle:latest
docker run -p 8000:8000 --rm raffle
```

Endpoints

- Generate token
```bash
curl --location --request POST 'localhost:8000/auth/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "admin",
    "password": "admin"
}'
```

- Participate in an Event
```bash
curl --location --request GET 'localhost:8000/raffle/events/10/participate/' \
--header 'Authorization: token 8f4e517becd0f64ef469a6ec5d955e90199f7ac2' \
--header 'Content-Type: application/json'
``` 
   
- Create an event  (Admin auth)
 ```
curl --location --request POST 'localhost:8000/raffle/events/' \
--header 'Authorization: token ba9881f718b87fb77b86a52bc319122182e02b0c' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "test",
    "reward": "machine",
    "date": "2021-06-02"
}'
```

- View winners

```
curl --location --request GET 'localhost:8000/raffle/winners/' \
--header 'Authorization: token 8f4e517becd0f64ef469a6ec5d955e90199f7ac2' \
--header 'Content-Type: application/json' 
```

- Upcoming events

```
curl --location --request GET 'localhost:8000/raffle/events/upcoming/' \
--header 'Authorization: token 8f4e517becd0f64ef469a6ec5d955e90199f7ac2' \
--header 'Content-Type: application/json'
```