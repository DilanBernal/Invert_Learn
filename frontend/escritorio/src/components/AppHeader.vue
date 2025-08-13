<script setup></script>
<template>
  <header class="main-header">
    <nav class="navbar">
      <router-link to="/">Home</router-link> 
      <router-link to="/register-user">Crear Usuario</router-link> 
      <router-link to="/users-list">Lista de  Usuarios</router-link> 
    </nav>
  </header>
</template>

<style scoped>
.main-header {
  position: sticky;
  width: 100vw;
  padding: 20px;
  border-bottom: 2px solid whitesmoke;
  background-color: #212529;
  top: 0;
  z-index: 20;
}
nav a{
  color: whitesmoke;
  text-decoration: none;
  margin: 0 20px ;
  position:relative;
}
nav a:not(:last-child)::before{
  content: "";
  width: 2px;
  height: 100%;
  background-color: whitesmoke;
  RIGHT: -100%;
  bottom: 0;
  position: absolute;
}
nav a:not(:first-child)::after{
  content: "";
  width: 2px;
  height: 100%;
  background-color: whitesmoke;
  left: -100%;
  bottom: 0;
  position: absolute;
}
</style>