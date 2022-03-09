<template>
  <article class="w-1/4 prose-sm prose bg-white shadow-lg prose-gray-400">
    <NuxtLink :to="`/articles/${article.slug}`">
      <img
        class="object-cover w-full h-32 mt-0 mb-1 prose-none"
        :src="article.image.src"
        :alt="article.image.alt"
      />
    </NuxtLink>

    <div class="px-4 pb-2">
      <TagList :tags="article.tags.slice(0, 3)" />

      <NuxtLink :to="`/articles/${article.slug}`" class="no-underline">
        <h3 class="my-1">{{ article.title }}</h3>
      </NuxtLink>

      <span class="text-xs uppercase">
        {{ formatDate(article.updatedAt) }}
      </span>
      <span class="text-xs italic lowercase">by</span>
      <span class="text-xs uppercase">{{ article.author }}</span>

      <p class="text-sm lead">{{ article.description }}</p>
    </div>
  </article>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: {
    article: Object,
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
