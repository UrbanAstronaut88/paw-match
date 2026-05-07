<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

defineProps({
  articles: {
    type: Array,
    default: () => [
      {
        title: "Перші дні вдома",
        description: "Як допомогти собаці адаптуватись і почуватися в безпеці.",
        slug: "pershi-dni-vdoma",
      },
      {
        title: "Чи вистачить часу?",
        description: "Дізнайся, чи підходить тобі такий ритм життя.",
        slug: "skilky-chasu-potrebuye-sobaka",
      },
    ],
  },
});
</script>

<template>
  <div class="grid grid-cols-2 items-start gap-6">
    <div
      v-for="(article, index) in articles"
      :key="index"
      class="flex flex-col gap-4 rounded-2xl p-6 bg-gray-20 shadow-card cursor-pointer"
      @click="router.push(`/article/${article.slug}`)"
    >
      <h3 class="text-h3 font-primary text-gray-100">{{ article.title }}</h3>
      <p class="text-secondary font-primary text-gray-80 m-0">
        {{ article.description }}
      </p>
    </div>
  </div>
</template>
