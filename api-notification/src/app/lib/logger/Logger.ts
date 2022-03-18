/* eslint-disable no-console */
import date from '../../utils/date';

class Logger {
  private reset = '\x1b[0m';
  private bright = '\x1b[1m';

  private black = '\x1b[30m';
  private red = '\x1b[31m';
  private green = '\x1b[32m';
  private yellow = '\x1b[33m';
  private blue = '\x1b[34m';
  private magenta = '\x1b[35m';
  private cyan = '\x1b[36m';
  private white = '\x1b[37m';

  info(message?: string) {
    console.log(
      `${this._get_date()} - ${this.bright}${this.green}[info]${this.reset}:`,
      message,
    );
  }

  warn(message?: string) {
    console.log(
      `${this._get_date()} - ${this.bright}${this.yellow}[warn]${this.reset}:`,
      message,
    );
  }

  error(message?: string) {
    console.log(
      `${this._get_date()} - ${this.bright}${this.red}[error]${this.reset}:`,
      message,
    );
  }

  debug(message?: string) {
    console.log(
      `${this._get_date()} - ${this.bright}${this.white}[white]${this.reset}:`,
      message,
    );
  }

  private _get_date() {
    return date.format(new Date());
  }
}

export default new Logger();
