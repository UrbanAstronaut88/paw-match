<script setup>
import PawIcon from "../assets/logo.svg";
import HomeIcon from "../assets/icons/ph_house-simple-bold.svg";
import MagnifyingGlassIcon from "../assets/icons/ph_magnifying-glass-bold.svg";
import HeartIcon from "../assets/icons/ph_heart-bold-1.svg";
import { useRoute } from "vue-router";
import { computed } from "vue";

defineProps({
  user: {
    type: Object,
    default: null,
  },
});

const navItems = [
  {
    label: "Головна",
    href: "/",
    icon: HomeIcon,
  },
  {
    label: "Дослідити",
    href: "/explore",
    icon: MagnifyingGlassIcon,
  },
  {
    label: "Обране",
    href: "/favorites",
    icon: HeartIcon,
  },
];

const route = useRoute();
const currentPath = computed(() => route.path);
</script>

<template>
  <header class="app-header rounded-2xl min-h-20">
    <div class="flex items-center justify-between h-full">
      <a href="/" class="flex items-center gap-2 no-underline">
        <span class="font-primary text-h1 text-gray-100">Petly</span>
        <PawIcon class="text-primary" />
      </a>

      <div class="flex items-center gap-14">
        <nav class="flex items-center gap-8">
          <a
            v-for="item in navItems"
            :key="item.href"
            :href="item.href"
            class="app-header-nav-item"
            :class="{ 'text-primary': currentPath === item.href }"
          >
            <component
              :is="item.icon"
              class="flex items-center justify-center w-6 h-6"
            />
            <span class="font-primary text-small">{{ item.label }}</span>
          </a>
        </nav>

        <div class="overflow-hidden shrink-0 w-13 h-13 rounded-full bg-gray-20">
          <img
            v-if="user?.avatar"
            :src="user.avatar"
            :alt="user.name"
            class="w-full h-full object-cover"
          />
          <span v-else class="block w-full h-full bg-gray-20" />
        </div>
      </div>
    </div>
  </header>
</template>
