<script setup>
import JpgUpload from './components/JpgUpload.vue'
import GpsMap from './components/GpsMap.vue'
import PermStorage  from './components/PermStorage.vue';
import LoadStorage from './components/LoadStorage.vue';
import ListStorage  from './components/ListStorage.vue';
import DeleteJpgs from './components/DeleteJpgs.vue'
</script>

<template>
  <div id="app">
    <header>
      <div class="wrapper">

      </div>
    </header>

    <main>
      <JpgUpload />
      <GpsMap/>
<<<<<<< HEAD
      <ListStorage/>
      <PermStorage/>
      <LoadStorage/>
      <DeleteJpgs/>
=======
      <LoadStorage/>
      <PermStorage/>
      <ListStorage/>
>>>>>>> 8b9bea2f081cd4630e2333cc2cd716321d79abba
    </main>
  </div>
</template>
<style scoped>
header {
  line-height: 1;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>

