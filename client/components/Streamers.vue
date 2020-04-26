<template>
  <div>
    <div v-for="streamer in listOfStreamers" v-bind:key="streamer.name" class="row">
      <h1 class="streamer-name">{{ streamer.user_name }}</h1>
      <h3 class="streamer-name">{{ streamer.viewer_count }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "Streamers",
  props: {
    listOfStreamers: Array
  },
  data() {
    return {};
  },
  methods: {}
};
</script>

<style>
.form-container {
  display: flex;
  flex-direction: column;
  background-color: lightblue;
}
.streamer-name {
  padding: 15px;
  text-align: center;
  font-weight: bold;
}

.header {
  padding: 15px;
  text-align: center;
  font-weight: bold;
}
</style>
