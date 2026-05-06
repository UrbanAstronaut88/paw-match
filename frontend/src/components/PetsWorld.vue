<script setup>
import { useRouter } from "vue-router";
import AppPageLayout from "./assets/AppPageLayout.vue";
import AppSplitContent from "./assets/AppSplitContent.vue";
import articles from "../assets/data/pets_world_articles.json";
import AppArticleCards from "./assets/AppArticleCards.vue";
import ArticleSection from "./ArticleSection.vue";

const router = useRouter();

function goBack() {
  router.back();
}

function openArticle(slug) {
  router.push(`/article/${slug}`);
}
</script>

<template>
  <AppPageLayout @back="goBack">
    <AppSplitContent
      title="Світ улюбленців"
      description="Корисні статті про догляд, поведінку та здоров'я собак"
      text-col-class="col-span-3"
    >
      <div
        class="col-span-12 grid grid-cols-2 grid-flow-col grid-rows-3 gap-8 mb-9 -mt-2"
      >
        <ArticleSection
          v-for="article in articles"
          :key="article.id"
          :title="article.title"
          :description="article.description"
          title-style="text-h2 font-primary text-gray-100"
          description-style="text-secondary font-primary text-gray-80"
          @click="openArticle(article.slug)"
        />
      </div>
    </AppSplitContent>
  </AppPageLayout>
</template>
