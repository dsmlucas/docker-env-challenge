import nodemailer from 'nodemailer';
import { Options } from 'nodemailer/lib/smtp-transport';

import Logger from '../lib/logger';

class EmailController {
  async send(data: NotificationType) {
    try {
      const conf = this._getConf();
      const transporter = nodemailer.createTransport(conf);

      const info = await transporter.sendMail({
        from: conf.auth?.user,
        to: data.channels.email?.recipients,
        subject: 'Hello',

        // TODO - Test if use text or html
        // text: 'Hello world1?',
        html: '<b>Hello world2?</b>',
      });

      Logger.debug(info.messageId);
    } catch (e) {
      Logger.error(String(e));
    }
  }

  private _getConf() {
    const conf: Options = {
      host: process.env.SMTP_HOST,
      port: Number(process.env.SMTP_PORT) || 0,
      secure: false,
      requireTLS: true,
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASSWORD,
      },
    };

    return conf;
  }
}

export default new EmailController();
