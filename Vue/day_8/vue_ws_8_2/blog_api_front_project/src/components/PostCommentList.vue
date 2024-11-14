<template>
    <div>
      <ul>
        <li>
          {{ comment.content }}
        </li>
      </ul>
    </div>
</template>

<script setup>
defineProps({
  comment:Object
})
</script>

<style scoped>

</style>