<template>
    <div>
      <ul>
        <li v-for="card in businessCards">
          <p>이름: {{ card.name }}</p>
          <p>직함: {{ card.title }}
            <button @click="deleteCard(card.id)">명함 삭제</button>
          </p>
        </li>
      </ul>
    </div>
</template>

<script setup>

defineProps({
    businessCards: Array 
})

const emit = defineEmits(['deleteCard'])

const deleteCard = function (id) {
  emit('deleteCard',id)
}
</script>

<style scoped>

</style>