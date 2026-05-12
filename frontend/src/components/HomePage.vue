<script setup>
import { useRouter } from "vue-router";
import ArticleSection from "./ArticleSection.vue";
import QuizHero from "./QuizHero.vue";
import AppArticleCards from "./assets/AppArticleCards.vue";
import AppFavoritesMiniCards from "./assets/AppFavoritesMiniCards.vue";
import { useAuthStore } from "../stores/auth";
import AppModal from "./assets/AppModal.vue";
import { ref } from "vue";

const router = useRouter();
const authStore = useAuthStore();
const showAuthModal = ref(false);

function open(adress) {
  router.push(`/${adress}`);
}

function openFavorites() {
  if (!authStore.isAuthenticated) {
    showAuthModal.value = true;
    return;
  }
  router.push("/favorites");
}
</script>

<template>
  <div class="grid grid-cols-12 gap-8 mt-10 mb-7">
    <h1 class="col-span-12 font-primary text-h1">Привіт!</h1>
    <QuizHero class="col-span-6 flex justify-center" @click="open('quiz')" />

    <div class="flex flex-col justify-center col-span-6 gap-9">
      <ArticleSection
        title="Світ улюбленців"
        description="Статті про собак — від вибору до догляду та розуміння поведінки"
        description-style="max-w-111.5 text-main font-primary text-gray-80"
        @click="open('pets-world')"
      >
        <AppArticleCards />
      </ArticleSection>

      <ArticleSection
        title="Улюблені породи"
        description="Тут зібрані всі породи, які тобі сподобались"
        @click="openFavorites"
      >
        <div class="relative">
          <AppFavoritesMiniCards />
        </div>
      </ArticleSection>
    </div>
  </div>

  <AppModal
    v-if="showAuthModal"
    title="Увійдіть або створіть акаунт"
    description="Щоб користуватися функцією обраного та зберігати свої вподобання"
    @close="showAuthModal = false"
  >
    <div class="flex gap-4">
      <button
        class="btn btn-primary btn-md flex-1"
        @click="router.push('/auth')"
      >
        Увійти
      </button>
      <button
        class="btn btn-secondary btn-md flex-1"
        @click="showAuthModal = false"
      >
        Скасувати
      </button>
    </div>
  </AppModal>
</template>
