import { createQueue } from "kue";
import { createClient } from "redis";


const queue = createQueue({
    redis: {
        createClientFactory: () => createClient()
    }
});

const job = {
    phoneNumber: '0173943892',
    message: 'this is a message'
};


queue.process('push_notification_code');

queue.create('push_notification_code', job).save();

queue.on('job enqueue', (id) => {
    console.log(`Notification job created: ${id}`);
});

queue.on('job complete', (id) => {
    console.log(`Notification job ${id} completed`);
});

queue.on('job failed', (id, result) => {
    console.log('Notification job failed');
});