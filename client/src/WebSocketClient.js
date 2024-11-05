import WebSocket from 'websocket';

class WebSocketClient {
  
  constructor(url) {
    this.url = url;
    this.client = null;
  }

  connect() {
    this.client = new WebSocket.client();

    this.client.on('open', () => {
      console.log('WebSocket connection opened');
    });

    this.client.on('close', () => {
      console.log('WebSocket connection closed');
    });

    this.client.on('error', (error) => {
      console.error('WebSocket error:', error);
    });

    this.client.on('connect', () => {
      console.log('WebSocket connected');
    });

    this.client.on('message', (message) => {
      console.log('Received message:', message.utf8Data);
    });

    this.client.connect(this.url);
  }

  send(data) {
    if (this.client.connected) {
      this.client.send(data);
    }
  }

  disconnect

() {
    if (this.client.connected) {
      this.client.close();
    }
  }
}

export default WebSocketClient;