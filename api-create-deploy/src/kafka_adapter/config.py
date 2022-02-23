import json
from kafka import KafkaProducer
from enum import Enum
from os import getenv

# from kafka.coordinator.assignors.roundrobin import RoundRobinPartitionAssignor

# Handle name assign to be equal on nodejs
# RoundRobinPartitionAssignor.name = 'RoundRobinAssigner'


class Topic(Enum):
    CREATE_DEPLOY = 'create-deploy'
    CREATE_COMMIT_AUTHOR = 'create-commit-author'


__BROKER1 = f'{getenv("KAFKA_HOST")}:{getenv("KAFKA_PORT")}'

BROKERS = [__BROKER1]
CLIENT_ID = 'api-create-deploy'
GROUP_ID = 'group-create-deploy'  # or 'g-create-deploy'
# PARTITIONS = [RoundRobinPartitionAssignor]
REQUIRED_TOPICS = [
    Topic.CREATE_DEPLOY.value
]


producer = KafkaProducer(
    bootstrap_servers=BROKERS,
    client_id=CLIENT_ID,
    compression_type='gzip',
    retries=3,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)
