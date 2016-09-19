'use strict';

module.exports = {
  name: 'thinkjs',
  type: 'file',
  secret: 'K&1!G4JP',
  timeout: 24 * 3600,
  cookie: { // cookie options
    length: 32,
    httponly: true
  },
  adapter: {
    file: {
      path: think.RUNTIME_PATH + '/session',
    }
  }
}