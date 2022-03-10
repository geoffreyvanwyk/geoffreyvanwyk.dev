<template>
  <div class="flex flex-wrap justify-start pl-0 list-none">
    <Tag v-for="tag in tags" :key="tag" :name="tag" />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: {
    tags: Array,
  },
})
</script>
