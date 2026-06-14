Can see from the default.conf this has rate limiting and load balacing, with a cluster of two server1:

upstream app1_cluster {
    server app1a:8000;
    server app1b:8000;
}

There are two because we have two compose blocks using the same image.

The def for the limiting is

limit_req_zone $binary_remote_addr zone=api_limit:10m rate=5r/s;

Here $binary_remote_addr is the address of the client, this means each client is rate limited separately. 

zone=api_limit:10m zone here is a memory zone, api_limit is the name and 10m = 10mb, the size we allocate

rate=5r/s is allowing up to 5 requests per second