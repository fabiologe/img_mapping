<template>
  <div class="map-container">
    <l-map :zoom="zoom" :center="center">
      <l-tile-layer
        :url="url"
        :attribution="attribution"
        
      ></l-tile-layer>
      <!-- Add markers, polygons, etc. here -->
    </l-map>
  </div>
</template>

<script>
import { ref } from 'vue';
import { LMap, LTileLayer } from '@vue-leaflet/vue-leaflet';

export default {
  components: {
    LMap,
    LTileLayer,
  },
  setup() {
    const center = ref([49.3132325, 7.2576813]);
    const zoom = ref(15);
    const url = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    const attribution = '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'

    return { center, zoom, url, attribution };
  },
};
</script>

<style>
.map-container {
  border: 2px solid black;
  overflow: hidden;
  height: 768px;
  width: 1024px;
}
</style>


