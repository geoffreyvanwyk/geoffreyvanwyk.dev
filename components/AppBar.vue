<template>
  <nav class="p-4 mb-2 bg-gray-700">
    <BrandingFigure />
  </nav>
</template>

<script lang="ts">
import Vue from 'vue'
import BrandingFigure from '~/components/BrandingFigure.vue'
export default Vue.extend({
  components: { BrandingFigure },
})
</script>
