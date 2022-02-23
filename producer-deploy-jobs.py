import json
import sys
from kafka import KafkaProducer
from uuid import uuid4


MAX_DEPLOYS = int(sys.argv[1])


def create_jobs():
    producer = KafkaProducer(
        bootstrap_servers='192.168.15.113:9094',
        client_id='tmp-producer',
        compression_type='gzip',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )

    for i in range(MAX_DEPLOYS):
        create_deploy(producer)
        print('Sent job number:', i)


def create_deploy(producer: KafkaProducer):
    id = str(uuid4())
    payload = {
        'id': id,
    }
    producer.send(
        'create-deploy',
        payload,
        key=str(id).encode('UTF-8'),
    )


if __name__ == '__main__':
    create_jobs()
