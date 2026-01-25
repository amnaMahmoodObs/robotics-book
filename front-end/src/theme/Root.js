import React from 'react';
import Chatbot from './common/Chatbot'; // relative to Root.js in theme/

export default function Root({ children }) {
  return (
    <>
      {children}
      <Chatbot />
    </>
  );
}
