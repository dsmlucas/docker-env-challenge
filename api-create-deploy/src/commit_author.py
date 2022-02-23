
from uuid import uuid4

import logger
from kafka_adapter.config import Topic, producer

MAX_AUTHORS = 5


class CommitAuthor():

    @staticmethod
    def create(deploy_id: str):
        try:
            for i in range(MAX_AUTHORS):
                id = str(uuid4())
                payload = {
                    'deploy_id': deploy_id,
                    'name': 'Author name {}'.format(i),
                    'email': 'author{}@test.local'.format(i),
                    'commit': id
                }

                topic = Topic.CREATE_COMMIT_AUTHOR.value
                producer.send(
                    topic=topic,
                    value=payload,
                    key=str(id).encode('UTF-8'),
                )
        except Exception as e:
            error_msg_fmt = 'Unable to submit jobs to topic: {}. {}'
            logger.error(error_msg_fmt.format(topic, e))
