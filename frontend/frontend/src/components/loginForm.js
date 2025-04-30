// components/LoginForm.js
import { useState } from 'react';
import axios from 'axios';

function LoginForm({ onLoggedIn }) {
  const [username, setUsername] = useState('');

  const login = async () => {
    try {
      const res = await axios.post('http://localhost:5000/login', { username });
      onLoggedIn(res.data);
    } catch (err) {
      alert('Login failed');
    }
  };

  return (
    <div className="auth-form">
      <input
        type="text"
        placeholder="Username"
        className="input neon"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <button onClick={login} className="neon-button">Login</button>
    </div>
  );
}

export default LoginForm;
