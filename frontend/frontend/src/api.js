import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export const fetchChain = () => axios.get(`${API_URL}/chain`);
export const addTransaction = (transaction) => axios.post(`${API_URL}/transaction`, transaction);
export const mineBlock = () => axios.post(`${API_URL}/mine`);
