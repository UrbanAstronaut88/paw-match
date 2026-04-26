<script setup>
import { ref } from "vue";
import AppTabSwitcher from "./assets/AppTabSwitcher.vue";
import AppLoginForm from "./assets/AppLoginForm.vue";
import AppRegisterForm from "./assets/AppRegisterForm.vue";
import AppPawsBackground from "./assets/AppPawsBackground.vue";

const activeTab = ref(0);
</script>

<template>
  <div class="relative min-h-screen">
    <AppPawsBackground />

    <div class="min-h-screen max-w-[1296px] mx-auto grid grid-cols-12 gap-8">
      <div class="col-start-5 col-span-4 flex justify-center flex-col gap-8">
        <div class="flex flex-col gap-4">
          <h1 class="font-primary text-h1 text-gray-100">Petly</h1>
          <p class="font-primary text-main text-gray-80">
            Знайди свою ідеальну породу
          </p>
        </div>

        <div class="flex flex-col gap-12">
          <AppTabSwitcher v-model="activeTab" :tabs="['Вхід', 'Реєстрація']" />

          <AppLoginForm v-if="activeTab === 0" />
          <AppRegisterForm v-else />
        </div>
      </div>
    </div>
  </div>
</template>
