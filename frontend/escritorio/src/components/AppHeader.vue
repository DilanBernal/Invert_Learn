<script setup></script>
<template>
  <header class="main-header">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/register-user">Crear Usuario</router-link>
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
}
</style>