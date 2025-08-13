import { createRouter, createWebHistory } from "vue-router";
import Register from "../screens/Register.vue";
import Home from "../screens/Home.vue";
import UserList from "../screens/UserList.vue";

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
  {
    path: "/users-list",
    name: "users-list",
    component: UserList
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
