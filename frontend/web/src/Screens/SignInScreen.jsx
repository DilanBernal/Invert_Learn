import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const SignInScreen = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [showPassword2, setShowPassword2] = useState(false);
  const [moneda, setMoneda] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (verifyPasswords()) {
      const usuario = {
        nombre: name,
        email: email,
        contrasena: password,
        moneda_preferida: moneda,
      };
      try {
        const response = await axios.post(
          "http://localhost:8000/usuario",
          usuario
        );
        console.log(response);
        resetForm();
        navigate("/");
      } catch (error) {
        if (error.response && error.response.status === 400) {
          alert("Error: " + error.response.data.detail);
          return;
        }
        console.error("Error al registrar el usuario:", error);
      }
    }
  };

  const resetForm = () => {
    setName("");
    setEmail("");
    setPassword("");
    setPassword2("");
    setMoneda("");
  };

  const verifyPasswords = () => {
    return password === password2 ? true : false;
  };

  return (
    <div className="container mt-5">
      <h2 className="text-center">Registrar Usuario</h2>
      <hr />
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
            required
          />
          <label htmlFor="email" className="form-label">
            Correo electrónico
          </label>
        </div>
        <div className="mb-3 form-floating">
          <input
            type={showPassword ? "text" : "password"}
            className="form-control"
            id="password"
            onInput={(e) => {
              setPassword(e.target.value);
            }}
            placeholder=""
            required
          />
          <label htmlFor="password" className="form-label">
            Contraseña
          </label>
          <button
            className="btn btn-outline-light btn-password position-absolute end-0"
            onClick={() => {
              setShowPassword(!showPassword);
            }}
          >
            {showPassword && <i className="bi bi-eye"></i>}
            {!showPassword && <i className="bi bi-eye-slash-fill"></i>}
          </button>
        </div>
        <div className="mb-3 form-floating">
          <input
            type={showPassword2 ? "text" : "password"}
            className="form-control"
            id="password2"
            onInput={(e) => {
              setPassword2(e.target.value);
            }}
            onBlur={verifyPasswords}
            placeholder=""
            required
          />
          <label htmlFor="password2" className="form-label">
            Confirmar Contraseña
          </label>
          <button
            className="btn btn-outline-light btn-password position-absolute end-0"
            onClick={() => {
              setShowPassword2(!showPassword2);
            }}
          >
            {showPassword2 && <i className="bi bi-eye"></i>}
            {!showPassword2 && <i className="bi bi-eye-slash-fill"></i>}
          </button>
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
            required
          />
          <label htmlFor="moneda" className="form-label">
            Tipo de moneda preferida
          </label>
        </div>
        <button type="submit" className="btn btn-primary">
          Registrar Usuario
        </button>
      </form>
    </div>
  );
};

export default SignInScreen;
