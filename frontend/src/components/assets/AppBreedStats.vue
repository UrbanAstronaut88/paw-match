<script setup>
defineProps({
  stats: {
    type: Array,
    default: () => [
      {
        emoji: "🐶",
        label: "Розмір",
        value: 2,
        color: "var(--color-size-bar)",
      },
      {
        emoji: "⚡",
        label: "Рівень активності",
        value: 3,
        color: "var(--color-activity-bar)",
      },
      {
        emoji: "🧴",
        label: "Складність догляду",
        value: 4,
        color: "var(--color-care-bar)",
      },
      {
        emoji: "👶",
        label: "Підходить для сімей з дітьми",
        value: 1,
        color: "var(--color-children-bar)",
      },
    ],
  },
});

const getWidth = (value) => `${value * 20}%`;
</script>

<template>
  <div class="flex flex-col gap-6 w-102.75 h-62">
    <div
      v-for="(stat, index) in stats"
      :key="index"
      class="flex flex-row gap-4"
    >
      <span
        class="flex items-center justify-center shrink-0 w-11 h-11 rounded-full bg-gray-10 text-h3"
        >{{ stat.emoji }}</span
      >
      <div class="flex flex-col w-full gap-3">
        <span class="font-primary text-main text-gray-100">{{
          stat.label
        }}</span>

        <div class="overflow-hidden h-0.75 rounded-btn bg-gray-20">
          <div
            class="h-full rounded-btn"
            :style="{
              width: getWidth(stat.value),
              backgroundColor: stat.color,
            }"
          />
        </div>
      </div>
    </div>
  </div>
</template>
