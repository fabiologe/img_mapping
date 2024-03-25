<template>
  <div style="height: 75vh; width: 50vw;">
    <l-map
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
          <a href="#" @click="showImage(image.filename)">View Image</a>
          <img v-if="imageUrl" :src="imageUrl" alt="Image">
        </l-popup>
      </l-marker>
    </l-map>
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
      imageData: {
        0: { filename: "32U_373366_5463738_21022024_100529.jpg", latitude: 49.3132325, longitude: 7.2576813 },
        1: { filename: "32U_373379_5463759_21022024_100455.jpg", latitude: 49.3134245, longitude: 7.2578506 },
        2: { filename: "32U_373380_5463758_21022024_100453.jpg", latitude: 49.3134223, longitude: 7.2578657 },
        3: { filename: "32U_373380_5463759_21022024_100502.jpg", latitude: 49.3134253, longitude: 7.2578587 },
        4: { filename: "32U_373395_5463752_21022024_100422.jpg", latitude: 49.3133692, longitude: 7.2580642 }
      },
      imageUrl: '',
      avgLat: 0, 
      avgLng: 0
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
      try {
        // Send a GET request to the backend to retrieve the image URL
        const response = await axios.post(`${path}/serve_jpgs`, { filename })
        
        // Create a data URL from the received image data
        const imageUrl = `data:image/jpeg;base64,${response.data}`;
        
        // Update imageUrl with the received URL
        this.imageUrl = imageUrl;
      } catch (error) {
        console.error("Error fetching image:", error);
      }
    },
  },
  mounted(){
    const numImages = Object.keys(this.imageData).length;
    let totalLat = 0;
    let totalLng = 0;
    for (const image of Object.values(this.imageData)) {
        totalLat += image.latitude;
        totalLng += image.longitude;
    }
    this.avgLat = totalLat / numImages;
    this.avgLng = totalLng / numImages;
  },
};

</script>