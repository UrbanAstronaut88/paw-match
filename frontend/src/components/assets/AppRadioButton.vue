<script setup>
defineOptions({ inheritAttrs: false });
</script>

<template>
  <label class="flex items-center gap-2">
    <input
      type="radio"
      name="group1"
      class="form-input-hidden"
      v-bind="$attrs"
    />
    <div class="radio"></div>
  </label>
</template>
