<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue";
import AppOtpInput from "../AppOtpInput.vue";

const emit = defineEmits(["next"]);

const props = defineProps({
  error: { type: String, default: "" },
});

const otp = ref("");

const TIMER_DURATION = 60;
const timer = ref(0);
let interval = null;

function startTimer() {
  timer.value = TIMER_DURATION;
  clearInterval(interval);
  interval = setInterval(() => {
    if (timer.value > 0) {
      timer.value--;
    } else {
      clearInterval(interval);
    }
  }, 1000);
}

const timerLabel = computed(() => {
  const minutes = Math.floor(timer.value / 60)
    .toString()
    .padStart(2, "0");
  const seconds = (timer.value % 60).toString().padStart(2, "0");
  return `(${minutes}:${seconds})`;
});

onMounted(() => startTimer());
onUnmounted(() => clearInterval(interval));
</script>

<template>
  <div
    class="flex flex-col items-start gap-6"
    @keydown.enter.prevent="otp.length >= 4 && emit('next', otp)"
  >
    <AppOtpInput label="Код був надісланий на вашу адресу" v-model="otp" />

    <span class="font-primary text-secondary text-gray-80" v-if="!error">
      Код не прийшов?
      <span v-if="timer > 0">{{ timerLabel }}</span>
    </span>

    <span v-else class="font-primary text-secondary text-error">{{
      error
    }}</span>

    <button class="btn btn-tertiary" :disabled="timer > 0" @click="startTimer">
      Надіслати ще раз
    </button>

    <button
      class="btn btn-primary btn-md"
      :disabled="otp.length < 4"
      @click="emit('next', otp)"
    >
      Продовжити
    </button>
  </div>
</template>
