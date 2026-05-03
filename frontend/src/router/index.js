import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "../stores/auth";
import AppLayout from "../components/AppLayout.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/auth",
      component: () => import("../components/AuthContainer.vue"),
    },
    {
      path: "/",
      component: AppLayout,
      children: [
        { path: "", component: () => import("../components/HomePage.vue") },
        {
          path: "explore",
          component: () => import("../components/SearchPage.vue"),
        },
        {
          path: "pets-world",
          component: () => import("../components/PetsWorld.vue"),
        },
        {
          path: "article/:slug",
          component: () => import("../components/assets/AppArticlePage.vue"),
        },
        {
          path: "quiz",
          component: () => import("../components/assets/AppQuiz.vue"),
        },
        {
          path: "breed/:id",
          component: () => import("../components/BreedPage.vue"),
        },
        {
          path: "favorites",
          component: () => import("../components/Favorites.vue"),
        },
        {
          path: "compare",
          component: () => import("../components/ComparePage.vue"),
        },
        {
          path: "profile",
          component: () => import("../components/ProfilePage.vue"),
        },
      ],
    },
  ],
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next("/auth");
  } else if (to.path === "/auth" && authStore.isAuthenticated) {
    next("/");
  } else {
    next();
  }
});

export default router;
