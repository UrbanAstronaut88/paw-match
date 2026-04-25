<script setup>
import HeartIcon from "../../assets/icons/ph_heart-fill.svg";
import EmptyHeartIcon from "../../assets/icons/ph_heart-bold.svg";
import { ref } from "vue";

const props = defineProps({
  favorites: {
    type: Array,
    default: () => [
      {
        title: "Чихуахуа",
        img: "../../assets/dogs/Chihua-hua.png",
      },
      {
        title: "Мопс",
        img: "../../assets/dogs/Mops.png",
      },
      {
        title: "Ши-тцу",
        img: "../../assets/dogs/Shi-tsu.png",
      },
    ],
  },
});

const likedIndexes = ref(new Set(props.favorites.map((_, i) => i)));

function toggleLike(index) {
  if (likedIndexes.value.has(index)) {
    likedIndexes.value.delete(index);
  } else {
    likedIndexes.value.add(index);
  }
  likedIndexes.value = new Set(likedIndexes.value);
}

const getImageUrl = (url) => {
  return new URL(`${url}`, import.meta.url).href;
};
</script>

<template>
  <div class="grid grid-cols-3 gap-6">
    <div
      v-for="(favorite, index) in favorites"
      :key="index"
      class="flex flex-col gap-4"
    >
      <div class="flex flex-col gap-4">
        <img
          :src="getImageUrl(favorite.img)"
          :alt="favorite.title"
          class="rounded-xl w-full object-cover"
        />

        <div class="flex flex-row justify-between items-center px-1">
          <h3 class="text-gray-100 text-h3 font-primary m-0">
            {{ favorite.title }}
          </h3>

          <component
            :is="likedIndexes.has(index) ? HeartIcon : EmptyHeartIcon"
            class="text-primary cursor-pointer"
            @click="toggleLike(index)"
          />
        </div>
      </div>
    </div>
  </div>
</template>
