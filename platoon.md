```
class MyHub {
  constructor(seed) {
    this.seed = seed;
    this.sock = zmq.socket('sub');
  }
 
  async init() {
    this.collection = await this.getCollection();
    return new Promise((res, rej) => {
      res("succ");
    })
  }
  /*  */
}


async transfer(to, value, tag, message) {
  await this.checkIfPending(this.seed);
  let storage = await this.collection.findOne({ seed: this.seed });
  if (storage == null || storage.input == null) {
    await this.getInputs();
    storage = await this.collection.findOne({ seed: this.seed });
  }
  storage.highestKeyIndex++;
  let remainderAddress = await this.getNewAddress(storage.highestKeyIndex, 1);


  return new Promise((res, rej) => {
    let tmp = 0;
    let inputs = [];
    let used = [];
    if (storage.inputs == null) {
      rej(new Error('Insufficient Balance'));
      return;
    }
    if (storage !== undefined && storage != null && storage.inputs.length > 0) {
      let i = 0;
      while (value > tmp && i < storage.inputs.length) {
        if (storage.inputs[i].used == null && storage.inputs[i].used == undefined) {
          tmp += storage.inputs[i].balance;
          inputs.push({
            address: storage.inputs[i].address,
            keyIndex: storage.inputs[i].keyIndex,
            security: storage.inputs[i].security,
            balance: storage.inputs[i].balance
          });
          used.push(i);
        }
        i++;
      }
      if (tmp < value) {
        rej(new Error('Insufficient Balance'));
        return;
      }
    } else {
      rej(new Error('Something went wrong'));
      return;
    }
    const transfers = [{
      address: to,
      value: value,
      tag: tag,
      message: converter.asciiToTrytes(message)
    }];
    const depth = 3;
    const minWeightMagnitude = config.mwm;

    iota.prepareTransfers(this.seed, transfers, { inputs, remainderAddress: remainderAddress[0] })
      .then(trytes => {
        return iota.sendTrytes(trytes, depth, minWeightMagnitude)
      })
      .then(bundle => {
        let pending = [];
        for (let i of used)
          storage.inputs[i].used = bundle[0].hash;
        pending.push({
          address: bundle[bundle.length - 1].address,
          keyIndex: storage.highestKeyIndex,
          security: storage.inputs[inputs.length - 1].security,
          balance: bundle[bundle.length - 1].value,
          used: bundle[0].hash
        })
        this.collection.updateOne({ seed: this.seed }, { '$set': { inputs: storage.inputs, pending:pending, highestKeyIndex: storage.highestKeyIndex } }, (error, result) => {
          res(bundle[0].hash);
          rej(error);
        });
      })
      .catch(err => {
        rej(err);
      })
  });
};

async checkIfPending() {
  let storage = await this.collection.findOne({ seed: this.seed });
  if (storage == null)
    storage = await this.getInputs();
  return new Promise((res, rej) => {
    let tails = [];
    if (storage != null && storage.pending != undefined && storage.pending != null) {
      for (let pending of storage.pending)
        tails.push(pending.used);
    }
    iota.getLatestInclusion(tails).then(states => {
      for (let i = 0; i < tails.length; i++) {
        if (states[i] && storage.inputs != null && storage.inputs != undefined) {
          for (let j = 0; j < storage.inputs.length; j++) {
            if (storage.inputs[i].used === tails[i]) {
              storage.inputs.splice(j, j + 1);
            }
          }
          storage.pending[i].used = null;
          storage.inputs.push(storage.pending[i]);
          storage.pending.splice(i, i + 1);
        }
      }
      this.collection.updateOne({ seed: this.seed }, { '$set': { inputs: storage.inputs, pending:storage.pending } }, (error, result) => {
        res(result);
        rej(error);
      });
    }).catch(err => {
      console.log(err);
    });
  })
};

async getInputs() {
  let storage = await this.collection.findOne({ seed: this.seed });
  return new Promise((res, rej) => {
    let options = undefined;
    if (storage !== null && storage.inputs != null && storage.inputs.length > 0) {
      options = { start: storage.inputs[0].keyIndex, end: storage.inputs[storage.inputs.length - 1].keyIndex, treshold: 1 };
    }
    iota.getInputs(this.seed, options)
      .then(({ inputs, totalBalance }) => {
        let index = 0;
        for (let input of inputs) {
          if (index < input.keyIndex)
            index = input.keyIndex;
        }
        if (storage == null) {
          this.collection.insertOne({
            seed: this.seed, inputs: inputs, balance: totalBalance, highestKeyIndex: index
          }, (err, result) => {
            rej(err);
            res(result);
            return
            });

getInputs part 1
If a database entry already exists, the system checks whether input addresses from the database are still input addresses, i.e., whether they were returned by the getInputs function. In case these addresses have an entry of a bundle hash at " used " in the database, it will be copied. The new database entry is then transferred to the database.
 
        } else {
          if (storage.inputs != null) {
            for (let oldInput of storage.inputs) {
              for (let i = 0; i < inputs.length; i++) {
                if (inputs[i].keyIndex == oldInput.keyIndex)
                  inputs[i].used = oldInput.used;
              }
            }
          }
          if (storage.highestKeyIndex < index) {
            this.collection.updateOne({ seed: this.seed }, { '$set': { inputs: inputs, balance:totalBalance, highestKeyIndex: index } }, (err, result) => {
              rej(err);
              res(result);
            });
          } else {
            this.collection.updateOne({ seed: this.seed }, { '$set': { inputs: inputs, balance:totalBalance } }, (err, result) => {
              rej(err);
              res(result);
            });
          }
        }
        res(inputs);
      })
      .catch(err => {
        rej(err);
      })
  });
};


listen(receivingAddress = null) {
  return new Observable((observer) => {
    this.sock.connect(tcp);
    this.sock.subscribe('tx');
    this.sock.subscribe('sn');
    this.sock.on('message', msg => {
      const data = msg.toString().split(' ');
      if (receivingAddress == null) {
        observer.next(data);
      }
      else {
        var index = undefined;
        for (var i = 0; i < receivingAddress.length; i++) {
          if (data[2] == receivingAddress[i])
            index = i;
        }
        if (index != undefined)
          observer.next(data);
      }
    });
  });
}

async getMessageOfTransaction(hash) {
  return new Promise((res, rej) => {
    iota.getTrytes(hash)
      .then(trytes => {
        var ascii = converter.trytesToAscii(trytes[0].substring(0, 2186));
        ascii = ascii.toString().replace(/\0/g, '');
        res(ascii);
      })
      .catch(err => {
        rej(err);
      })
 
  });
};

async getNewReceivingAddress() {
  await this.checkIfPending();
  let storage = await this.collection.findOne({ seed: this.seed });
  if (storage == null || storage.inputs == null)
    await this.getInputs();
  storage.highestKeyIndex++;
  let address = await this.getNewAddress(storage.highestKeyIndex, 1);
  return new Promise((res, rej) => {
    if (storage.receiving == undefined)
      storage.receiving = [];
    storage.receiving.push({
      address: address[0],
      keyIndex: storage.highestKeyIndex,
      security: 2,
      balance: 0
    })
    this.collection.updateOne({ seed: this.seed }, { '$set': { highestKeyIndex: storage.highestKeyIndex, receiving: storage.receiving } }, (error, result) => {
      res(address);
      rej(error);
    });
  });

async getBalancesOfReceiving() {
  let storage = await this.collection.findOne({ seed: this.seed });
  let addresses = [];
  return new Promise((res, rej) => {
    for (let address of storage.receiving)
      addresses.push(address.address);
    iota.getBalances(addresses, 100)
      .then(({ balances }) => {
        for (let i = 0; i < balances.length; i++) {
          storage.receiving[i].balance = balances[i];
        }
        this.collection.updateOne({ seed: this.seed }, { '$set': { receiving: storage.receiving } }, (error, result) => {
          res(balances);
          rej(error);
        });
      })
      .catch(err => {
        rej(err);
      })
  });
}

async moveFromReceivingToInput(address) {
  await this.getBalancesOfReceiving();
  let storage = await this.collection.findOne({ seed: this.seed });
  return new Promise((res, rej) => {
    let index = undefined;
    for (let i = 0; i < storage.receiving.length; i++) {
      if (storage.receiving[i].address == address) {
        index = i;
        break;
      }
    }
    let balance = storage.receiving[index].balance;
    if (balance > 0)
      storage.inputs.push(storage.receiving[index]);
    storage.receiving.splice(index, index + 1);
    this.collection.updateOne({ seed: this.seed }, { '$set': { inputs: storage.inputs, receiving:storage.receiving } balance: storage.balance + balance}, (error, result) => {
      res(balance);
      rej(error);
    });
  });
}

```
