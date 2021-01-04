<template>
  <div v-if="dataReady" class="squareBox">
    <square v-for="index in 120" :key="index" v-bind:colour=squaresFromAPI[1].colour /> 
    </div>
</template>

<script>
import square from '@/components/square.vue'
import squaresAPI from '../services/api.js'

export default {
  components: {square},
  name: 'squareBox',

  data () {
    return {
        dataReady: false,
        // other data
    }
},

  async mounted(){
    this.squaresFromAPI = await squaresAPI.getSquares()
    this.dataReady = true
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
