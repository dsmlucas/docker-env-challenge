from concurrent.futures import ThreadPoolExecutor
import multiprocessing

from kafka_adapter import consume_topics
import database
import logger


CPUS = multiprocessing.cpu_count()


def init_tasks():
    with ThreadPoolExecutor() as executor:
        for i in range(CPUS):
            executor.submit(consume_topics, i)


if __name__ == '__main__':
    try:
        database.init()
        init_tasks()
    except Exception as e:
        logger.error(e)
        raise e
