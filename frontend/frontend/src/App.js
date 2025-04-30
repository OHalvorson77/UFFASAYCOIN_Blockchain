import React, { useState, useEffect } from 'react';
import axios from 'axios';
import RegisterForm from './components/RegisterForm';
import LoginForm from './components/loginForm';
import TransactionForm from './components/TransactionForm';
import './App.css'; 

function App() {
  const [user, setUser] = useState(null);
  const [chain, setChain] = useState([]);
  const [view, setView] = useState('login'); 

  const loadChain = async () => {
    const res = await axios.get('http://localhost:5000/chain');
    setChain(res.data.chain);
  };

  const refreshUser = async () => {
    if (!user) return;
    const res = await axios.post('http://localhost:5000/login', {
      username: user.username,
    });
    setUser(res.data);
  };

  const mineBlock = async () => {
    await axios.post('http://localhost:5000/mine', {
      miner_address: user.wallet.address,
    });
    await loadChain();
    await refreshUser();
  };

  useEffect(() => {
    loadChain();
  }, []);

  return (
    <div className="app-container">
      <h1 className="neon-title">UffasayCoin Platform</h1>

      {!user && (
        <div className="auth-section">
          {view === 'login' ? (
            <>
              <LoginForm onLoggedIn={setUser} />
              <p className="auth-toggle">
                No account? <span onClick={() => setView('register')}>Register here</span>
              </p>
            </>
          ) : (
            <>
              <RegisterForm onRegistered={setUser} />
              <p className="auth-toggle">
                Already have an account? <span onClick={() => setView('login')}>Login here</span>
              </p>
            </>
          )}
        </div>
      )}

      {user && (
        <div className="wallet-section">
          <div className="wallet-info">
            <p className="label">Username:</p>
            <p className="value">{user.username}</p>
            <p className="label">Wallet Address:</p>
            <p className="value">{user.wallet.address}</p>
            <p className="label">Balance:</p>
            <p className="value">{user.wallet.balance} UffasayCoin</p>
          </div>

          <TransactionForm sender={user.wallet.address} onTransactionSent={refreshUser} />

          <button onClick={mineBlock} className="neon-button mine-button">⛏️ Mine Transactions</button>
        </div>
      )}

      <div className="chain-section">
        <h2 className="neon-subtitle">Blockchain</h2>
        {chain.map((block, i) => (
          <div key={i} className="block-card">
            <h3>Block #{block.index}</h3>
            <p><strong>Hash:</strong> {block.hash}</p>
            <p><strong>Previous:</strong> {block.previous_hash}</p>
            <p><strong>Transactions:</strong> {block.transactions.length}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
