<template>
    <div v-if="projects.length > 0">
      <h2>Project Names:</h2>
      <ul>
        <li v-for="(project, index) in projects" :key="index">{{ project }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  const path = 'http://localhost:5000/'
  
  export default {
    data() {
      return {
        projects: [] // Array to store project names received from the backend
      };
    },
    mounted() {
      // Call the getProjectNames method when the component is mounted
      this.getProjectNames();
    },
    methods: {
      async getProjectNames() {
        try {
          // Make a GET request to retrieve project names from the backend
          const response = await axios.get(`${path}list_projects`);
          // Update the projects array with project names received from the backend
          this.projects = response.data.projects;
          console.log('Project names:', this.projects);
        } catch (error) {
          console.error("Error fetching project names:", error);
          alert('Failed to fetch project names');
        }
      }
    }
  }
  </script>
  
  <style scoped>
  /* Add your component styles here if needed */
  </style>
  