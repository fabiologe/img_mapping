<template>
  <div>
    <input type="text" v-model="projectName" placeholder="Enter Project Name">
    <button @click="submitProject">Submit</button>
  </div>
</template>

  
  <script>
  import axios from 'axios'

  const path = 'http://localhost:5000/'

  export default {
    data() {
      return {
        projectName: ''
      };
    },
    methods: {
      submitProject() {
          if (this.projectName.trim() !== '') {
            // If project name is provided, do something like perm_save_jpgs()
            this.permSaveJPGs();
          } else {
            // If no project name is provided, do something like delete_jpg()
            console.log('NO Files to save')
          }
      },
      async permSaveJPGs() {
    try {
        // Check if projectName is not empty
        if (this.projectName.trim() !== '') {
            // Make a POST request to save JPEGs associated with the project
            const response = await axios.post(`${path}perm_save`, { project_name: this.projectName });
            console.log('Response from Backend:', response.data);
        } else {
            console.error("Project name is empty.");
        }
    } catch (error) {
        console.error("Error saving JPEGs:", error);
        alert('Failed to store images permanently');
    }
},

     }
  }
  </script>
  
  
  <style scoped>
  /* Add your component styles here if needed */
  </style>
  