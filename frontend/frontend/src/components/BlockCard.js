import React from 'react';

function BlockCard({ block }) {
  return (
    <div style={{ border: '1px solid black', margin: '10px', padding: '10px' }}>
      <p><strong>Index:</strong> {block.index}</p>
      <p><strong>Timestamp:</strong> {block.timestamp}</p>
      <p><strong>Transactions:</strong> {JSON.stringify(block.transactions)}</p>
      <p><strong>Previous Hash:</strong> {block.previous_hash}</p>
      <p><strong>Nonce:</strong> {block.nonce}</p>
      <p><strong>Hash:</strong> {block.hash}</p>
    </div>
  );
}

export default BlockCard;
