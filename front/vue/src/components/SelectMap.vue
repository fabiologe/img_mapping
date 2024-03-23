<template>
    <div class="container">
      <div class = "showButton">
        <p>🗺️</p>
        <button type="button" class="btn btn-success btn-sm" @click="showMap">Show Map</button>
        </div>
      <div id="map" class="map-container"></div>
    </div>
  </template>
  
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
 
  <script>
  import axios from 'axios';
  import L from 'leaflet';
  const path = 'http://localhost:5000/';

  export default {
    data() {
      return {
        map:null,
        markers: []
      };
    },
    methods: {
      async showMap() {
        try {
          //const response = await axios.get(`${path}/check_jpgs`);
         // console.log('Response from Backend:', response.data);
         const imageData = {
          0: { filename: "32U_373366_5463738_21022024_100529.jpg", latitude: 49.3132325, longitude: 7.2576813 },
          1: { filename: "32U_373379_5463759_21022024_100455.jpg", latitude: 49.3134245, longitude: 7.2578506 },
          2: { filename: "32U_373380_5463758_21022024_100453.jpg", latitude: 49.3134223, longitude: 7.2578657 },
          3: { filename: "32U_373380_5463759_21022024_100502.jpg", latitude: 49.3134253, longitude: 7.2578587 },
          4: { filename: "32U_373395_5463752_21022024_100422.jpg", latitude: 49.3133692, longitude: 7.2580642 }
        };
        const map = L.map('map', {
                                  center: [49.313, 7.258], // Set the map center
                                  zoom: 13 // Set the initial zoom level
                  	             });
        const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', 
                                  {
	                              	maxZoom: 19,
	                              	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
	                                }).addTo(map);

        
        this.markers = []; // Clear existing markers

        for (const image of Object.values(imageData)) {
          const marker = L.marker([image.latitude, image.longitude]).addTo(this.map);
          marker.bindPopup(`<b>${image.filename}</b>`).openPopup() // Optional popup with filename
          this.markers.push(marker); // Add marker to the markers array
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
  },
  mounted() {
    

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
  height: 400px;
	width: 600px;
	max-width: 100%;
	max-height: 100%;; /* Ensure map container takes full height */
}
</style>
