<script setup>
import AuthContainer from "./components/AuthContainer.vue";
import AppLayout from "./components/AppLayout.vue";
import HomePage from "./components/HomePage.vue";
import AppQuizButton from "./components/assets/AppQuizButton.vue";

import { ref } from "vue";
import AppQuiz from "./components/assets/AppQuiz.vue";
import AppSplitContent from "./components/assets/AppSplitContent.vue";
import PetsWorld from "./components/PetsWorld.vue";
import { RouterView } from "vue-router";
const housing = ref(null);
</script>

<template>
  <!-- <AuthContainer /> -->

  <AppLayout>
    <!-- <HomePage /> -->
    <!-- <AppQuiz /> -->
    <RouterView />
    <!-- <PetsWorld /> -->
  </AppLayout>
</template>
