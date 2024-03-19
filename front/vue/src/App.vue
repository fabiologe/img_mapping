<script setup>
//import TiffUpload from './components/TiffUpload.vue'
import LeafletMap from './components/LeafletMap.vue';
import JpgUpload from './components/JpgUpload.vue'
</script>

<template>
  <div id="app" class="app-container">
    <main>
      <div class="components-container">
        <JpgUpload class="jpg-upload" />  <LeafletMap />
      </div>
    </main>
  </div>
</template>

<style scoped>
  /* ... existing styles */

  .components-container {
    display: grid;
    grid-template-rows: auto 1fr;  /* Define rows */
  }
  .jpg-upload {
    width: 100px;  /* Adjust width as needed */
    height: 50px;  /* Adjust height as needed */
    position: absolute;  /* Absolute positioning */
    top: 0;  /* Top position at 0 */
    left: 0;  /* Left position at 0 */
  }
</style>


