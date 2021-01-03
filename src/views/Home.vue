<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <squareBox/>
    <ul>
      <li v-for="colours in squareArrayValues" :key="colours.number" v-text="colours.colour"></li>
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import SquareBox from '../components/squareBox.vue'


export default {
  name: 'Home',
  components: {
    HelloWorld,
    SquareBox
  }
}
</script>
