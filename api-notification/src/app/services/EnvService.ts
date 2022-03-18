import * as dotenv from 'dotenv';

import Logger from '../lib/logger';

class EnvService {
  get(key: string) {
    try {
      dotenv.config({
        path: `.env.${process.env.NODE_ENV}`,
      });

      return process.env[key];
    } catch (e) {
      Logger.error(String(e));
    }
  }

  getNumber(key: string) {
    return Number(this.get(key));
  }

  isDev() {
    return process.env.NODE_ENV === 'dev';
  }

  isProd() {
    return process.env.NODE_ENV === 'prod';
  }
}

export default new EnvService();
