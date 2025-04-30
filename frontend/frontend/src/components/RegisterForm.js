import React, { useState } from 'react';
import axios from 'axios';

function RegisterForm({ onRegistered }) {
  const [username, setUsername] = useState('');

  const handleRegister = async () => {
    try {
      const res = await axios.post('http://localhost:5000/register', { username });
      onRegistered(res.data);
    } catch (err) {
      alert('Registration failed');
    }
  };

  return (
    <div className="p-4 border rounded">
      <h2 className="text-lg font-bold">Register</h2>
      <input className="border p-2 mr-2" value={username} onChange={(e) => setUsername(e.target.value)} />
      <button onClick={handleRegister} className="bg-blue-500 text-white px-4 py-2">Register</button>
    </div>
  );
}

export default RegisterForm;
