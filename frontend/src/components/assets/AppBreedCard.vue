<script setup>
import HeartIcon from "../../assets/icons/ph_heart-bold-1.svg";
import HeartFillIcon from "../../assets/icons/ph_heart-fill-1.svg";
import { ref } from "vue";

const props = defineProps({
  title: { type: String, required: true },
  image: { type: String, required: true },
  size: { type: String, default: "sm" },
  liked: { type: Boolean, default: false },
});

const isLiked = ref(props.liked);

function toggleLike() {
  isLiked.value = !isLiked.value;
}
</script>

<template>
  <div
    class="flex flex-col overflow-hidden bg-gray-20 rounded-[20px] w-fit"
    :class="size === 'big' ? 'gap-2' : 'gap-0'"
  >
    <div :class="size === 'big' ? 'p-6' : 'p-4'">
      <div
        class="w-full overflow-hidden shrink-0"
        :class="size === 'big' ? 'h-125' : 'h-67'"
      >
        <img :src="image" :alt="title" class="w-full h-full object-cover" />
      </div>

      <div
        class="flex flex-col"
        :class="size === 'big' ? 'pt-4 gap-8' : 'pt-3 gap-6'"
      >
        <div class="flex items-center justify-between">
          <span
            class="font-primary text-gray-100"
            :class="size === 'big' ? 'text-h2' : 'text-h3'"
          >
            {{ title }}
          </span>
          <button
            class="cursor-pointer outline-none bg-transparent border-none p-0 flex items-center justify-center"
            @click="toggleLike"
          >
            <component
              :is="isLiked ? HeartFillIcon : HeartIcon"
              class="size-6 block"
              :class="isLiked ? 'text-primary' : 'text-gray-100'"
            />
          </button>
        </div>

        <button
          class="btn btn-primary self-start"
          :class="size === 'big' ? 'btn-md' : 'btn-sm'"
        >
          Переглянути
        </button>
      </div>
    </div>
  </div>
</template>
