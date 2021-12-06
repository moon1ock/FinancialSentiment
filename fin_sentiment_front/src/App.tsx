import React from 'react';
import { Routes, Route } from "react-router-dom";
import Landing from './components/landing/landing'
import SearchPage from './components/searchpage/searchpage'

function App() {
  return (
    <div className="font-ProximaNova">
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/search" element={<SearchPage />} />
      </Routes>
    </div>
  );
}

export default App;
