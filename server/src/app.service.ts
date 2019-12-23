import { Injectable, Logger } from '@nestjs/common';
import * as amqp from 'amqplib';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }

  async getPlan(planConfig): Promise<any> {
    const open = amqp.connect('amqp://localhost');

    return await open.then(conn => {
      return conn
        .createChannel()
        .then(ch => {
          ch.assertQueue('simulations', { durable: false });
          ch.assertQueue('results', { durable: false });
          ch.sendToQueue('simulations', Buffer.from(JSON.stringify(planConfig)));

          return new Promise((resolve, reject) => {
            ch.consume('results', msg => {
              if (msg) {
                return resolve(msg.content.toString());
              }
            });
          });
        })
        .then(plan => {
          setTimeout(() => {
            conn.close();
          }, 500);
          return plan;
        })
        .catch(Logger.warn);
    });
  }
}
