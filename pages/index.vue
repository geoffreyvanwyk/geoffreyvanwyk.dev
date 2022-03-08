<template></template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'IndexPage',
  async asyncData({ $content }) {
    const posts = await $content('articles')
      .only(['title', 'description', 'img', 'tags', 'slug'])
      .sortBy('createdAt', 'desc')
      .fetch()

    return {
      posts,
    }
  },
})
</script>
