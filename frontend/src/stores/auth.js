import { defineStore } from "pinia";
import { ref, computed } from "vue";
import Cookies from "js-cookie";
import { login, register, logout, me } from "../api/auth";

export const useAuthStore = defineStore("auth", () => {
  const token = ref(Cookies.get("token") || null);
  const rawUser = Cookies.get("user");
  const user = ref(
    rawUser && rawUser !== "undefined" ? JSON.parse(rawUser) : null,
  );

  const isAuthenticated = computed(() => !!token.value);

  function setAuth(newToken, newUser) {
    token.value = newToken;
    user.value = newUser;
    Cookies.set("token", newToken, { expires: 7 });
    Cookies.set("user", JSON.stringify(newUser), { expires: 7 });
  }

  function clearAuth() {
    token.value = null;
    user.value = null;
    Cookies.remove("token");
    Cookies.remove("user");
  }

  async function handleLogin(payload) {
    const data = await login(payload);
    setAuth(data.access, data.user);
    return data;
  }

  async function handleRegister(payload) {
    await register(payload);
    const data = await login({
      email: payload.email,
      password: payload.password,
    });
    token.value = data.access;
    Cookies.set("token", data.access, { expires: 7 });
    Cookies.set("refresh", data.refresh, { expires: 30 });
    const userData = await me();
    user.value = userData;
    Cookies.set("user", JSON.stringify(userData), { expires: 7 });
    return data;
  }

  async function handleLogout() {
    await logout();
    clearAuth();
  }

  async function fetchMe() {
    const data = await me();
    user.value = data;
    Cookies.set("user", JSON.stringify(data), { expires: 7 });
    return data;
  }

  return {
    token,
    user,
    isAuthenticated,
    handleLogin,
    handleRegister,
    handleLogout,
    fetchMe,
  };
});
