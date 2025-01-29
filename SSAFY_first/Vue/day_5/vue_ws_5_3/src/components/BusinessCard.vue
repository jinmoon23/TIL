<template>
    <div>
      <businessCardDetail 
        :business-cards="businessCards"
        @delete-card="deleteCard"
      />
    </div>
</template>

<script setup>
import { ref } from 'vue' 
import businessCardDetail from '@/components/businessCardDetail.vue'

const businessCards = ref([
    {id: crypto.randomUUID(),
      name: '일론 머스크',
      title: '테슬라 테크노킹'
    },
    {id: crypto.randomUUID(),
      name: '래리 앨리슨',
      title: '오라클 창업주'
    },
    {id: crypto.randomUUID(),
      name: '빌 게이츠',
      title: '마이크로소프트 공동창업주'
    },
    {id: crypto.randomUUID(),
      name: '래리 페이지',
      title: '구글 공동창업주'
    },
    {id: crypto.randomUUID(),
      name: '세르게이 브린',
      title: '구글 공동창업주'
    },
])
const deleteCard = function (id) {
  console.log(id)
  const findedCardIndex = businessCards.value.findIndex((card) => {
    return id === card.id
  })
  console.log(findedCardIndex)
  businessCards.value.splice(findedCardIndex,1)
}
</script>

<style scoped>

</style>