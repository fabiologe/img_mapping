<template>
    <div>
      <input type="text" v-model="projectId" placeholder="Enter Project ID">
      <button @click="reloadJPGs">Reload JPEGs</button>
    </div>
</template>

<script>
import axios from 'axios'

const path = 'http://localhost:5000/'

export default {
    data() {
        return {
            projectId: '' // Initialize projectId data property
        };
    },
    methods: {
        async reloadJPGs() {
            try {
                // Check if projectId is not empty
                if (this.projectId.trim() !== '') {
                    // Make a GET request to reload JPEGs associated with the project
                    const response = await axios.get(`${path}load_perm_jpgs/${this.projectId}`);

                    console.log('Response from Backend:', response.data);
                    alert('JPEGs reloaded successfully');
                } else {
                    console.error("Project ID is empty.");
                    alert('Please enter a project ID');
                }
            } catch (error) {
                console.error("Error reloading JPEGs:", error);
                alert('Failed to reload JPEGs');
            }
        }
    }
}
</script>

<style scoped>
/* Add your component styles here if needed */
</style>

  