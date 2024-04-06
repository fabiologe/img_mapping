<template>
  <div>
    <button @click="deleteImages">CLEAN SERVER CACHE</button>
  </div>
</template>

<script>
import axios from 'axios';
const path = 'http://localhost:5000/';

export default {
  methods: {
    async deleteImages() {
      try {
        // Make a POST request to delete all JPEGs in the specified directory
        const directory = 'jpgs/gps'; // or any other directory you want to delete images from
        const response = await axios.post(`${path}delete_jpgs`, { directory });
        console.log('Response from Backend:', response.data);
        alert('CACHE CLEANED');
      } catch (error) {
        console.error("Error deleting images:", error);
        alert('Failed to delete images');
      }
    }
  }
}
</script>




