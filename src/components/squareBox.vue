<template>
  <div class="squareBox">
    <square v-for="index in 120" :key="index"/>  
</div>
</template>

<script>
import square from '@/components/square.vue'


export default {
  components: { square},
  name: 'squareBox'
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
