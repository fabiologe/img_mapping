<template>
    <div class="upload-container">
      <p>🗺️</p>
      <button type="button" class="btn btn-success btn-sm" @click="showMap">Show Map</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  const path = 'http://localhost:5000/';

  export default {
    data() {
      return {
        // No map-related properties needed for this version
      };
    },
    methods: {
      async showMap() {
        try {
          const response = await axios.get(`${path}/check_jpgs`);
          console.log('Response from Backend:', response.data);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },
    },
    mounted() {
      this.showMap();
    },
  };

  </script>

<style scoped>
/* Add any specific styles for your map container or button here */
</style>
