<script setup>
const model = defineModel();

defineOptions({ inheritAttrs: false });

defineProps({
  icon: {
    type: Object,
    required: true,
  },
  value: {
    type: String,
    required: true,
  },
  variant: {
    type: String,
    default: "checkbox",
  },
});
</script>

<template>
  <div class="flex items-center gap-2 cursor-pointer">
    <input
      type="checkbox"
      :value="value"
      v-model="model"
      class="form-input-hidden"
      v-bind="$attrs"
    />
    <div :class="variant">
      <component :is="icon" class="w-4 h-4" />
    </div>
  </div>
</template>
