<script setup>
import { ref, computed, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import AppPageLayout from "./assets/AppPageLayout.vue";
import AppBreedStats from "./assets/AppBreedStats.vue";
import AppHomeTag from "./assets/AppHomeTag.vue";
import AppModal from "./assets/AppModal.vue";
import {
  getBreed,
  addFavorite,
  removeFavorite,
  listFavorites,
} from "../api/breeds";
import { useAuthStore } from "../stores/auth";

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();

const breed = ref(null);
const isLoading = ref(false);
const isFavorite = ref(false);
const showAuthModal = ref(false);
const loadError = ref("");
const favoriteError = ref("");

const stats = computed(() => {
  if (!breed.value) return [];
  const { traits } = breed.value;
  return [
    { value: traits.size.value },
    { value: traits.energy.value },
    { value: traits.grooming.value },
    { value: traits.kids_friendly.value },
  ];
});

onMounted(async () => {
  isLoading.value = true;
  try {
    breed.value = await getBreed(route.params.id);

    if (authStore.isAuthenticated) {
      const favorites = await listFavorites();
      isFavorite.value = favorites.results.some(
        (f) => f.breed.id === breed.value.id,
      );
    }
  } catch (error) {
    loadError.value = "Не вдалось завантажити породу. Спробуйте ще раз.";
  } finally {
    isLoading.value = false;
  }
});

function goBack() {
  router.back();
}

async function toggleFavorite() {
  if (!authStore.isAuthenticated) {
    showAuthModal.value = true;
    return;
  }

  try {
    if (isFavorite.value) {
      await removeFavorite(breed.value.id);
      isFavorite.value = false;
    } else {
      await addFavorite(breed.value.id);
      isFavorite.value = true;
    }
  } catch (error) {
    favoriteError.value = "Не вдалось оновити улюблене.";
    setTimeout(() => {
      favoriteError.value = "";
    }, 3000);
  }
}
</script>

<template>
  <AppPageLayout @back="goBack">
    <div
      v-if="isLoading"
      class="col-span-12 flex justify-center items-center py-20 font-primary text-gray-60"
    >
      Завантаження...
    </div>

    <div
      v-else-if="loadError"
      class="col-span-12 flex justify-center py-20 font-primary text-error"
    >
      {{ loadError }}
    </div>

    <template v-else-if="breed">
      <div class="col-span-6 row-start-2 h-full pb-8">
        <img
          :src="breed.image || breed.image_url"
          :alt="breed.name"
          class="h-full object-cover rounded-3xl"
        />
      </div>

      <div class="col-start-7 col-span-4 row-start-2 flex flex-col gap-6 mb-8">
        <h1 class="font-primary text-h1 text-gray-100">{{ breed.name }}</h1>

        <div class="flex flex-col gap-4">
          <h2 class="font-primary text-h3 text-gray-100">Опис породи</h2>
          <p class="font-primary text-main text-gray-80">
            {{ breed.description }}
          </p>
        </div>

        <div class="flex flex-col gap-8 mt-2">
          <h2 class="font-primary text-h2 text-gray-100">
            Характеристики породи
          </h2>
          <AppBreedStats :stats="stats" />
        </div>

        <AppHomeTag :type="breed.traits.housing_type.value" class="mt-2" />

        <span
          v-if="favoriteError"
          class="font-primary text-secondary text-error"
        >
          {{ favoriteError }}
        </span>

        <div class="flex items-center gap-4 mt-2.5">
          <template v-if="isFavorite">
            <button class="btn btn-md btn-secondary" @click="toggleFavorite">
              Видалити породу
            </button>
            <button
              class="btn btn-md btn-primary"
              @click="router.push('/explore')"
            >
              Більше порід
            </button>
          </template>

          <button
            v-else
            class="btn btn-big btn-primary"
            @click="toggleFavorite"
          >
            Додати в улюблене
          </button>
        </div>
      </div>
    </template>

    <div
      v-else
      class="col-span-12 flex justify-center py-20 font-primary text-gray-60"
    >
      Породу не знайдено
    </div>

    <AppModal
      v-if="showAuthModal"
      title="Потрібно увійти"
      description="Увійдіть в акаунт щоб додавати породи в улюблене"
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
  </AppPageLayout>
</template>
