<script setup>
import {ref} from 'vue'
import TheWelcome from './components/TheWelcome.vue'
import store from './store'
const props = defineProps({
    token: String,
    user: String
})

if (props.token) {
  store.setToken(props.token)
}
const username = props.user ? props.user: ''

</script>

<template>
  <header>
    {{ store.count }} - {{  store.token  }} - {{ username }}
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" @click="store.increment" />

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
