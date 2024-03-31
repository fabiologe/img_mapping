<template>
  <div style="height: 350px;">
    <div class="info" style="height: 15%">
      <span>Center: {{ center }}</span>
      <span>Zoom: {{ zoom }}</span>
      <span>Bounds: {{ bounds }}</span>
  </div>
  <l-map
    ref="map"
    :crs="crs"
    :zoom="zoom"
    :center="center"
    @update:zoom="zoomUpdated"
    @update:center="centerUpdated"
    @update:bounds="boundsUpdated"
     style="height: 75vh; width: 100vw;"
  >
    <l-tile-layer
        :url="url"
        :attribution="attribution"
        
    />
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
import { CRS, latLng} from "leaflet";
import axios from 'axios';
import "proj4leaflet";
import proj4 from "proj4";

const UtmCrs = new L.Proj.CRS(
  'EPSG:32632',
  '+proj=utm +zone=32 +ellps=WGS84 +datum=WGS84 +units=m +no_defs',
  {
    resolutions: [
            4000, 3750, 3500, 3250, 3000, 2750, 2500, 2250, 2000, 1750, 1500, 1250, 1000, 750, 650, 500, 250, 100, 50, 20, 10, 5, 2.5, 2, 1.5, 1, 0.5
          ],
          origin: [373179, 5463515]
          //[373179, 5463515]
  })

export default {
  components: {
    LMap,
    LTileLayer
  },
  data() {
    return {
      zoom: 3,
      center: [49.311193, 7.255175],
      bounds: null,
      crs: UtmCrs,
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      
    };
  },
  methods: {
    zoomUpdated (zoom) {
      this.zoom = zoom;
    },
    centerUpdated (center) {
      this.center = center;
    },
    boundsUpdated (bounds) {
      this.bounds = bounds;
    }
  }
};
</script>


