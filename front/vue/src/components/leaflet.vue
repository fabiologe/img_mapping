// Import Leaflet CSS
import 'leaflet/dist/leaflet.css';

// Import Leaflet library
import L from 'leaflet';

<template>
    <div id="map"></div>
  </template>
  
  <script>
  import 'leaflet/dist/leaflet.css';
  import L from 'leaflet';
  
  export default {
    name: 'LeafletMap',
    mounted() {
      this.initMap();
    },
    methods: {
      initMap() {
        // Initialize the map
        const map = L.map('map').setView([51.505, -0.09], 13);
  
        // Add a tile layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);
  
        // Add markers, layers, etc.
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add any custom styles for the map container */
  #map {
    height: 400px; /* Adjust the height as needed */
  }
  </style>
  