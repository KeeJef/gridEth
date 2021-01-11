<template>
  <div class="square" v-bind:style="{ backgroundColor: colourData }" v-on:click="clicked = !clicked"  v-bind:class="{active: clicked }"></div>
</template>

<script>
export default {
  name: 'square',
  props:{colour: String},
  data: function () {
     return {
       clicked: false,
       colourData: "#"+ this.colour
     }
     
  },
watch : {
  colour: {
    handler: function() {
        this.colourData = "#"+ this.colour;
    },
    immediate: true,
  },
},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.square{
    height: 10px;
    width: 10px;
    background-color: transparent;
    outline: 1px solid #CCC;
}
.active{
    width: 320px;
    height: 200px;
    background-color: black;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;

    /* Position the tooltip */
    position: absolute;
    z-index: 1;
}

</style>
