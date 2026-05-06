import axios from "axios";
import Cookies from "js-cookie";

const BACKEND_ORIGIN = import.meta.env.VITE_BACKEND_ORIGIN || "";
const API_PREFIX = import.meta.env.VITE_API_PREFIX || "/api/v1";

export const http = axios.create({
  baseURL: `${BACKEND_ORIGIN}${API_PREFIX}`,
});

http.interceptors.request.use((config) => {
  const token = Cookies.get("token");
  if (token) {
    config.headers = config.headers ?? {};
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
