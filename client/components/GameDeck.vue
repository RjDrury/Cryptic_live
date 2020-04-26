
<template>
  <div>
    <div v-for="chunk in productChunks" v-bind:key="chunk" class="row">
      <div v-for="game in chunk" v-bind:key="game.name" class="col-sm-2">
        <GameCard v-bind:game="game" />
      </div>
    </div>
  </div>
</template>

<script>
import _ from "lodash";
import GameCard from "~/components/GameCard.vue";
export default {
  name: "GameDeck",
  components: {
    GameCard
  },
  props: {
    listOfGames: Array
  },
  data() {
    return {};
  },
  methods: {},
  computed: {
    productChunks() {
      return _.chunk(Object.values(this.listOfGames), 6);
    }
  }
};
</script>

<style>
.form-container {
  display: flex;
  flex-direction: column;
  background-color: lightblue;
}
.col {
  padding-bottom: 15px;
}
.row {
  padding-top: 15px;
}

.header {
  padding: 15px;
  text-align: center;
  font-weight: bold;
}
</style>
