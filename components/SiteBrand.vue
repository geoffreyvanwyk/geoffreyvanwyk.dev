<template>
  <figure class="flex">
    <NuxtLink to="/">
      <img
        src="~/assets/geoffreyvanwyk.jpg"
        alt="Profile photo of Geoffrey van Wyk"
        class="w-16 h-16 rounded-full ring-4 ring-gray-200"
      />
    </NuxtLink>
    <figcaption
      class="flex flex-col items-start justify-center pl-4 font-semibold"
    >
      <NuxtLink to="/">
        <div class="text-gray-100">Geoffrey van Wyk</div>
      </NuxtLink>
      <div class="text-gray-400">Computer Programmer</div>
    </figcaption>
  </figure>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({})
</script>
