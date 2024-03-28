<template>
    <div>
      <button @click="reloadMap">Reload Map</button>
      <div style="height: 75vh; width: 100vw;">
        <l-map
          v-model="zoom"
          v-model:zoom="zoom"
          :center="[avgEasting, avgNorthing]"
          @move="log('move')"
        >
        <!--Need to build url form tiff which is stored in backend /map_tiles-->
          <l-tile-layer
            url=""
          ></l-tile-layer>
          <l-control-layers />
          
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
        avgEasting: 0, 
        avgNorthing: 0
      };
    },
    computed: {
      iconUrl() {
        return `https://placekitten.com/${this.iconWidth}/${this.iconHeight}`;
      },
      iconSize() {
        return [this.iconWidth, this.iconHeight];
      },
    },
    methods: {
      log(a) {
        console.log(a);
      },
      async showImage(filename) {
        try {//Need to edit path and new blueprints need to be created
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
          
        } catch (error) {
          console.error("Error fetching image data:", error);
          alert('Failed to fetch image data. Please try again later.');
        }
      },
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