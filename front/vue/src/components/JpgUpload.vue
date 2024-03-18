<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sandstone/bootstrap.min.css" integrity="sha384-zEpdAL7W11eTKeoBJK1g79kgl9qjP7g84KfK3AZsuonx38n8ad+f5ZgXtoSDxPOh" crossorigin="anonymous">
      <div class="col-sm-5">
        <p> Upload jpg's  </p>
        <input type="file" multiple @change="submitFiles">
        <br><br>
        <button type="button" class="btn btn-success btn-sm" @click="submitFiles">Submit</button>
        <p v-if="showWarning" :errorMessage="errorMessage" @close="showWarning = false" class="warning-message">⚠️ wrong file selected ⚠️</p>
        <button type="button" @click="confirmReload" v-if="showWarning">Reload</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const path = 'http://localhost:5000/upload_jpgs'
const allowedExtensions = ['jpg']; // Allowed file extensions (adjust as needed)

export default {
  data() {
    return {
      showWarning: false,
      errorMessage: '',
      filenames: [],
    }
  },
  methods: {
    getFilenames(event) {
      const files = event.target.files;
      this.filenames = [];

      let hasInvalidFiles = false; // Flag to track invalid files
      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const extension = file.name.split('.').pop().toLowerCase();
      
        if (!allowedExtensions.includes(extension)) {
          hasInvalidFiles = true;
        } else {
          this.filenames.push(file.name);
        }
      }
    
      if (hasInvalidFiles) {
        this.showWarning = true; // Set showWarning only if there are invalid files
        this.errorMessage = `Invalid file extension detected!`
        console.log('showWarning:', this.showWarning);
      }
},confirmReload() {
    if (confirm("Invalid files selected. Reload page to clear selection?")) {
      window.location.reload();
    }
  },
  async submitFiles(event) {
  if (!event.target.files.length) {
    console.warn('No files selected for upload!');
    return;
  }

  const files = event.target.files;

  const formData = new FormData();
  for (let i = 0; i < files.length; i++) {
        formData.append('jpg', files[i]); // Append all files with the same key 'jpg'
        console.log(`${files[i].name} uploaded`);
      }

  try {
    const response = await axios.post(path, formData, {
      onUploadProgress: (progressEvent) => {
        const percentage = Math.round((progressEvent.loaded * 100) / progressEvent.total);
        console.log(`Trying to upload ${this.filenames} - Upload progress: ${percentage}%`);
        // Update a progress bar or display a message (see next step)
      }
    });
    if (response.data.status === 'success') {
      console.log('Files uploaded successfully!');
      // Display a success message to the user (see next step)
    } else {
      console.error('Error uploading files:', response.data.message);
      // Optionally: display user-friendly error message from server response
    }
  } catch (error) {
    console.error('Error uploading files:', error);
    // Handle server errors or other unexpected issues
  }
}
  }
}
</script>
<style scoped>
  .upload-container {
    display: flex; /* Enable flexbox layout */
    align-items: center; /* Align elements vertically */
  }

  .warning-message {
    margin-left: 0px;
    /* Optional: add spacing between button and message */
    white-space: nowrap; /* Prevents line breaks */
    /* Other styles for the message */
  }
</style>



