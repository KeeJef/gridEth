<template>
  <div class="squareBox">
    <square v-bind:colour = TestFunction() v-for="index in 120" :key="index"/> 
    </div>
</template>

<script>
import square from '@/components/square.vue'
import squaresAPI from '../services/api.js'

export default {
  components: {square},
  name: 'squareBox',

  async mounted(){
    this.squaresFromAPI = await squaresAPI.getSquares()
    console.log(this.squaresFromAPI)
  },
  async TestFunction(){
    return squaresAPI.getSquares()
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.squareBox{
    height: 1200px;
    width: 1200px;
    display: inline-flex;
    flex-wrap: wrap;
    border-style: solid;
    border-color: gray;
}
</style>
