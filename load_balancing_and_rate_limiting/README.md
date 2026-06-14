Build the stack with

docker compose up

We should then be able to visit

http://localhost:8080/app1/

http://localhost:8080/app2/

The former requests will be load balanced among the 2 app1 containers, though we shouldn't be able to see this. 

The request should also be rate limited, we can test that with the test_rate_limit.sh script