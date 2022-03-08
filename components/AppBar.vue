<template>
  <nav class="bg-gray-700 mb-2 p-4">
    <branding-figure></branding-figure>
  </nav>
</template>

<script lang="ts">
import Vue from 'vue'
import BrandingFigure from '~/components/BrandingFigure.vue'
export default Vue.extend({
  components: { BrandingFigure },
})
</script>
