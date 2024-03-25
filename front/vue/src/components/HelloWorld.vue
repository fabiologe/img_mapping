<template>
  <div class="container">
    <div class = "showButton">
      <p>🗺️</p>
      <button type="button" class="btn btn-success btn-sm" @click="showMap">Show Map</button>
    </div>
    <div class="map-container">
      <l-map style="width: 100%; height: 100%" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      </l-map>
    </div>
  </div>
</template>
//const response = await axios.get(`${path}/check_jpgs`);
// console.log('Response from Backend:', response.data);
imageData = response.data


<script>
import axios from 'axios';
import { ref } from 'vue'; 
import { LMap, LTileLayer, LMarker, LPopup } from '@vue-leaflet/vue-leaflet'; 

const path = 'http://localhost:5000/';
export default {components: {
  LMap,
  LTileLayer,
  LMarker
},
  data() {
    return {
    zoom: 13,
    center: [49.3132, 7.2577],
    mapUrl: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
    mapAttribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      };
  },
  methods: {
    async showMap() {
      try {
      
       const imageData = {
        0: { filename: "32U_373366_5463738_21022024_100529.jpg", latitude: 49.3132325, longitude: 7.2576813 },
        1: { filename: "32U_373379_5463759_21022024_100455.jpg", latitude: 49.3134245, longitude: 7.2578506 },
        2: { filename: "32U_373380_5463758_21022024_100453.jpg", latitude: 49.3134223, longitude: 7.2578657 },
        3: { filename: "32U_373380_5463759_21022024_100502.jpg", latitude: 49.3134253, longitude: 7.2578587 },
        4: { filename: "32U_373395_5463752_21022024_100422.jpg", latitude: 49.3133692, longitude: 7.2580642 }
      };
      // Calculate average latitude and longitude
      const numImages = Object.keys(imageData).length;
      let totalLat = 0;
      let totalLng = 0;
      for (const image of Object.values(imageData)) {
          totalLat += image.latitude;
          totalLng += image.longitude;
      }
      const avgLat = totalLat / numImages;
      const avgLng = totalLng / numImages;

      const map = LMap('map', {
          center: [avgLat, avgLng], // Set the map center based on average latitude and longitude
          zoom: 13 // Set the initial zoom level
      });

      const tiles = LTileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19,
          attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);

      this.markers = []; // Clear existing markers

      for (const image of Object.values(imageData)) {
          const marker = LMarker([image.latitude, image.longitude]).addTo(map);
          marker.bindPopup(`<b>${image.filename}</b>`).openPopup();
          this.markers.push(marker);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  },
},
};
</script>

<style scoped>

.container {
position: relative;
height: 100vh;
display: flex;
flex-direction: column;
}

.showButton {
position: absolute;
top: 10px;
left: 10px;
z-index: 1000; /* Ensure buttons are above the map */
}

.map-container {
height: 600px;
width: 400px;
}

</style>