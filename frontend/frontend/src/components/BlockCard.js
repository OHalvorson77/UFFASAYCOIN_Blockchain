import React from 'react';

function BlockCard({ block }) {
    return (
      <div className="bg-gray-700 rounded-xl p-4 shadow-lg w-72 border border-teal-400">
        <h2 className="text-lg font-semibold mb-2">Block #{block.index}</h2>
        <p className="text-sm mb-1"><strong>Hash:</strong> {block.hash}</p>
        <p className="text-sm mb-1"><strong>Previous:</strong> {block.previousHash}</p>
        <p className="text-sm mb-1"><strong>Timestamp:</strong> {new Date(block.timestamp).toLocaleString()}</p>
        <p className="text-sm mb-2"><strong>Nonce:</strong> {block.nonce}</p>
  
        <div className="text-sm">
          <strong>Transactions:</strong>
          <ul className="list-disc ml-4 mt-1">
            {block.transactions.map((tx, idx) => (
              <li key={idx}>
                {tx.sender} ➡️ {tx.recipient}: {tx.amount}
              </li>
            ))}
          </ul>
        </div>
      </div>
    );
  }

  export default BlockCard;
  
