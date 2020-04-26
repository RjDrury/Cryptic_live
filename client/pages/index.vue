<template>
  <div>
    <h1 class="page-title">Categories</h1>
    <div class="sidebar-wrapper">
      <Sidebar v-bind:suggestedStreams="stream_list" />
    </div>
    <div class="container">
      <hr class="title-line-break" />
      <GameDeck v-bind:listOfGames="game_list" />
    </div>
  </div>
</template>

<script>
import GameDeck from "~/components/GameDeck.vue";
import Sidebar from "~/components/Sidebar.vue";
export default {
  components: {
    GameDeck,
    Sidebar
  },
  layout: "",
  data() {
    return {
      game_list: [],
      stream_list: []
    };
  },
  async asyncData({ $axios }) {
    const games = await $axios.get("http://localhost:5000/games");
    const streams = await $axios.get("http://localhost:5000/topstreamers");

    return {
      game_list: games.data.game_list,
      stream_list: streams.data.stream_list
    };
  }
};
</script>

<style>
.container {
  margin: 0px;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
h1 {
  color: white;
}
body {
  background: #1f2b3b;
}
.sidebar-wrapper {
  position: absolute;
  margin-left: 84%;
}
</style>
