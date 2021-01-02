<template>
  <div class="square" colour="grey" v-on:click="clicked = !clicked" v-bind:class="{ active: clicked }"></div>
</template>

<script>
export default {
  name: 'square',
  data: function () {
     return {
       clicked: false
     }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.square{
    height: 10px;
    width: 10px;
    outline: 1px solid #CCC;
}
.active{
    height: 10px;
    width: 10px;
    outline: 1px solid rgb(235, 56, 56);
}
</style>
