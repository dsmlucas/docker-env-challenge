import { Kafka, logLevel } from 'kafkajs';

import EnvService from '../../services/EnvService';

const kafkaId = EnvService.get('KAFKA_CLIENT_ID');
const kafkaHost = EnvService.get('KAFKA_HOST');
const kafkaPort = EnvService.getNumber('KAFKA_PORT');

const kafka = new Kafka({
  brokers: [`${kafkaHost}:${kafkaPort}`],
  clientId: kafkaId,
  logLevel: logLevel.ERROR,
  retry: {
    initialRetryTime: 1000,
    retries: 5,
  },
});

const admin = kafka.admin();
const consumer = kafka.consumer({ groupId: 'g-api-notification' });
const producer = kafka.producer();

enum Topic {
  NOTIFICATION = 'notification',
}

export { admin, consumer, producer, Topic };
