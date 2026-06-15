Build the stack with

docker compose up

We should then be able to visit

http://localhost:8080/app1/

http://localhost:8080/app2/

This example has proxy_set_header Host $host; for one of the apps, this passes the client host ip 
on to the app in a header (so we see Host: localhost in our printed header). If we visit app2 (which doesn't have proxy_set header) we just see Host: app2:8000
