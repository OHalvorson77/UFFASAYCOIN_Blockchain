import React, { useState } from 'react';
import axios from 'axios';

function TransactionForm({ sender }) {
  const [receiver, setReceiver] = useState('');
  const [amount, setAmount] = useState(0);

  const submitTransaction = async () => {
    await axios.post('http://localhost:5000/transaction', {
      sender,
      receiver,
      amount
    });
    alert('Transaction submitted');
  };

  return (
    <div className="p-4 border rounded mt-4">
      <h2 className="text-lg font-bold">Send Transaction</h2>
      <input placeholder="Receiver" onChange={e => setReceiver(e.target.value)} className="border p-2 mr-2" />
      <input type="number" placeholder="Amount" onChange={e => setAmount(Number(e.target.value))} className="border p-2 mr-2" />
      <button onClick={submitTransaction} className="bg-green-500 text-white px-4 py-2">Send</button>
    </div>
  );
}

export default TransactionForm;
