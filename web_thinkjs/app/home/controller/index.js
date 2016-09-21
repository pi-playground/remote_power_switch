'use strict';

var Base = require('./base.js');
var powerStatus = 'off'

var amqp = require('amqplib/callback_api');
var _ch = null;
var q = 'remote_power_switch';

function sendMsg(msg){
    _ch.sendToQueue(q, new Buffer(msg));
    console.log(" [x] Sent %s", msg);
}
amqp.connect('amqp://rabbitmq.dev.twleansw.com', function(err, conn) {
  conn.createChannel(function(err, ch) {
    ch.assertQueue(q, {durable: false});
    // Note: on Node 6 Buffer.from(msg) should be used
    _ch = ch ;
    console.log(_ch)

  });
});

module.exports = think.controller(Base, {
  /**
   * index action
   * @return {Promise} []
   */
  indexAction: function(self){
    //auto render template file index_index.html
  	this.assign("title", "Remote Power Switch By ThinkJS");
  	this.assign("powerStatus", powerStatus);
    return self.display();
  },
  onAction: function(self){
    //auto render template file index_index.html
  	powerStatus="on";
  	sendMsg('POWER_ON');
  	this.redirect("/");
  },
  offAction: function(self){
    //auto render template file index_index.html
  	
  	powerStatus="off";
  	sendMsg('POWER_OFF');
  	this.redirect("/");
  }
});