<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList 
      :products="products" 
      @add-to-cart="addToCart"
      />
    <p>장바구니 총 가격 {{ totalPrice }}</p>
    <Cart 
      :cart-products="cartProducts"
      @delete-cart-item="deleteCartItem"
      />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from '@/components/Cart.vue';
let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const cartProducts = ref([])

const addToCart= function (id) {
  // 4. 버튼에 부착된 product.id로 어떤 객체인지 식별하고
  // 그 객체를 cartProducts 배열에 push
  for (const product of products.value) {
    if (id === product.id) {
      product.id += 10000
      cartProducts.value.push(product)
      totalPrice.value += product.price
    }
  }
}
const totalPrice = ref(0)

const deleteCartItem = function (cart) {
  const cartIndex = cartProducts.value.indexOf(cart)
  const product = cartProducts.value[cartIndex]
  totalPrice.value -= product.price
  cartProducts.value.splice(cartIndex, 1)
}




</script>
