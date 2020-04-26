<template>
  <div>
    <div v-for="chunk in productChunks" v-bind:key="chunk" class="row">
      <div v-for="stream in chunk" v-bind:key="stream.name" class="col-sm-3 card-padding">
        <StreamCard v-bind:stream="stream" />
      </div>
    </div>
  </div>
</template>

<script>
import _ from "lodash";
import StreamCard from "~/components/StreamCard.vue";
export default {
  name: "StreamDeck",
  components: {
    StreamCard
  },
  props: {
    listOfStreams: Array
  },
  data() {
    return {};
  },
  methods: {},
  computed: {
    productChunks() {
      return _.chunk(Object.values(this.listOfStreams), 4);
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
.col-sm-3 {
  padding: 5px !important;
}
.row {
  padding-top: 15px;
}

.header {
  padding: 15px;
  text-align: center;
  font-weight: bold;
}
.card-padding {
  padding-right: 15px !important;
  padding-left: 15px !important;
}
</style>
