<template>
  <div class="flex">
    <ArticleTeaser
      v-for="article in this.articles"
      :key="article.slug"
      :article="article"
    />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'IndexPage',
  async asyncData({ $content }) {
    const articles = await $content('articles')
      .where({ published: true })
      .sortBy('createdAt', 'desc')
      .fetch()

    return { articles }
  },
})
</script>
