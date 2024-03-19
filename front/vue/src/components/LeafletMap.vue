<template>
  <div ref="mapContainer"></div>
</template>

<script>
import { onMounted, ref } from "vue";
import L from "leaflet";

export default {
  setup() {
    const lat = ref(51.505); // Replace with your desired latitude
    const lng = ref(-0.09); // Replace with your desired longitude
    const map = ref();
    const mapContainer = ref();

    onMounted(() => {
      map.value = L.map(mapContainer.value).setView([lat.value, lng.value], 13);
      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      }).addTo(map.value);

      // Optional: Add a draggable marker (uncomment if desired)
      // L.marker([lat.value, lng.value], { draggable: true })
      //   .addTo(map.value)
      //   .on("dragend", (event) => {
      //     console.log(event);
      //   });
    });

    return {
      lat,
      lng,
      map,
      mapContainer,
    };
  },
};
</script>

<style scoped>
  /* Add styles for the map container element here (optional) */
  #mapContainer {
    height: 100px;
    width: 100px;
  }
</style>


  