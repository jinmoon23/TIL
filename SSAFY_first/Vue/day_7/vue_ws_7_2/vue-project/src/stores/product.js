import { ref, computed } from 'vue'
import { defineStore } from 'pinia'



export const useProductStore = defineStore('product', () => {
    const productList = ref([
        {id:crypto.randomUUID(),
        name:'상품1',
        imagePath:'src/assets/product1.png',
        price:10000,
        isFavorite:false
        },
        {id:crypto.randomUUID(),
        name:'상품2',
        imagePath:'src/assets/product2.png',
        price:20000,
        isFavorite:false
        },
        {id:crypto.randomUUID(),
        name:'상품3',
        imagePath:'src/assets/product3.png',
        price:30000,
        isFavorite:false
        },
        {id:crypto.randomUUID(),
        name:'상품4',
        imagePath:'src/assets/product4.png',
        price:40000,
        isFavorite:false
        },
    ])
    const cart = function (id) {
      const index = productList.value.findIndex((product) => {
        return id === product.id
      })
      productList.value[index].isFavorite = !productList.value[index].isFavorite
    }
  return {
    productList,
    cart
  }
})
