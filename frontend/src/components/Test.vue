<script setup>
import viteLogo from "../assets/vite.svg";
import heroImg from "../assets/hero.png";
import vueLogo from "../assets/vue.svg";
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

      <button
        class="btn btn-icon btn-primary"
        disabled=""
        style="margin-bottom: 12px"
      >
        <svg class="size-6 block">
          <use href="../../icons/icon arrow left.svg"></use>
        </svg>
      </button>

      <button class="btn btn-icon btn-primary" style="margin-bottom: 12px">
        <svg class="size-6 block">
          <use href="../../icons/icon arrow left.svg"></use>
        </svg>
      </button>

      <h2 style="font-size: 24px; margin-bottom: 12px">
        Secondary Icon Button
      </h2>
      <button class="btn btn-icon btn-icon-secondary" disabled="">
        <svg class="size-6 block">
          <use href="../../icons/icon arrow right.svg"></use>
        </svg>
      </button>

      <button class="btn btn-icon btn-icon-secondary">
        <svg class="size-6 block">
          <use href="../../icons/icon arrow right.svg"></use>
        </svg>
      </button>

      <h2 style="font-size: 24px; margin-bottom: 12px">Radio Button</h2>

      <label class="flex items-center gap-2" style="margin-bottom: 12px">
        <input
          type="radio"
          name="group1"
          class="form-input-hidden"
          checked="true"
          disabled=""
        />
        <div class="radio"></div>
      </label>

      <label class="flex items-center gap-2" style="margin-bottom: 12px">
        <input type="radio" name="group1" class="form-input-hidden" />
        <div class="radio"></div>
      </label>

      <h2 style="font-size: 24px; margin-bottom: 12px">Checkbox</h2>

      <label class="flex items-center gap-2 mb-3 cursor-pointer">
        <input
          type="checkbox"
          class="form-input-hidden"
          checked=""
          disabled=""
        />

        <div class="checkbox">
          <svg class="w-4 h-4">
            <use href="../../icons/ph_check-bold.svg"></use>
          </svg>
        </div>
      </label>

      <label class="flex items-center gap-2 mb-3 cursor-pointer">
        <input type="checkbox" class="form-input-hidden" checked="" />

        <div class="checkbox">
          <svg class="w-4 h-4">
            <use href="../../icons/ph_check-bold.svg"></use>
          </svg>
        </div>
      </label>

      <h2 style="font-size: 24px; margin-bottom: 12px">Checkbox round</h2>

      <label>
        <input type="checkbox" class="form-input-hidden" />
        <div class="checkbox-round">
          <svg class="w-4 h-4">
            <use href="../../icons/ph_check-bold.svg"></use>
          </svg>
        </div>
      </label>

      <label>
        <input
          type="checkbox"
          class="form-input-hidden"
          disabled=""
          checked=""
        />
        <div class="checkbox-round" style="margin-top: 12px">
          <svg class="w-4 h-4">
            <use href="../../icons/ph_check-bold.svg"></use>
          </svg>
        </div>
      </label>
    </div>
  </section>
</template>
