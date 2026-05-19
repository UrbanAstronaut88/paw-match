<script setup>
import { ref, computed, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import AppPageLayout from "./assets/AppPageLayout.vue";
import AppBreedCard from "./assets/AppBreedCard.vue";
import AppBreedStats from "./assets/AppBreedStats.vue";
import AppHomeTag from "./assets/AppHomeTag.vue";
import { compareBreeds, addFavorite, removeFavorite, listFavorites } from "../api/breeds";
import AppSplitContent from "./assets/AppSplitContent.vue";
import { useAuthStore } from "../stores/auth";

const router = useRouter();
const route = useRoute();
const authStore = useAuthStore();

const isLoading = ref(false);
const compareError = ref("");
const firstBreed = ref(null);
const secondBreed = ref(null);
const conclusion = ref("");
const firstLiked = ref(false);
const secondLiked = ref(false);

function getStats(traits) {
  return [
    { value: traits.size.value },
    { value: traits.energy.value },
    { value: traits.grooming.value },
    { value: traits.kids_friendly.value },
  ];
}

const firstStats = computed(() =>
  firstBreed.value ? getStats(firstBreed.value.traits) : [],
);
const secondStats = computed(() =>
  secondBreed.value ? getStats(secondBreed.value.traits) : [],
);

onMounted(async () => {
  const firstId = route.query.first;
  const secondId = route.query.second;

  if (!firstId || !secondId) {
    router.back();
    return;
  }

  isLoading.value = true;
  try {
    const result = await compareBreeds(firstId, secondId);
    firstBreed.value = result.first_breed;
    secondBreed.value = result.second_breed;
    conclusion.value = result.conclusion;

    if (authStore.isAuthenticated) {
      const favorites = await listFavorites();
      const ids = new Set(favorites.results.map((f) => f.breed.id));
      firstLiked.value = ids.has(result.first_breed.id);
      secondLiked.value = ids.has(result.second_breed.id);
    }
  } catch {
    compareError.value = "Не вдалось порівняти породи. Спробуйте ще раз.";
  } finally {
    isLoading.value = false;
  }
});

async function toggleFavorite(which) {
  const breed = which === "first" ? firstBreed.value : secondBreed.value;
  const isLiked = which === "first" ? firstLiked.value : secondLiked.value;

  try {
    if (isLiked) {
      await removeFavorite(breed.id);
    } else {
      await addFavorite(breed.id);
    }
    if (which === "first") firstLiked.value = !firstLiked.value;
    else secondLiked.value = !secondLiked.value;
  } catch {
    // тихо ігноруємо
  }
}
</script>

<template>
  <AppPageLayout @back="router.back()">
    <AppSplitContent
      v-if="isLoading"
      title="Порівнюємо обрані породи…"
      description="Збираємо дані про породи та показуємо їх відмінності у зручному вигляді"
    >
      <img
        src="../assets/compare_dog.png"
        alt="Собака"
        class="w-full col-span-12 object-cover rounded-2xl mb-8 -mt-2"
      />
    </AppSplitContent>

    <div
      v-else-if="compareError"
      class="col-span-12 flex justify-center py-20 font-primary text-error"
    >
      {{ compareError }}
    </div>

    <template v-else-if="firstBreed && secondBreed">
      <div class="col-span-12 row-start-2 flex flex-col gap-2">
        <h1 class="font-primary text-h1 text-gray-100">Результати порівняння</h1>
        <p class="font-primary text-secondary text-gray-100">Порівняли — тепер обирайте</p>
      </div>

      <div class="col-span-6 row-start-3">
        <AppBreedCard
          :title="firstBreed.name"
          :image="firstBreed.image_src"
          :liked="firstLiked"
          size="big"
          @toggle-like="toggleFavorite('first')"
          @view="router.push(`/breed/${firstBreed.id}`)"
        />
      </div>

      <div class="col-span-6 row-start-3">
        <AppBreedCard
          :title="secondBreed.name"
          :image="secondBreed.image_src"
          :liked="secondLiked"
          size="big"
          @toggle-like="toggleFavorite('second')"
          @view="router.push(`/breed/${secondBreed.id}`)"
        />
      </div>

      <div class="col-span-6 row-start-4 flex flex-col gap-4">
        <AppBreedStats :stats="firstStats" />
        <div class="flex gap-4">
          <AppHomeTag v-for="h in firstBreed.housing" :key="h" :type="h" />
        </div>
      </div>

      <div class="col-span-6 row-start-4 flex flex-col gap-4">
        <AppBreedStats :stats="secondStats" />
        <div class="flex gap-4">
          <AppHomeTag v-for="h in secondBreed.housing" :key="h" :type="h" />
        </div>
      </div>

      <div
        v-if="conclusion"
        class="col-span-4 col-start-1 row-start-5 flex flex-col gap-6 pb-20"
      >
        <h2 class="font-primary text-h3 text-gray-100">Висновок</h2>
        <p class="font-primary text-secondary text-gray-100">{{ conclusion }}</p>
        <button
          class="btn btn-primary btn-big w-[300px] mt-4"
          @click="router.push('/favorites')"
        >
          Порівняти інші породи
        </button>
      </div>
    </template>
  </AppPageLayout>
</template>