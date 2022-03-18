import json
import random
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
        # create_deploy(producer)
        create_notification(producer)
        print('Sent job number:', i)


def create_deploy(producer: KafkaProducer):
    key = str(uuid4())
    payload = {
        'asset_id': random.sample(range(0, 1000), 1)[0],
        'current_commit': str(uuid4()),
        'previous_commit': str(uuid4()),
    }

    producer.send(
        'create-deploy',
        payload,
        key=str(key).encode('UTF-8'),
    )


def create_notification(producer: KafkaProducer):
    key = str(uuid4())
    payload = {
        'template': 'recover-password',
        'channels': {
            'email': {
                'recipients': ['fagisij754@siberpay.com'],
            }
        },
        'data': {
            'ma': 'oeeeee'
        },
    }

    producer.send(
        'notification',
        payload,
        key=str(key).encode('UTF-8'),
    )


if __name__ == '__main__':
    create_jobs()
