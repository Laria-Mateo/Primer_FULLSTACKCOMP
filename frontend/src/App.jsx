import React, { useState, useEffect } from 'react';
import UserBox from './components/UsersBox';
import CreateUser from './components/CreateUser';

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetchUsers();
  }, []); 

  function fetchUsers() {
    fetch('http://localhost:8000/api/users')
      .then(res => res.json())
      .then(res => setUsers(res))
      .catch(error => console.error('Error fetching users:', error));
  }

  function handleRefresh() {
    fetchUsers();
  }

  return (
    <>
      <h1>Cree su Usuario</h1>
      <CreateUser />
      <input type="submit" value="Refresh" onClick={handleRefresh} />
      {users.map(user => (
        <UserBox name={user.name} password={user.password} id={user.id} key={user.id} />
      ))}
    </>
  );
}

export default App;
