#!/bin/bash
docker-compose exec kafka  \
bash -c "seq 100 | kafka-console-producer --request-required-acks 1 --broker-list localhost:29092 --topic org.waelson.app.views && echo 'Produced 100 messages.'"