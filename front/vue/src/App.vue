<script setup>
import TiffUpload from './components/TiffUpload.vue'
import JpgUpload from './components/JpgUpload.vue'
import GpsMap from './components/GpsMap.vue'
import PermStorage from './components/PermStorage.vue'
import ListStorage from './components/ListStorage.vue'
import LoadStorage from './components/LoadStorage.vue'
</script>

<template>
  <div id="app">
    <header>
      <div class="wrapper">

      </div>
    </header>

    <main>
      <!--<TiffUpload />-->
      <JpgUpload/>
      <GpsMap/>
      <!--<LoadStorage/>
      <PermStorage/>
      <ListStorage/>-->
    </main>
  </div>
</template>
<style scoped>

</style>


