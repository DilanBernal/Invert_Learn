<script setup>
import AppHeader from './components/AppHeader.vue';
</script>

<template>
  <app-header></app-header>
  <v-combobox label="Combobox" :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
    variant="outlined"></v-combobox>
  <router-view />
</template>

<style scoped></style>
