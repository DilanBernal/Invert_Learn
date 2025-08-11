import { createRouter, createWebHistory } from "vue-router";
import Register from "../screens/Register.vue";
import Home from "../screens/Home.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/register-user",
    name: "register-user",
    component: Register,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
