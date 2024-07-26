import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Home';
import NotFound from './NotFound';

const Router: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route element={<NotFound/>} />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
