<script setup>
import { computed, onMounted, ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import SearchIcon from "../assets/icons/ph_magnifying-glass-bold_18.svg";
import AppInput from "./assets/AppInput.vue";
import AppBreedCard from "./assets/AppBreedCard.vue";
import AppPageLayout from "./assets/AppPageLayout.vue";
import AppFilters from "./assets/AppFilters.vue";
import {
  addFavorite,
  listBreeds,
  listFavorites,
  removeFavorite,
} from "../api/breeds";
import { useAuthStore } from "../stores/auth";
import AppModal from "./assets/AppModal.vue";

const route = useRoute();
const router = useRouter();

const allBreeds = ref([]);
const isLoading = ref(false);

const authStore = useAuthStore();
const showAuthModal = ref(false);

const favoriteIds = ref(new Set());

function parseArrayQuery(val) {
  if (!val) return [];
  return Array.isArray(val) ? val : [val];
}

const inputValue = ref("");
const isFiltersOpen = ref(false);

const activeFilters = ref({
  size: parseArrayQuery(route.query.size),
  activity: parseArrayQuery(route.query.activity),
  care: parseArrayQuery(route.query.care),
  housing: route.query.housing || null,
  kids: route.query.kids || null,
});

const sizeMap = { small: 1, medium: 2, large: 3 };
const activityMap = { low: 1, medium: 3, high: 5 };
const kidsMap = { no: 1, yes: 5 };

function mapFiltersToParams(filters) {
  const params = {};
  if (filters.size.length) params.size = sizeMap[filters.size[0]];
  if (filters.activity.length) params.energy = activityMap[filters.activity[0]];
  if (filters.housing) params.house_type = filters.housing;
  if (filters.kids) params.kids_friendly = kidsMap[filters.kids];
  return params;
}

const searchValue = ref("");

const breedsData = computed(() => {
  const query = searchValue.value.toLowerCase().trim();
  if (!query) return allBreeds.value;
  return allBreeds.value.filter((breed) =>
    breed.name.toLowerCase().includes(query),
  );
});

function applySearch() {
  searchValue.value = inputValue.value;
}

const hasActiveSearch = computed(() => {
  return (
    searchValue.value.trim() ||
    activeFilters.value.size.length ||
    activeFilters.value.activity.length ||
    activeFilters.value.care.length ||
    activeFilters.value.housing ||
    activeFilters.value.kids
  );
});

async function fetchBreeds() {
  isLoading.value = true;
  try {
    const params = mapFiltersToParams(activeFilters.value);
    const response = await listBreeds(params);
    allBreeds.value = Array.isArray(response)
      ? response
      : (response.results ?? []);
  } catch (error) {
    console.error("Помилка завантаження порід:", error);
    allBreeds.value = [];
  } finally {
    isLoading.value = false;
  }
}

onMounted(async () => {
  fetchBreeds();

  if (authStore.isAuthenticated) {
    const favorites = await listFavorites();
    favoriteIds.value = new Set(favorites.results.map((f) => f.breed.id));
  }
});

watch(
  () => route.query,
  (newQuery) => {
    activeFilters.value = {
      size: parseArrayQuery(newQuery.size),
      activity: parseArrayQuery(newQuery.activity),
      care: parseArrayQuery(newQuery.care),
      housing: newQuery.housing || null,
      kids: newQuery.kids || null,
    };
    fetchBreeds();
  },
  { deep: true },
);

function toggleFilters() {
  isFiltersOpen.value = true;
}

function closeFilters() {
  isFiltersOpen.value = false;
}

async function handleToggleLike(breedId) {
  if (!authStore.isAuthenticated) {
    showAuthModal.value = true;
    return;
  }

  try {
    if (favoriteIds.value.has(breedId)) {
      await removeFavorite(breedId);
      favoriteIds.value.delete(breedId);
    } else {
      await addFavorite(breedId);
      favoriteIds.value.add(breedId);
    }
    favoriteIds.value = new Set(favoriteIds.value);
  } catch (error) {
    console.error("Помилка:", error);
  }
}

function handleApplyFilters(newFilters) {
  activeFilters.value = newFilters;
  isFiltersOpen.value = false;

  const query = { ...route.query };

  if (newFilters.size.length) query.size = newFilters.size;
  else delete query.size;
  if (newFilters.activity.length) query.activity = newFilters.activity;
  else delete query.activity;
  if (newFilters.care.length) query.care = newFilters.care;
  else delete query.care;
  if (newFilters.housing) query.housing = newFilters.housing;
  else delete query.housing;
  if (newFilters.kids) query.kids = newFilters.kids;
  else delete query.kids;

  router.push({ query });
}

function goBack() {
  if (isFiltersOpen.value) {
    isFiltersOpen.value = false;
  } else {
    router.back();
  }
}
</script>

<template>
  <AppPageLayout v-if="isFiltersOpen" @back="goBack">
    <AppFilters
      :key="isFiltersOpen"
      :initial-filters="activeFilters"
      @apply="handleApplyFilters"
      @close="closeFilters"
    />
  </AppPageLayout>

  <template v-else>
    <div class="grid grid-cols-12 gap-8 mt-10 mb-7">
      <div class="col-start-1 col-span-4 flex flex-col gap-8">
        <h1 class="font-primary text-h1 text-gray-100">
          Тут ви знайдете улюбленця
        </h1>

        <div class="flex flex-col items-start gap-6">
          <AppInput
            v-model="inputValue"
            placeholder="Пошук"
            :icon="SearchIcon"
            @keydown.enter="applySearch"
            @blur="applySearch"
          />

          <button class="btn btn-md btn-secondary" @click="toggleFilters">
            Фільтри
          </button>
        </div>
      </div>
    </div>

    <div
      v-if="isLoading"
      class="col-span-12 flex justify-center py-20 text-gray-60 font-primary"
    >
      Завантаження...
    </div>

    <template v-else>
      <div
        v-if="hasActiveSearch"
        class="col-span-12 font-primary text-h3 text-gray-100 mb-10"
      >
        Знайдені породи за пошуковим запитом: ({{ breedsData.length }})
      </div>

      <div
        v-if="breedsData.length > 0"
        class="col-span-12 grid grid-cols-4 gap-8 pb-20"
      >
        <AppBreedCard
          v-for="breed in breedsData"
          :key="breed.id"
          :title="breed.name"
          :image="breed.image || breed.image_url"
          :liked="favoriteIds.has(breed.id)"
          @toggle-like="handleToggleLike(breed.id)"
          @view="router.push(`/breed/${breed.id}`)"
        />
      </div>

      <div
        v-else
        class="col-span-12 flex justify-center py-20 text-gray-60 font-primary"
      >
        За вашими критеріями нічого не знайдено 😔
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
    </template>
  </template>
</template>
