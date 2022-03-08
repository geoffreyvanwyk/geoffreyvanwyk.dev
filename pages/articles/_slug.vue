<template>
  <article
    class="mx-auto prose prose-lg bg-white shadow-lg prose-gray-400 prose-h1:mb-2 prose-code:text-xs"
  >
    <img class="w-full prose-none" :src="article.img" :alt="article.alt" />

    <div class="px-4 pb-2">
      <p class="text-sm uppercase">
        {{ formatDate(article.updatedAt) }}
        <span class="italic lowercase">by</span>
        {{ article.author }}
      </p>

      <h1>{{ article.title }}</h1>
      <tag-list :tags="article.tags" />
      <p class="lead">{{ article.description }}</p>

      <nuxt-content :document="article" />
    </div>
  </article>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  async asyncData({ $content, params }) {
    const article = await $content('articles', params.slug).fetch()

    return { article }
  },
  methods: {
    formatDate(date: string) {
      return new Date(date).toLocaleDateString('en-za', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      } as Intl.DateTimeFormatOptions)
    },
  },
})
</script>
