<script setup>
import viteLogo from "../assets/vite.svg";
import heroImg from "../assets/hero.png";
import vueLogo from "../assets/vue.svg";

import IconArrowLeft from "../assets/icons/icon_arrow-left.svg";
import IconArrowRight from "../assets/icons/icon_arrow-right.svg";
import CheckIcon from "../assets/icons/ph_check-bold.svg";
import IconButton from "./assets/AppIconButton.vue";
import RadioButton from "./assets/AppRadioButton.vue";
import CheckBox from "./assets/AppCheckbox.vue";
</script>

<template>
  <section id="center">
    <div>
      <h1 style="font-size: 50px; margin-bottom: 12px">Buttons</h1>

      <h2 style="font-size: 24px; margin-bottom: 12px">Big</h2>

      <button
        class="btn btn-big btn-primary"
        disabled="true"
        style="margin-bottom: 12px"
      >
        Продовжити
      </button>
      <button class="btn btn-big btn-primary" style="margin-left: 12px">
        Продовжити
      </button>

      <h2 style="font-size: 24px; margin-bottom: 12px">Medium</h2>

      <button
        class="btn btn-md btn-primary"
        disabled="true"
        style="margin-bottom: 12px"
      >
        Продовжити
      </button>

      <button class="btn btn-md btn-primary" style="margin-left: 12px">
        Продовжити
      </button>

      <h2 style="font-size: 24px; margin-bottom: 12px">Small</h2>

      <button
        class="btn btn-sm btn-primary"
        disabled="true"
        style="margin-bottom: 12px"
      >
        Продовжити
      </button>

      <button class="btn btn-sm btn-primary" style="margin-left: 12px">
        Продовжити
      </button>

      <h2 style="font-size: 24px; margin-bottom: 12px">Secondary</h2>

      <button
        class="btn btn-md btn-secondary"
        disabled="true"
        style="margin-bottom: 12px"
      >
        Продовжити
      </button>

      <button class="btn btn-md btn-secondary" style="margin-bottom: 12px">
        Продовжити
      </button>

      <h2 style="font-size: 24px; margin-bottom: 12px">Tertiary</h2>

      <button
        class="btn btn-tertiary"
        disabled="true"
        style="margin-bottom: 12px"
      >
        Надіслати ще раз
      </button>

      <button class="btn btn-tertiary" style="margin-left: 12px">
        Надіслати ще раз
      </button>

      <h2 style="font-size: 24px; margin-bottom: 12px">Icon Button</h2>

      <IconButton class="btn-primary" :icon="IconArrowLeft" disabled="" />

      <IconButton class="btn-primary" :icon="IconArrowLeft" />

      <h2 style="font-size: 24px; margin-bottom: 12px">
        Secondary Icon Button
      </h2>

      <IconButton class="btn-primary" :icon="IconArrowRight" disabled="" />

      <IconButton class="btn-primary" :icon="IconArrowRight" />

      <h2 style="font-size: 24px; margin-bottom: 12px">Radio Button</h2>

      <RadioButton checked="" disabled="" />
      <RadioButton />

      <h2 style="font-size: 24px; margin-bottom: 12px">Checkbox</h2>

      <CheckBox :icon="CheckIcon" disabled="" checked="" />

      <CheckBox :icon="CheckIcon" />

      <h2 style="font-size: 24px; margin-bottom: 12px">Checkbox round</h2>

      <CheckBox
        variant="checkbox-round"
        :icon="CheckIcon"
        disabled=""
        checked=""
      />

      <CheckBox variant="checkbox-round" :icon="CheckIcon" />
    </div>
  </section>
</template>
