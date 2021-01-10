<template>
  <div v-if="dataReady" class="squareBox">
    <square
      v-for="(item, index) in 120" :key="index" v-bind:colour="squaresFromAPI[index].colour"
    />
  </div>
</template>

<script>
import square from "@/components/square.vue";
import squaresAPI from "../services/api.js";

export default {
  components: { square },
  name: "squareBox",

  data() {
    return {
      polling: null,
      dataReady: false,
      squaresFromAPI: []
      // other data
    };
  },

  methods: {
    pollData() {
      this.polling =  setInterval(async() => {
        this.squaresFromAPI = await squaresAPI.getSquares();
      }, 3000);
    },
  },
  beforeUnmount() {
    clearInterval(this.polling);
  },

  async mounted() {
    this.squaresFromAPI = await squaresAPI.getSquares();
    this.dataReady = true;
    this.pollData()
  },
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.squareBox {
  height: 1200px;
  width: 1200px;
  display: inline-flex;
  flex-wrap: wrap;
  border-style: solid;
  border-color: gray;
}
</style>
