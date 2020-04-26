<template>
  <div>
    <h1 class="page-title">Top Streams</h1>
    <div class="sidebar-wrapper">
      <Sidebar v-bind:suggestedStreams="stream_list"/>
    </div>
    <div class="container">
      <StreamDeck v-bind:listOfStreams="stream_list" />
    </div>
  </div>
</template>

<script>
import StreamDeck from "~/components/StreamDeck.vue";
import Sidebar from "~/components/Sidebar.vue";
export default {
  components: {
    StreamDeck,
    Sidebar
  },
  layout: "",
  data() {
    return {
      stream_list: []
    };
  },
  async asyncData({ $axios }) {
    const streams = await $axios.get("http://localhost:5000/topstreamers");
    return {
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
body {
  background: #1f2b3b;
}
  .sidebar-wrapper{
    position: absolute;
    margin-left: 82%;
  }
</style>
