import * as dotenv from 'dotenv';

import system from '../package.json';
import KafkaController from './app/controllers/KafkaController';
import Logger from './app/lib/logger';

class App {
  public constructor() {
    Logger.info(`##################################`);
    Logger.info(`## Server running successfully  ##`);
    Logger.info(`## Version: ${system.version}               ##`);
    Logger.info(`##################################`);

    this.init();
  }

  private async loadEnv(): Promise<void> {
    dotenv.config({
      path: `.env.${process.env.NODE_ENV}`,
    });
  }

  private async init(): Promise<void> {
    this.loadEnv();

    await this.kafka();
  }

  private async kafka(): Promise<void> {
    await KafkaController.init();
  }
}

new App();
