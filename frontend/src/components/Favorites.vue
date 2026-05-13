<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import AppBreedCard from "./assets/AppBreedCard.vue";
import CheckIcon from "../assets/icons/ph_check-bold.svg";
import { listFavorites, removeFavorite, compareBreeds } from "../api/breeds";
import { useAuthStore } from "../stores/auth";
import AppCheckBox from "./assets/AppCheckBox.vue";

const router = useRouter();
const authStore = useAuthStore();

const favorites = ref([]);
const isLoading = ref(false);
const isCompareMode = ref(false);
const selectedIds = ref([]);
const fetchError = ref("");
const removeError = ref("");

const canCompare = computed(() => selectedIds.value.length === 2);

onMounted(async () => {
  if (!authStore.isAuthenticated) {
    router.push("/auth");
    return;
  }

  isLoading.value = true;
  try {
    const response = await listFavorites();
    favorites.value = response.results.map((f) => ({
      id: f.breed.id,
      name: f.breed.name,
      image: f.breed.image || f.breed.image_url,
    }));
  } catch (error) {
    fetchError.value =
      "Не вдалось завантажити улюблені породи. Спробуйте ще раз.";
    favorites.value = mockFavorites;
  } finally {
    isLoading.value = false;
  }
});

async function handleRemove(breedId) {
  try {
    await removeFavorite(breedId);
    favorites.value = favorites.value.filter((f) => f.id !== breedId);
    selectedIds.value = selectedIds.value.filter((id) => id !== breedId);
  } catch (error) {
    removeError.value = "Не вдалось видалити породу.";
    setTimeout(() => {
      removeError.value = "";
    }, 3000);
  }
}

function clearAll() {
  favorites.value.forEach((f) => removeFavorite(f.id));
  favorites.value = [];
  selectedIds.value = [];
}

function toggleCompareMode() {
  isCompareMode.value = !isCompareMode.value;
  selectedIds.value = [];
}

function toggleSelect(breedId) {
  if (selectedIds.value.includes(breedId)) {
    selectedIds.value = selectedIds.value.filter((id) => id !== breedId);
  } else if (selectedIds.value.length < 2) {
    selectedIds.value = [...selectedIds.value, breedId];
  }
}

async function handleCompare() {
  if (!canCompare.value) return;
  router.push({
    path: "/compare",
    query: {
      first: selectedIds.value[0],
      second: selectedIds.value[1],
    },
  });
}

const selectedIdsStrings = computed({
  get: () => selectedIds.value.map(String),
  set: (val) => {
    if (val.length <= 2) {
      selectedIds.value = val.map(Number);
    }
  },
});
</script>

<template>
  <div
    class="grid grid-cols-12 gap-x-8 gap-y-10 items-start content-start pt-10"
  >
    <div
      v-if="isCompareMode"
      class="col-span-2 row-start-1 flex items-center gap-4 self-start"
    >
      <button
        class="btn btn-icon btn-icon-secondary"
        @click="toggleCompareMode"
      >
        <svg viewBox="0 0 24 24" fill="none" class="size-6">
          <path
            d="M15 18l-6-6 6-6"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </button>
      <span class="font-primary text-btn text-gray-80">Назад</span>
    </div>

    <div
      class="col-span-12 flex flex-col gap-10 pb-20"
      :class="isCompareMode ? 'row-start-2' : ' row-start-1'"
    >
      <div class="flex flex-col gap-8">
        <h1 class="font-primary text-h1 max-w-[411px] text-gray-100">
          {{ isCompareMode ? "Порівняння порід" : "Тут ваші улюблені породи" }}
        </h1>

        <p
          v-if="isCompareMode"
          class="font-primary text-secondary text-gray-100 -mt-4 max-w-[411px]"
        >
          Виберіть породи, щоб порівняти їх характеристики та зрозуміти, яка
          підходить саме вам
        </p>

        <div class="flex items-center gap-4">
          <button
            v-if="!isCompareMode"
            class="btn btn-md btn-secondary"
            :disabled="favorites.length === 0"
            @click="clearAll"
          >
            Очистити
          </button>

          <button
            class="btn btn-md btn-primary"
            :disabled="(isCompareMode && !canCompare) || favorites.length === 0"
            @click="isCompareMode ? handleCompare() : toggleCompareMode()"
          >
            Порівняти
          </button>
        </div>
      </div>

      <div
        v-if="isLoading"
        class="flex justify-center py-20 font-primary text-gray-60"
      >
        Завантаження...
      </div>

      <div
        v-else-if="fetchError"
        class="flex justify-center py-20 font-primary text-error"
      >
        {{ fetchError }}
      </div>

      <template v-else>
        <span v-if="removeError" class="font-primary text-secondary text-error">
          {{ removeError }}
        </span>
        <div v-else-if="favorites.length > 0" class="grid grid-cols-4 gap-8">
          <div v-for="breed in favorites" :key="breed.id" class="relative">
            <label v-if="isCompareMode" class="absolute top-4 right-4 z-10">
              <AppCheckBox
                :icon="CheckIcon"
                :value="String(breed.id)"
                variant="checkbox-round"
                v-model="selectedIdsStrings"
                :disabled="
                  selectedIds.length >= 2 && !selectedIds.includes(breed.id)
                "
              />
            </label>

            <div :class="isCompareMode ? 'pointer-events-none' : ''">
              <AppBreedCard
                :title="breed.name"
                :image="breed.image"
                :liked="true"
                @toggle-like="handleRemove(breed.id)"
                @view="router.push(`/breed/${breed.id}`)"
              />
            </div>
          </div>
        </div>

        <div v-else class="flex flex-col items-center gap-6 py-20">
          <h3 class="text-h3 font-primary text-gray-100">
            Ще немає улюблених порід...
          </h3>

          <button
            class="btn btn-md btn-primary"
            @click="router.push('/explore')"
          >
            Показати породи
          </button>
        </div>
      </template>
    </div>
  </div>
</template>
