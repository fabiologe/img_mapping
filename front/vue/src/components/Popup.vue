<template>
    <div v-if="show" class="warning-popup">
      <p>{{ errorMessage }}</p>
      <button @click="$emit('close')">Close</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      show: {
        type: Boolean,
        default: false,
      },
      errorMessage: {
        type: String,
        default: '',
      },
    },
  }
  </script>
  
  <style scoped>
  .warning-popup {
    position: absolute; /* Position the popup near the button (adjust as needed) */
    /* ... other styles for the popup */
  }
  </style>
  
  