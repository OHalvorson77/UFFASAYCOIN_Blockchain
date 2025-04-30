# UFFASAYCOIN_Blockchain


A user-friendly, educational blockchain platform built with Flask and React. UFFASAYCOIN allows you to create a wallet, send and receive coins, mine blocks, and visualize your personal blockchain—all with a sleek black-and-neon-green 3D interface.

---

## 🚀 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 🧠 Overview

UFFASAYCOIN is a full-stack blockchain application designed for learning and experimentation. Unlike traditional cryptocurrencies, UFFASAYCOIN emphasizes transparency and user engagement by providing:

- **Personal Wallets**: Each user has a unique wallet with a public address and balance.
- **Transaction Management**: Easily send and receive coins between users.
- **Blockchain Visualization**: View the entire blockchain with detailed block information.
- **Mining**: Mine new blocks to validate transactions and earn coins.
- **Real-Time Updates**: Wallet balances and blockchain state update instantly.

---

## ✨ Features

- **User Authentication**: Register and log in with a username and password.
- **Wallet Management**: Create and manage your wallet with a unique address.
- **Transaction Handling**: Send and receive UFFASAYCOIN securely.
- **Blockchain Exploration**: Visualize the blockchain with detailed block and transaction information.
- **Mining Functionality**: Mine new blocks to add to the blockchain.
- **Responsive UI**: Sleek black and neon green 3D theme for an immersive experience. ([An awesome README template to jumpstart your projects! - GitHub](https://github.com/othneildrew/Best-README-Template?utm_source=chatgpt.com))

---

## ⚙️ Tech Stack

- **Backend**:
  - Python
  - Flask
  - Flask-CORS
  - JSON Web Tokens (JWT) ([README](https://en.wikipedia.org/wiki/README?utm_source=chatgpt.com), [How to create Professional Github Readme Profile (Step By Step)](https://www.youtube.com/watch?v=rCt9DatF63I&utm_source=chatgpt.com))

- **Frontend**:
  - React
  - React Router
  - Axios
  - Tailwind CSS ([Write Your README Before Your Code](https://www.wired.com/2010/08/write-your-readme-before-your-code?utm_source=chatgpt.com))

- **Blockchain**:
  - Custom Python-based blockchain implementation
  - SHA-256 hashing
  - Proof-of-Work consensus algorithm ([Blockchain-By-Example/README.md at master - GitHub](https://github.com/PacktPublishing/Blockchain-By-Example/blob/master/README.md?utm_source=chatgpt.com), [How to Write a Good README File for Your GitHub Project](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/?utm_source=chatgpt.com))

---

## 🛠️ Getting Started

### Prerequisites

- Node.js and npm
- Python 3.8+
- pip

### Installation

#### Backend

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/uffasaycoin.git
   cd uffasaycoin/backend
   ```


2. Create a virtual environment: ([Readme file template - EOSIO + Antelope Documentation](https://guide.eoscostarica.io/docs/tools/readme-file-template?utm_source=chatgpt.com))
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```


3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


4. Run the Flask server:
   ```bash
   python main.py
   ```


#### Frontend

1. Navigate to the frontend directory: ([How to write a good README - GitHub](https://github.com/banesullivan/README?utm_source=chatgpt.com))
 
   cd ../frontend
   


2. Install dependencies:
  
   npm install
  


3. Run the React development server:
 
   npm start
  


---

## 🖥️ Usage

1. Open your browser and navigate to `http://localhost:3000`.
2. Register a new account or log in with existing credentials.
3. View your wallet address and balance.
4. Send and receive UFFASAYCOIN transactions.
5. Mine new blocks and watch your balance update in real-time.
6. Explore the blockchain and view detailed information about each block and transaction.

---

## 📡 API Endpoints

### Authentication

- `POST /register`: Register a new user.
- `POST /login`: Log in an existing user.

### Blockchain Operations

- `POST /mine`: Mine a new block.
- `GET /chain`: Get the current blockchain.

### Transactions

- `POST /transaction`: Create a new transaction.

---


## 🤝 Contributing

We welcome contributions to enhance UFFASAYCOIN. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

Please ensure your code adheres to the existing style and includes appropriate tests.

---
