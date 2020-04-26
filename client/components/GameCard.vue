
<template>
  <div>
    <a :href="'/game/'+game.twitch_id+'/'+game.mixer_id">
      <b-card class="game-card">
        <b-card-img :src="game.box_img" class="game-image" />
        <b-card-title>
          <a :href="'/game/'+game.twitch_id+'/'+game.mixer_id">{{game.name}}</a>
        </b-card-title>
        <b-card-text>
          <a :href="'/game/'+game.twitch_id+'/'+game.mixer_id">{{game.viewers}} viewers</a>
        </b-card-text>
      </b-card>
    </a>
  </div>
</template>

<script>
export default {
  name: "GameCard",

  props: {
    game: Object
  },
  data() {
    return {};
  },
  methods: {},
  computed: {}
};
</script>

<style>
.game-card {
  width: 10rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-align: left;
  border: hidden;
}
.game-image {
  width: 100%;
  height: 15vw;
  object-fit: cover;
}
.card-body {
  padding: 5px !important;
  font-size: 0.9rem;
  color: lightgray;
}
a {
  color: inherit;
}
a:hover {
  color: skyblue;
  text-decoration: none;
}
.card-title {
  margin-bottom: 0;
  font-size: 0.9rem;
  color: white !important;
}
.card-text {
  font-size: 0.7rem;
}
.col {
  padding-bottom: 3rem;
}
.card {
  background-color: #294058;
}
.header {
  padding: 15px;
  text-align: center;
  font-weight: bold;
}
.game-card:hover {
  border: solid 2.5px skyblue;
}
.game-img {
  opacity: 1 !important;
}
</style>
