
<template>
  <div>
    <a :href="getLinkToStream(stream)">
      <b-card class="stream-card">
        <b-card-img :src="getThumbnail(stream.thumbnail)" class="stream-image" />
        <b-card-title>
          <a :href="getLinkToStream(stream)">{{stream.name}}</a>
        </b-card-title>
        <b-card-text>
          <a :href="getLinkToStream(stream)">{{stream.title}}</a>
        </b-card-text>
        <b-card-text>
          <a :href="getLinkToStream(stream)">{{stream.viewers}} viewers</a>
        </b-card-text>
      </b-card>
    </a>
  </div>
</template>

<script>
export default {
  name: "StreamCard",

  props: {
    stream: Object
  },
  data() {
    return {};
  },
  methods: {
    getThumbnail(thumbnailLink) {
      var newlink = thumbnailLink;
      if (thumbnailLink != null) {
        var newlink = newlink.replace("{width}", "440");
        newlink = newlink.replace("{height}", "380");
      } else {
        newlink = require("../static/Profile_avatar_placeholder_large.png");
      }
      return newlink;
    },
    getLinkToStream(stream) {
      let link = "";
      if (stream.twitch) {
        link = "https://www.twitch.tv/" + stream.name;
      } else if (stream.mixer) {
        link = "https://mixer.com/" + stream.name;
      }
      return link;
    }
  },
  computed: {}
};
</script>

<style>
.stream-card {
  max-width: 15rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-align: left;
  border: hidden;
}
.stream-image {
  width: 100%;
  height: 15vw;
  object-fit: cover;
}
.card-body {
  padding: 5px !important;
  font-size: 0.7rem;
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
.stream-card:hover {
  border: solid 2.5px skyblue;
}
.stream-img {
  opacity: 1 !important;
}
</style>
