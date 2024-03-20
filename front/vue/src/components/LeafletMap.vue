<template>
  <div id="mapContainer" ref="mapContainer" v-if="showMap">
    <button @click="hideMap">Hide Map</button>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import L from "leaflet";

export default {
  setup() {
    const lat = ref(51.505);
    const lng = ref(-0.09);
    const map = ref();
    const mapContainer = ref();
    const showMap = ref(false); // Flag to control map visibility

    onMounted(() => {
      if (window.location.search.includes("showMap=true")) { // Check for URL parameter
        showMap.value = true;
        initializeMap();
      }
    });

    const initializeMap = () => {
      map.value = L.map(mapContainer.value).setView([lat.value, lng.value], 13);
      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      }).addTo(map.value);
    };

    const hideMap = () => {
      showMap.value = false;
      // Optionally: Replace current URL to remove "showMap" parameter
      window.history.replaceState({}, document.title, window.location.origin + window.location.pathname);
    };

    return {
      lat,
      lng,
      map,
      mapContainer,
      showMap,
      hideMap,
    };
  },
};
</script>

<style scoped>
#mapContainer {
  height: 300px; /* Adjust as needed */
  width: 500px;  /* Adjust as needed */
  border: 2px solid red;
}
</style>




  