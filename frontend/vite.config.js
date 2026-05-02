import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwindcss from "@tailwindcss/vite";
import svgLoader from "vite-svg-loader";

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  const backendOrigin = env.VITE_BACKEND_ORIGIN || "http://localhost:8000";

  return {
    plugins: [vue(), tailwindcss(), svgLoader()],
    server: {
      proxy: {
        "/api": {
          target: backendOrigin,
          changeOrigin: true,
        },
        "/media": {
          target: backendOrigin,
          changeOrigin: true,
        },
      },
    },
  };
});
