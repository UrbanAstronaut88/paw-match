<script setup lang="ts">
import Header from "./Header.vue";
import Footer from "./Footer.vue";
import AppPawsBackground from "./assets/AppPawsBackground.vue";
import { onMounted } from "vue";
import { useAuthStore } from "../stores/auth";
</script>

<template>
  <div class="flex relative flex-col min-h-screen">
    <Header />
    <AppPawsBackground />
    <main class="relative z-10 flex-1 w-full max-w-[1296px] mx-auto">
      <RouterView />
    </main>
    <Footer />
  </div>
</template>
