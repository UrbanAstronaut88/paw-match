<script setup>
import PawIcon from "../../assets/icons/big-paw.svg";

function random(min, max) {
  return Math.random() * (max - min) + min;
}

const zones = [
  { topMin: 0, topMax: 10, leftMin: 0, leftMax: 10 },
  { topMin: 0, topMax: 10, leftMin: 70, leftMax: 95 },
  { topMin: 50, topMax: 70, leftMin: 0, leftMax: 30 },
  { topMin: 60, topMax: 90, leftMin: 70, leftMax: 95 },
  { topMin: 10, topMax: 40, leftMin: 40, leftMax: 60 },
];

const paws = zones.map((zone, i) => ({
  id: i,
  top: `${random(zone.topMin, zone.topMax)}%`,
  left: `${random(zone.leftMin, zone.leftMax)}%`,
  duration: random(5, 9),
  rotate: random(0, 90),
}));
</script>

<template>
  <div class="absolute inset-0 pointer-events-none overflow-hidden -z-10">
    <PawIcon
      v-for="paw in paws"
      :key="paw.id"
      class="absolute text-primary"
      :style="{
        top: paw.top,
        left: paw.left,
        opacity: 0.05,
        '--rotate': `${paw.rotate}deg`,
        animation: `paw-float ${paw.duration}s ease-in-out infinite`,
      }"
    />
  </div>
</template>
