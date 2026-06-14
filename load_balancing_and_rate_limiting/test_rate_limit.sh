for i in {1..50}; do
  curl -s http://localhost:8080/app1/ &
done
wait