<!-- <script setup>
defineOptions({ inheritAttrs: false });

defineProps({
  icon: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" class="form-input-hidden" v-bind="$attrs" />

    <div class="checkbox">
      <component :is="icon" class="w-4 h-4" />
    </div>
  </label>
</template> -->

<script setup>
defineOptions({ inheritAttrs: false });

defineProps({
  icon: {
    type: Object,
    required: true,
  },
  variant: {
    type: String,
    default: "checkbox",
  },
});
</script>

<template>
  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" class="form-input-hidden" v-bind="$attrs" />
    <div :class="variant">
      <component :is="icon" class="w-4 h-4" />
    </div>
  </label>
</template>
