<template>
  <div class="colourPicker" v-bind:style="{ backgroundColor: colourData }" v-on:click="clicked = !clicked"  v-bind:class="{active: clicked }"></div>
</template>

<script>

//https://baianat.github.io/verte/examples.html#default-example
export default {
  name: 'colourPicker',
  props:{colour: String, price: Number, link: String},
  data: function () {
     return {
       colourPicked: null,
       price: null, 
       link: null,
       addToCartValue: false 
     }
     
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.square{
    height: 350px;
    width: 200px;
    background-color: white;
    outline: 1px solid #CCC;
}

</style>
