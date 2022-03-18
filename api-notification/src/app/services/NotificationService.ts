import { ValidationError } from 'yup';

import EmailController from '../controllers/EmailController';
import Logger from '../lib/logger';
import { notificationSchema } from '../utils/validator';

class NotificationService {
  async run(data: NotificationType) {
    try {
      await notificationSchema.validate(data);

      await EmailController.send(data);
    } catch (e) {
      if (e instanceof ValidationError) {
        Logger.error(String(e));
      } else {
        throw e;
      }
    }
  }
}

export default new NotificationService();
