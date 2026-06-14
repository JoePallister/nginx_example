We can hit the first app on 

http://localhost:8080/app1/

The nginx block in the compose maps "8080:80" so we are hitting the internal nginx port 80.

nginx config has a corresponing

listen 80

The other blocks in the config look like

location /app1/ {
    proxy_pass http://app1:8000/;
}

Here 

location /app1/

means "look for routes that start with /app1/"

We then have

proxy_pass http://app1:8000/;

which tells us where to send it, app1 (since everything is on the same docker network) at port 8000 (8000 is currently hardcoded in the py files). 
nginx strips out the /app1/ and just sends the rest, so

/app1/get_events -> get_events
