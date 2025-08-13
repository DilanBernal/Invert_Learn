<template>
  <div class="container">
    <h2 class="text-center">Lista de Usuarios</h2>
    <div v-for="user in usersList" :key="user.usuario_id">
      <UserItem :user="user" @delete-user="handleDeleteUser(user.usuario_id)" @edit-user="handleEditUser(user.usuario_id)" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import UserItem from '../components/UserItem.vue';

export default {
  components: {
    UserItem
  },
  data() {
    return {
      usersList: []
    };
  },
  mounted() {
    this.getUsers();
  },
  methods: {
    async getUsers() {
      try {
        const response = await axios.get("http://localhost:8000/usuario");
        this.usersList = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async handleDeleteUser(id) {
      try {
        const response = await axios.delete(`http://localhost:8000/usuario/${id}`);
        if (response.status === 200) {
          this.getUsers();
        }
      } catch (error) {
        console.error(error);
      }
    },
    handleEditUser(id) {
      this.$router.push(`/edit-user/${id}`);
    }
  }
};
</script>

<style scoped>
/* Add any component-specific styles here if needed */
</style>