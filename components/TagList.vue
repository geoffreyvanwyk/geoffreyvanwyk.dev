<template>
  <ul class="flex flex-wrap flex-grow justify-start pl-0 list-none">
    <li v-for="tag in tags" :key="tag"><Tag :name="tag" /></li>
  </ul>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: {
    tags: Array,
  },
})
</script>
