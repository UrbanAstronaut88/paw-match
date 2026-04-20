<script setup>
import EyeIcon from "../../assets/icons/ph_eye-bold.svg";
import EyeOffIcon from "../../assets/icons/ph_eye-closed-bold.svg";

import { ref } from "vue";

defineOptions({ inheritAttrs: false });

defineProps({
  label: {
    type: String,
    default: "",
  },
});

const showPassword = ref(false);
</script>

<template>
  <div class="flex flex-col gap-2">
    <span class="input-label" v-if="label">{{ label }}</span>

    <div class="input-wrapper" v-bind="$attrs">
      <input
        :type="showPassword ? 'text' : 'password'"
        placeholder="password"
        class="input"
        v-bind="$attrs"
      />
      <button type="button" @click="showPassword = !showPassword">
        <EyeOffIcon v-if="showPassword" />
        <EyeIcon v-else />
      </button>
    </div>
  </div>
</template>
