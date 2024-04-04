<template>
  <div>
    <button @click="reloadMap">Reload Map</button>
    <div style="height: 75vh; width: 100vw;">
      <l-map :use-global-leaflet="false"
        v-model="zoom"
        v-model:zoom="zoom"
        :center="[avgLat, avgLng]"
        @move="log('move')"
      >
        <l-tile-layer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        ></l-tile-layer>
        <l-control-layers />
        <l-marker
          v-for="(image, index) in imageData"
          :key="index"
          :lat-lng="[image.latitude, image.longitude]"
          draggable
          @moveend="log('moveend')">
          <l-popup>
            <p>{{ image.filename }}</p>
            <p>GPS: {{ image.latitude }}, {{ image.longitude }}</p>
            <p> UTM-Coordinates: </p>
            <p>{{ image.easting}}, {{image.northing }}</p>
            <a href="#" @click="showImage(image.filename)">View Image</a>
          </l-popup>
        </l-marker>
      </l-map>
    </div>
  </div>
</template>

<script>
import {
  LMap,
  LIcon,
  LTileLayer,
  LMarker,
  LControlLayers,
  LTooltip,
  LPopup,
  LPolyline,
  LPolygon,
  LRectangle,
} from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
import axios from 'axios';
import proj4 from 'proj4';

const path = 'http://localhost:5000/';

export default {
  components: {
    LMap,
    LIcon,
    LTileLayer,
    LMarker,
    LControlLayers,
    LTooltip,
    LPopup,
    LPolyline,
    LPolygon,
    LRectangle,
  },
  data() {
    return {
      zoom: 2,
      iconWidth: 25,
      iconHeight: 40,
      imageData: [],
      avgLat: 0, 
      avgLng: 0
    };
  },
  methods: {
    log(a) {
      console.log(a);
    },
    async showImage(filename) {
      try {
        const response = await axios.post(`${path}/serve_jpgs`, { filename }, { responseType: 'blob' });
        const blob = new Blob([response.data], { type: 'image/jpeg' });
        const imageUrl = URL.createObjectURL(blob);
        const newWindow = window.open(imageUrl, '_blank');
        if (!newWindow) {
          console.error('Failed to open new window. Please check your browser settings.');
        }
      } catch (error) {
        console.error("Error fetching image:", error);
        alert('Failed to fetch the image. Please try again later.');
      }
    },
    async fetchImageData() {
      try {
        const response = await axios.get(`${path}/check_jpgs`);
        console.log('Response from Backend:', response.data);
        this.imageData = response.data;
        this.calculateAverageCoordinates();
      } catch (error) {
        console.error("Error fetching image data:", error);
        alert('Failed to fetch image data. Please try again later.');
      }
    },
    calculateAverageCoordinates() {
      const numImages = this.imageData.length;
      let totalLat = 0;
      let totalLng = 0;
      for (const image of this.imageData) {
        totalLat += image.latitude;
        totalLng += image.longitude;
      }
      this.avgLat = totalLat / numImages;
      this.avgLng = totalLng / numImages;
    },
    async reloadMap() {
      // Clear existing image data
      this.imageData = [];
      // Fetch new image data
      await this.fetchImageData();
    },
  },
  mounted() {
    this.fetchImageData();
  },
};
</script>

