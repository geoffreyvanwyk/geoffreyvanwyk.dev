<template>
  <ul class="list-none pl-0 flex justify-start">
    <li v-for="tag in tags" :key="tag"><tag :name="tag" /></li>
  </ul>
</template>

<script lang="ts">
import Vue from 'vue'
import Tag from '~/components/Tag.vue'
export default Vue.extend({
  components: { Tag },
  props: {
    tags: Array,
  },
})
</script>
