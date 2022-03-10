<template>
  <span
    class="px-3 py-1 my-1 ml-1 text-xs font-medium text-gray-800 bg-gray-100 border border-gray-100 rounded-full"
    >{{ name }}</span
  >
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: {
    name: String,
  },
})
</script>
