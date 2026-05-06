<script setup>
import { useRouter } from "vue-router";
import ArticleSection from "./ArticleSection.vue";
import QuizHero from "./QuizHero.vue";
import AppArticleCards from "./assets/AppArticleCards.vue";
import AppFavoritesMiniCards from "./assets/AppFavoritesMiniCards.vue";
import { useAuthStore } from "../stores/auth";

const router = useRouter();
const authStore = useAuthStore();

function open(adress) {
  router.push(`/${adress}`);
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
        description-style="max-w-111.5"
        @click="open('pets-world')"
      >
        <AppArticleCards />
      </ArticleSection>

      <ArticleSection
        title="Улюблені породи"
        description="Тут зібрані всі породи, які тобі сподобались"
        @click="open('favorites')"
      >
        <div class="relative">
          <AppFavoritesMiniCards
            :class="{
              'blur-sm pointer-events-none select-none':
                !authStore.isAuthenticated,
            }"
          />

          <div
            v-if="!authStore.isAuthenticated"
            class="absolute inset-0 flex items-center justify-center"
          >
            <button class="btn btn-secondary btn-md" @click.stop="open('auth')">
              Увійти
            </button>
          </div>
        </div>
      </ArticleSection>
    </div>
  </div>
</template>
