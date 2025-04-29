import React, { useEffect, useState } from 'react';
import { fetchChain, addTransaction, mineBlock } from './api';
import BlockCard from './components/BlockCard';
import TransactionForm from './components/TransactionForm';

function App() {
  const [chain, setChain] = useState([]);

  useEffect(() => {
    loadChain();
  }, []);

  const loadChain = async () => {
    try {
      const response = await fetchChain();
      setChain(response.data.chain);
    } catch (error) {
      console.error('Error fetching chain:', error);
    }
  };

  const handleAddTransaction = async (transaction) => {
    try {
      await addTransaction(transaction);
      alert('Transaction added!');
    } catch (error) {
      console.error('Error adding transaction:', error);
    }
  };

  const handleMineBlock = async () => {
    try {
      await mineBlock();
      alert('Block mined!');
      loadChain();
    } catch (error) {
      console.error('Error mining block:', error);
    }
  };

  return (
    <div>
      <h1>Blockchain Explorer</h1>
      <TransactionForm onAddTransaction={handleAddTransaction} />
      <button onClick={handleMineBlock}>Mine Block</button>
      <div>
        {chain.map((block, index) => (
          <BlockCard key={index} block={block} />
        ))}
      </div>
    </div>
  );
}

export default App;
