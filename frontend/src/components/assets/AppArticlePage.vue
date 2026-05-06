<script setup>
import { computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import AppPageLayout from "./AppPageLayout.vue";
import ArrowLeftIcon from "../../assets/icons/icon_arrow-left.svg";
import articles from "../../assets/data/articles.json";
import AppSplitContent from "./AppSplitContent.vue";
import AppArticleCTA from "./AppArticleCTA.vue";

const route = useRoute();
const router = useRouter();

const article = computed(() =>
  articles.find((a) => a.slug === route.params.slug),
);

function goBack() {
  router.back();
}

function open(adress) {
  router.push(`/${adress}`);
}
</script>

<template>
  <AppPageLayout @back="goBack">
    <div
      v-if="!article"
      class="col-span-12 pt-20 text-center font-primary text-h2 text-gray-60"
    >
      Статтю не знайдено
    </div>

    <AppSplitContent
      v-else
      :title="article.title"
      :description="article.description"
      text-col-class="col-span-5"
    >
      <div class="col-start-0 col-span-7 row-start-3 flex flex-col gap-8">
        <div
          v-for="(section, index) in article.sections"
          :key="index"
          class="flex flex-col gap-3"
        >
          <h2 class="font-primary text-h2 text-gray-100">
            {{ `${index + 1}. ${section.title}` }}
          </h2>
          <p class="font-primary text-main text-gray-80">
            {{ section.content }}
          </p>
        </div>
        <div class="flex flex-col gap-8">
          <h2 class="font-primary text-main text-gray-100 whitespace-pre-line">
            {{ article.finalTitle }}
          </h2>
        </div>
      </div>

      <AppArticleCTA
        class="col-span-5 row-start-4 pb-14"
        @start="open('quiz')"
      />
    </AppSplitContent>
  </AppPageLayout>
</template>
