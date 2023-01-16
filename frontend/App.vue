<script setup>
import {ref} from 'vue'
import TheWelcome from './components/TheWelcome.vue'
const props = defineProps({
    token: String,
    user: String
})
const token = props.token ? props.token: null
const username = props.user ? props.user: ''

let count = ref(0)

function increment (event) {
  console.log(event)
  count.value++
}
</script>

<template>
  <header>
    {{ count }} - {{  token  }} - {{ username }}
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" @click="increment" />

    <div class="wrapper">

    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
