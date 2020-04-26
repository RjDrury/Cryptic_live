<template>
  <div class="sidebar-wrapper">
    <b-card class="sidebar">
      <b-card-title class="sidebar-title">
        Suggested
        <br />Streams
      </b-card-title>
      <div class="cards">
        <div class="card1">
          <StreamCard v-bind:stream="suggestedStreams[randomNumber()]"></StreamCard>
        </div>
        <div class="card2">
          <StreamCard v-bind:stream="suggestedStreams[randomNumber()]"></StreamCard>
        </div>
        <div class="card3">
          <StreamCard v-bind:stream="suggestedStreams[randomNumber()]"></StreamCard>
        </div>
        <div class="card4">
          <StreamCard v-bind:stream="suggestedStreams[randomNumber()]"></StreamCard>
        </div>
        <div class="card5">
          <StreamCard v-bind:stream="suggestedStreams[randomNumber()]"></StreamCard>
        </div>
      </div>
    </b-card>
  </div>
</template>

<script>
import StreamCard from "~/components/StreamCard.vue";
export default {
  name: "Sidebar",
  components: {
    StreamCard
  },
  props: {
    suggestedStreams: Array
  },
  data() {
    return {};
  },
  methods: {
    randomNumber: function() {
      return Math.ceil(Math.random() * (50 - 0));
    }
  }
};
</script>

<style>
.sidebar-wrapper {
  align-content: center;
  position: absolute;
}
.sidebar {
  width: 14rem;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-align: left;
  border: 1px solid;
  margin-top: 15px;
  background-color: #28364b !important;
}
.sidebar-title {
  font-size: 20pt !important;
  text-align: center;
  padding-bottom: 15px;
  color: lightgrey !important;
}
.cards {
  width: 80%;
}

.card5,
.card4,
.card3,
.card2,
.card1 {
  max-width: fit-content;
  max-height: fit-content;
  position: relative;
  left: 11%;
  margin-bottom: 20px;
}
</style>
