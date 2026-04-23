<script setup>
import Footer from "./components/Footer.vue";
import Header from "./components/Header.vue";
import Test from "./components/Test.vue";
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <Header />

    <main class="flex-1 max-w-[1296px] w-full mx-auto">
      <Test />
    </main>

    <Footer />
  </div>
</template>
