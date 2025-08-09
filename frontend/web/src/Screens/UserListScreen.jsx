import React, { useEffect, useState } from "react";
import axios from "axios";
import UserItem from "../Components/UserItem";

const UserListScreen = () => {
  const [usersList, setUsersList] = useState([]);

  const getUsers = async () => {
    try {
      const response = await axios.get("http://localhost:8000/usuario");
      const data = response.data;
      setUsersList(data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleDeleteUser = async (id) => {
    try {
      const response = await axios.delete(
        `http://localhost:8000/usuario/${id}`
      );
      if (response) {
        getUsers();
      }
    } catch (error) {
      console.error(error);
    }
  };
  useEffect(() => {
    getUsers();
  }, []);

  return (
    <>
      <div className="container">
        <h2 className="text-center">Lista de Usuarios</h2>
        {usersList.map((item) => {
          return (
            <UserItem
              key={item.usuario_id}
              handleDeleteUser={() => {
                handleDeleteUser(item.usuario_id);
              }}
              user={item}
            />
          );
        })}
      </div>
    </>
  );
};

export default UserListScreen;
