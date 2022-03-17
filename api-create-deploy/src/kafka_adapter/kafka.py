from kafka import KafkaConsumer, KafkaAdminClient
from json import loads
from time import sleep

from .config import (
    BROKERS, CLIENT_ID, GROUP_ID, REQUIRED_TOPICS, Topic, producer
)
from commit_author import CommitAuthor
import database
import logger


def consume_topics(node: int):
    logger.info(f'Initializing kafka node {node}')

    try:
        __check_has_topics()

        consumer = KafkaConsumer(
            bootstrap_servers=BROKERS,
            client_id=CLIENT_ID,
            group_id=GROUP_ID,
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            max_poll_records=10,
        )
        consumer.subscribe(REQUIRED_TOPICS)

        logger.info(f'Kafka started successfully {node}')

        for msg in consumer:
            try:
                # TODO - Create 'form' validation

                deploy = database.create_deploy(msg.value)

                CommitAuthor.create(deploy)
            except Exception as e:
                logger.error(f'Error on reading message {e}')
                retry_message(msg, Topic(msg.topic))

    except Exception as e:
        logger.error(f'{e}: {BROKERS}')


def __check_has_topics():
    admin = KafkaAdminClient(bootstrap_servers=BROKERS)
    existent_topics = admin.list_topics()
    has_topics = False

    while not has_topics:
        has_topics = True

        for topic in REQUIRED_TOPICS:
            existent_topics = admin.list_topics()

            if topic not in existent_topics:
                has_topics = False
                logger.warn(f'Waiting for topic be created: {topic}')
                sleep(10)


def retry_message(msg, topic: Topic):
    retries = 0
    if msg.headers:
        for header in msg.headers:
            if header[0] == 'error_retries':
                retries = int(header[1]) + 1
    else:
        retries = 1

    if retries > 3:
        return

    logger.debug('Retrying {}'.format(retries))

    producer.send(
        topic=topic.value,
        value=msg.value,
        key=msg.key,
        headers=[('error_retries', str(retries).encode())]
    )
