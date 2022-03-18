import { admin, consumer, producer, Topic } from '../lib/kafka';
import Logger from '../lib/logger';
import sleep from '../lib/sleep';
import NotificationService from '../services/NotificationService';

const scanTopics = [Topic.NOTIFICATION];

class KafkaController {
  async init() {
    try {
      Logger.info('Initializing kafka');

      let hasTopics = false;

      while (!hasTopics) {
        const existentTopics = await admin.listTopics();

        hasTopics = true;

        scanTopics.map(t => {
          if (!existentTopics.includes(t)) {
            hasTopics = false;
            Logger.warn(`Waiting for topic be created: ${t}`);
          }
        });

        await sleep(5);
      }

      await producer.connect();
      await consumer.connect();

      for (const topic of scanTopics) {
        await consumer.subscribe({ topic: topic });
      }

      await consumer.run({
        autoCommitInterval: 1000,
        // autoCommitThreshold: 10,

        eachMessage: async ({ topic, message }) => {
          const value = message.value as never;

          try {
            const data = JSON.parse(value) as NotificationType;

            // throw Error('On error always retry');

            if (scanTopics.includes(<Topic>topic)) {
              if (topic === Topic.NOTIFICATION) {
                await NotificationService.run(data);
              }
            }
          } catch (e) {
            Logger.error(String(e));
            throw e;
          }
        },
      });

      Logger.info('Kafka started successfully');
    } catch (e) {
      Logger.error(String(e));
    }
  }
}

export default new KafkaController();
