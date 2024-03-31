<template>
  <div>
    <button @click="reloadMap">Reload Map</button>
    <div v-if="mapContainerExists" style="height: 75vh; width: 100vw;">
      <l-map
        v-model="zoom"
        v-model:zoom="zoom"
        :center="[utmEasting, utmNorthing]"
        @move="log('move')"
      >
        <l-tile-layer :url="tiffUrl"></l-tile-layer>
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
import { CRS} from "leaflet";
import axios from 'axios';
import "proj4leaflet";
import proj4 from "proj4";

const path = 'http://localhost:5000/';
const utmProjection = '+proj=utm +zone=32 +ellps=WGS84 +datum=WGS84 +units=m +no_defs';
const gpsProjection = '+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs';

function utmToGPS(easting, northing) {
  const gpsCoords = proj4(utmProjection, gpsProjection, [easting, northing]);
  return { latitude: gpsCoords[1], longitude: gpsCoords[0] };
}

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
      utmEasting : 373179,
      utmNorthing : 5463515, // Need to fetch from backend the tiff file 
      tiffUrl: '', // Initialize tiffUrl here
      mapContainerExists: false,
      gpsCenter: {},

    };
  },
  methods: { 
    log(a) {
      console.log(a);
    },
    async checkTIFF() {
      try {
        const response = await axios.get(`${path}/check_tiffs`);
        tiffData = response.data
        return tiffData
      } catch (error) {
        console.error("Error fetching TIFF data:", error);
        throw new Error('Failed to fetch TIFF data. Please try again later.');
      }
    },
    async serveTIFF(filename) {
      try {
        const response = await axios.post(`${path}/serve_tiffUTM`, { filename }, { responseType: 'blob' });
        const blobTiff = new Blob([response.data], { type: 'image/tiff' });
        const tiffUrl = URL.createObjectURL(blobTiff);
        this.tiffUrl = tiffUrl; // Update tiffUrl with the created URL
        const newWindowTiff = window.open(tiffUrl, '_blank'); // Open new window for .tiff file
        if (!newWindowTiff) {
          console.error('Failed to open new window for TIFF file. Please check your browser settings.');
        }
      } catch (error) {
        console.error("Error fetching image:", error);
        throw new Error('Failed to fetch the image. Please try again later.');
      }
    },
    addTIFFLayerToMap(tiffUrl) {
      // Define your UTM projection
      const utm32NCrs = new L.Proj.CRS(
        'EPSG:32632',
        '+proj=utm +zone=32 +ellps=WGS84 +datum=WGS84 +units=m +no_defs',
        {
          resolutions: [
            4000, 3750, 3500, 3250, 3000, 2750, 2500, 2250, 2000, 1750, 1500, 1250, 1000, 750, 650, 500, 250, 100, 50, 20, 10, 5, 2.5, 2, 1.5, 1, 0.5
          ],
          origin: [373179, 5463515]
        }
      );

      // Create Leaflet map with custom UTM projection
      const map = L.map('map', {
        crs: utm32NCrs,
        zoom: 2,

      });

     const xmin=  373179 
     const  ymin=  5463515 
     const  xmax= 374209 
      const ymax= 5464087
      L.imageOverlay(tiffUrl, [[xmin, ymin], [xmax, ymax]]).addTo(map);

      
      map.fitBounds([[xmin, ymin], [xmax, ymax]]);
    },
    async reloadMap() {
      try {
        this.tiffData = [];
        const tiffData = await this.checkTIFF();
        if (tiffData.length > 0) {
          const firstFilename = tiffData[0].filename;
          await this.serveTIFF(firstFilename);
        } else {
          console.error('No TIFF data available.');
        }
      } catch (error) {
        console.error('Error reloading map:', error);
      }
    },
  },
  mounted() {
    document.addEventListener('DOMContentLoaded', () => {
      this.reloadMap();
      this.mapContainerExists = true;
     
    });
  }
};
</script>

<template>
  <div>
    <button @click="reloadMap">Reload Map</button>
    <div v-if="mapContainerExists" style="height: 75vh; width: 100vw;">
      <l-map
        v-model="zoom"
        :center="[utmEasting, utmNorthing]"
        @move="log('move')"
      >
        <l-tile-layer :url="tiffUrl"></l-tile-layer>
        <l-control-layers />
      </l-map>
    </div>
  </div>
</template>

<script>
import {
  LMap,
  LTileLayer,
  LControlLayers,
} from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
import "proj4leaflet";
import proj4 from "proj4";
import test1Tiff from './test_1.tif'

const utmProjection = '+proj=utm +zone=32 +ellps=WGS84 +datum=WGS84 +units=m +no_defs';
const gpsProjection = '+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs';

function utmToGPS(easting, northing) {
  const gpsCoords = proj4(utmProjection, gpsProjection, [easting, northing]);
  return { latitude: gpsCoords[1], longitude: gpsCoords[0] };
}

export default {
  components: {
    LMap,
    LTileLayer,
    LControlLayers,
  },
  data() {
    return {
      zoom: 2,
      utmEasting: 373179,
      utmNorthing: 5463515,
      mapContainerExists: false,
      tiffUrl: test1Tiff, // Replace with the actual URL of your TIFF image
    };
  },
  methods: { 
    log(a) {
      console.log(a);
    },
    addTIFFLayerToMap(tiffUrl) {
      // Define your UTM projection
      const utm32NCrs = new L.Proj.CRS(
        'EPSG:32632',
        '+proj=utm +zone=32 +ellps=WGS84 +datum=WGS84 +units=m +no_defs',
        {
          resolutions: [
            4000, 3750, 3500, 3250, 3000, 2750, 2500, 2250, 2000, 1750, 1500, 1250, 1000, 750, 650, 500, 250, 100, 50, 20, 10, 5, 2.5, 2, 1.5, 1, 0.5
          ],
          origin: [373179, 5463515]
        }
      );

      // Create Leaflet map with custom UTM projection
      const map = L.map('map', {
        crs: utm32NCrs,
        zoom: this.zoom,
      });

      // Set the bounding box coordinates of your TIFF image
      const xmin = 373179;
      const ymin = 5463515;
      const xmax = 374209;
      const ymax = 5464087;

      // Add TIFF image overlay to the map
      L.imageOverlay(tiffUrl, [[xmin, ymin], [xmax, ymax]]).addTo(map);

      // Fit the map view to the TIFF image bounds
      map.fitBounds([[xmin, ymin], [xmax, ymax]]);
    },
    reloadMap() {
      this.mapContainerExists = true;
      this.addTIFFLayerToMap(this.tiffUrl);
    },
  },
  mounted() {
    this.reloadMap();
  }
};
</script>