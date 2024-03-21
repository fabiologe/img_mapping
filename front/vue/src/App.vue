<script setup>
import TiffUpload from './components/TiffUpload.vue'
import JpgUpload from './components/JpgUpload.vue'
import LeafletMap from './components/LeafletMap.vue'
import SelectMap from './components/SelectMap.vue'
</script>

<template>
  <div id="app">
    <header>
      <div class="wrapper">

      </div>
    </header>

    <main>
      <!--<TiffUpload />
      <JpgUpload />-->
      <LeafletMap/>
      <SelectMap/>
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


