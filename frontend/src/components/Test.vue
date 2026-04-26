<script setup>
import CardDogImg from "../assets/card_dog.png";
import ArticleSection from "./ArticleSection.vue";
import AppArticleCards from "./assets/AppArticleCards.vue";
import AppBreedCard from "./assets/AppBreedCard.vue";
import AppBreedStats from "./assets/AppBreedStats.vue";
import AppFavoritesMiniCards from "./assets/AppFavoritesMiniCards.vue";
import Header from "./Header.vue";
import QuizHero from "./QuizHero.vue";

import mopsImg from "../assets/mops_card.png";
import shitsuImg from "../assets/shi-tsu_card.png";
import AppTabSwitcher from "./assets/AppTabSwitcher.vue";
import PawIcon from "../assets/icons/big-paw.svg";

import { ref } from "vue";
import AppHomeTag from "./assets/AppHomeTag.vue";
import AppQuizStepDivider from "./assets/AppQuizStepDivider.vue";
import { listBreeds } from "../api/breeds";
const activeTab = ref(0);

const breedsResponse = ref(null);
const breedsError = ref(null);

async function loadBreeds() {
  breedsError.value = null;
  try {
    breedsResponse.value = await listBreeds({ page_size: 1 });
  } catch (e) {
    breedsError.value = e?.message ?? String(e);
  }
}
</script>

<template>
  <!-- <section class="component">
    <button
      class="px-4 py-2 rounded bg-gray-100 text-black"
      @click="loadBreeds"
    >
      Test API: load breeds
    </button>
    <pre
      v-if="breedsResponse"
      class="mt-2 p-2 bg-gray-900 text-white rounded overflow-auto"
      >{{ breedsResponse }}</pre
    >
    <p v-if="breedsError" class="mt-2 text-red-600">
      API error: {{ breedsError }}
    </p>
  </section> -->

  <QuizHero class="component" :image="CardDogImg" />

  <ArticleSection
    class="component"
    title="Світ улюбленців"
    description="Статті про собак — від вибору до догляду та розуміння поведінки"
    description-style="w-[446px]"
  >
    <AppArticleCards />
  </ArticleSection>

  <ArticleSection
    class="component"
    title="Улюблені породи"
    description="Тут зібрані всі породи, які тобі сподобались"
  >
    <AppFavoritesMiniCards />
  </ArticleSection>

  <ArticleSection
    class="component"
    title="1. Як підготуватись до появи собаки?"
    description="Що потрібно купити, як облаштувати простір і підготувати дім до нового улюбленця. Розбираємо базові речі, які допоможуть зробити перехід для собаки комфортним і без стресу — від першого лежака до безпечного дому."
    contentGap="gap-6"
    titleStyle="text-h2 font-primary text-gray-100"
    description-style="text-secondary font-primary text-gray-80"
  />

  <AppBreedStats class="component" />

  <AppTabSwitcher v-model="activeTab" :tabs="['бульдог', 'мопс']" />

  <AppBreedCard
    title="Шит-цу"
    :image="shitsuImg"
    class="m-10"
    v-if="activeTab === 0"
  />
  <AppBreedCard
    title="Мопс"
    :image="mopsImg"
    size="big"
    class="component"
    v-if="activeTab === 1"
  />

  <AppHomeTag class="component" type="apartment" />
  <AppHomeTag class="component" />

  <AppQuizStepDivider :current="1" :total="7" class="component" />

  <component :is="PawIcon"></component>
</template>

<style>
.component {
  margin-top: 16px;
}
</style>
