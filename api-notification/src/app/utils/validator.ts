import * as yup from 'yup';

import { NotificationTemplate } from '../@types/enum';

const emailSchema = yup.object().shape({
  recipients: yup.array().of(yup.string().email()).min(1),
});

const slackSchema = yup.object().shape({
  recipients: yup.array().of(yup.string()).min(1),
});

const notificationSchema = yup.object().shape({
  template: yup.mixed().oneOf(Object.values(NotificationTemplate)).required(),
  channels: yup
    .object()
    .shape({
      email: emailSchema,
      slack: slackSchema,
    })
    .required(),
});

export { notificationSchema };
