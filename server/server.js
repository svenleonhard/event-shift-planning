var express = require('express');
var app = express();
app.listen(3000, function () {
  console.log('server running on port 3000');
})

var amqp = require('amqplib/callback_api');
app.get('/plan', call_shift_planning);

function call_shift_planning(req, res) {
  var input = [
    req.query.funds, // starting funds
    req.query.size, // (initial) wager size
    req.query.count, // wager count — number of wagers per sim
    req.query.sims // number of simulations
  ]
  amqp.connect('amqp://localhost', function (err, conn) {
    conn.createChannel(function (err, ch) {
      var simulations = 'simulations';
      ch.assertQueue(simulations, { durable: false });
      var results = 'results';
      ch.assertQueue(results, { durable: false });
      ch.sendToQueue(simulations, Buffer.from(JSON.stringify(input)));
      ch.consume(results, function (msg) {
        res.send(msg.content.toString())
      }, { noAck: true });
    });
    setTimeout(function () { conn.close(); }, 500); 
    });
}