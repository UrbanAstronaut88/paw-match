<script setup>
import HeartIcon from "../../assets/icons/ph_heart-fill.svg";
import { ref, onMounted } from "vue";
import { listFavorites, removeFavorite } from "../../api/breeds";
import { useAuthStore } from "../../stores/auth";
import chihuahua from "../../assets/dogs/Chihua-hua.png";
import mops from "../../assets/dogs/Mops.png";
import shitsu from "../../assets/dogs/Shi-tsu.png";

const authStore = useAuthStore();
const favorites = ref([]);

const defaultFavorites = [
  { id: null, title: "Чихуахуа", img: chihuahua },
  { id: null, title: "Мопс", img: mops },
  { id: null, title: "Ші-тцу", img: shitsu },
];

onMounted(async () => {
  if (!authStore.isAuthenticated) {
    favorites.value = defaultFavorites;
    return;
  }

  try {
    const response = await listFavorites();
    const results = response.results.slice(0, 3).map((f) => ({
      id: f.breed.id,
      title: f.breed.name,
      img: f.breed.image || f.breed.image_url,
    }));
    favorites.value = results;
  } catch (error) {
    console.error("Помилка завантаження улюблених:", error);
    favorites.value = defaultFavorites;
  }
});

async function removeLike(breedId, index) {
  if (!breedId) return;
  try {
    await removeFavorite(breedId);
    favorites.value.splice(index, 1);
  } catch (error) {
    console.error("Помилка видалення:", error);
  }
}
</script>

<template>
  <div class="grid grid-cols-3 gap-6 min-h-[160px]">
    <template v-if="favorites.length">
      <div
        v-for="(favorite, index) in favorites"
        :key="index"
        class="flex flex-col gap-4"
      >
        <img
          :src="favorite.img"
          :alt="favorite.title"
          class="rounded-xl w-full object-cover"
        />
        <div class="flex flex-row justify-between items-center px-1">
          <h3 class="text-gray-100 text-h3 font-primary m-0">
            {{ favorite.title }}
          </h3>
          <component
            :is="HeartIcon"
            class="cursor-pointer"
            :class="favorite.id ? 'text-primary' : 'text-gray-30'"
            @click="removeLike(favorite.id, index)"
          />
        </div>
      </div>
    </template>

    <div v-else class="col-span-3 flex items-center justify-center">
      <span class="font-primary text-secondary text-gray-60">
        Улюблених порід поки немає
      </span>
    </div>
  </div>
</template>
