import { createApp } from "vue";
import "./styles/main.css";
import App from "./App.vue";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [{ path: "/", component: () => import("./App.vue") }],
});

createApp(App).use(router).mount("#app");
