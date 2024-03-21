<template>
    <div class="upload-container">
      <p>🗺️</p>
      <button type="button" class="btn btn-success btn-sm" @click="showMap">Show Map</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  const path = 'http://localhost:5000/'
  
  export default {
    data() {
      return {
        hasJPG: false, 
        hasTIF: false,
      }
    },
    methods: {
      async showMap() {
        try {
          // Check for files in /jpg and /map_tiles directories
          const jpgResponse = await axios.get(`${path}/jpg/has_files`);
          const mapTilesResponse = await axios.get(`${path}/map_tiles/has_files`);
  
          if (jpgResponse.data && mapTilesResponse.data) {
            // Both directories have files, trigger map component (replace with actual logic)
            console.log('Show map component!'); // Replace with actual map component rendering logic
          } else {
            console.error('Missing files! Either /jpg or /map_tiles directory is empty.');
          }
        } catch (error) {
          console.error('Error checking for files:', error);
          // Handle errors appropriately (e.g., display error message to user)
        }
      },
      
    },
    computed: {
      // Disable button if no files are uploaded based on hasFiles flag
      disabled() {
        return !this.hasFiles;
      }
    }
  }
  </script>
  
  <style scoped>
    /* ... existing styles ... */
  </style>
  