import React, { useEffect, useState } from 'react';
import httpClient from "./httpClient";

// Define the User type
interface User {
  id: number;
  email: string;
}

const Home: React.FC = () => {
  const [user, setUser] = useState<User | null>(null);

  const logoutUser = async (): Promise<void> => {
    await httpClient.post<void>("//localhost:5000/logout");
    setUser(null); // Clear user state after logout
    window.location.href = "/";
  };

  useEffect(() => {
    (async () => {
      try {
        const resp = await httpClient.get<User>("//localhost:5000/@me");
        setUser(resp.data);
      } catch (error) {
        console.log("Not authenticated");
      }
    })();
  }, []);

  return (
    <div>
      <h1>Welcome to this React Application</h1>
      {/* Will check if user is logged in or not */}
      {user != null ? (
        <div>
          <h2>Logged in</h2>
          <h3>ID: {user.id}</h3>
          <h3>Email: {user.email}</h3>

          <button onClick={logoutUser}>Logout</button>
        </div>
      ) : (
        <div>
          <p>You are not logged in</p>
          <div>
            <a href="/login">
              <button>Login</button>
            </a>
            <a href="/register">
              <button>Register</button>
            </a>
          </div>
        </div>
      )}
    </div>
  );
};

export default Home;
