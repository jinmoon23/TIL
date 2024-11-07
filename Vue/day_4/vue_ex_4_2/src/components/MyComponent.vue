<template>
  <div>
    <header>
      <h1 class="fixed-top d-flex justify-content-center">Gallery</h1>
    </header>

    <main>
      <div class="container mt-5 pt-5">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4">
          <div v-for="n in numberOfItems" :key="n" class="col">
            <div class="card">
              <img src="@/assets/sample.png" class="card-img-top" alt="...">
              <div class="card-body">
                <p class="card-text">하이룽룽룽 {{n}}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import {ref} from 'vue'
const numberOfItems = ref(4)
</script>

<style scoped>

</style>
