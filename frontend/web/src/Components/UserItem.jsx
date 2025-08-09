import React, { useState } from "react";

const UserItem = ({ user }) => {
  const [hoverCanBtn, setHoverCanBtn] = useState(false);
  const [hoverEditBtn, setHoverEditBtn] = useState(false);

  return (
    <>
      <hr />
      <div className="row">
        <div className="col-11 align-items-center d-flex gap-4">
          <span>
            <strong>ID:</strong> {user.usuario_id}
          </span>
          <span>
            <strong>NOMBRES:</strong>
            {user.nombre}
          </span>
          <span>
            <strong>EMAIL:</strong>
            {user.email}
          </span>
          <span>
            <strong>MONEDA PREFERIDA:</strong>
            {user.moneda_preferida}
          </span>
        </div>
        <div className="col-1">
          <button
            className="btn btn-outline-danger"
            onMouseEnter={() => {
              setHoverCanBtn(true);
            }}
            onMouseLeave={() => {
              setHoverCanBtn(false);
            }}
            onFocus={() => {
              setHoverCanBtn(true);
            }}
            onPointerLeave={() => {
              setHoverCanBtn(false);
            }}
          >
            <i
              className={!hoverCanBtn ? "bi bi-trash3" : "bi bi-trash3-fill"}
            ></i>
          </button>
          <button
            className="btn btn-outline-primary"
            onMouseEnter={() => {
              setHoverEditBtn(true);
            }}
            onMouseLeave={() => {
              setHoverEditBtn(false);
            }}
            onFocus={() => {
              setHoverEditBtn(true);
            }}
            onPointerLeave={() => {
              setHoverEditBtn(false);
            }}
            onBlur={() => {
              setHoverEditBtn(false);
            }}
          >
            <i
              className={hoverEditBtn ? "bi bi-pencil-fill" : "bi bi-pencil"}
            ></i>
          </button>
        </div>
      </div>
      <hr />
    </>
  );
};

export default UserItem;
