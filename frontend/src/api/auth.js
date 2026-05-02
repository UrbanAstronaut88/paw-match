import { http } from "./http";

http.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      Cookies.remove("token");
      Cookies.remove("user");
      window.location.href = "/auth";
    }
    return Promise.reject(error);
  },
);

export async function register(payload) {
  const { data } = await http.post("/auth/register/", payload);
  return data;
}

export async function login(payload) {
  const { data } = await http.post("/auth/login/", payload);
  return data;
}

export async function refreshToken(payload) {
  const { data } = await http.post("/auth/refresh/", payload);
  return data;
}

export async function me() {
  const { data } = await http.get("/auth/me/");
  return data;
}

export async function changePassword(payload) {
  const { data } = await http.post("/auth/change-password/", payload);
  return data;
}

export async function logout() {
  const { data } = await http.post("/auth/logout/");
  return data;
}
