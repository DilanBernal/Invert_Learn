import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import axios from "axios";

const EditUserScreen = () => {
  const id = useParams()["id"];
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [moneda, setMoneda] = useState("");
  const navigator = useNavigate();
  useEffect(() => {
    const getUserById = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/usuario/${id}`);
        const data = response.data;
        console.log(response);
        setName(data.nombre);
        setEmail(data.email);
        setMoneda(data.moneda_preferida);
      } catch (error) {
        console.error(error);
      }
    };
    getUserById(id);
  }, [id, navigator]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const user = {
        nombre: name,
        email: email,
        moneda_preferida: moneda,
      };
      const response = await axios.put(
        `http://localhost:8000/usuario/${id}`,
        user
      );
      if (response) {
        navigator("/user-list");
        console.log(response);
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
      <div className="container">
        <form className="mx-4" onSubmit={handleSubmit}>
          <div className="mb-3 form-floating">
            <input
              type="text"
              className="form-control"
              onInput={(e) => {
                setName(e.target.value);
              }}
              id="name"
              placeholder=""
              value={name}
              required
            />
            <label htmlFor="name">Nombres y Apellidos</label>
          </div>
          <div className="mb-3 form-floating">
            <input
              type="email"
              className="form-control"
              onInput={(e) => {
                setEmail(e.target.value);
              }}
              placeholder="user@example.com"
              id="email"
              value={email}
              required
            />
            <label htmlFor="email" className="form-label">
              Correo electrónico
            </label>
          </div>
          <div className="mb-3 form-floating">
            <input
              type="text"
              className="form-control"
              onInput={(e) => {
                setMoneda(e.target.value.toUpperCase());
              }}
              id="moneda"
              placeholder="COP, USD, EUR"
              minLength={1}
              maxLength={3}
              value={moneda}
              required
            />
            <label htmlFor="moneda" className="form-label">
              Tipo de moneda preferida
            </label>
          </div>
          <button type="submit" className="btn btn-primary">
            Editar
          </button>
        </form>
      </div>
    </>
  );
};

export default EditUserScreen;
