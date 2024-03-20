<template>
  <div class="upload-container">
    <p>🛰️</p>
    <input type="file" multiple @change="submitFiles">
    <button type="button" class="btn btn-success btn-sm" @click="submitFiles">Submit</button>

    <template v-if="showWarning">
    <p class="warning-message">⚠️ Invalid file extension detected! ⚠️</p>
    <button type="button" @click="confirmReload">Reload</button>
    </template>
  </div>
</template>

<script>
import axios from 'axios'

const path = 'http://localhost:5000/upload_tiffs'
const allowedExtensions = ['tif']; // Allowed file extensions (adjust as needed)

export default {
  data() {
    return {
      showWarning: false,
      errorMessage: '',
      filenames: [],
    }
  },
  methods: {
  confirmReload() {
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
  const formData = new FormData();
  for (let i = 0; i < files.length; i++) {
        formData.append('tif', files[i]); // Append all files with the same key 'jpg'
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
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1em;
  }

  .warning-container {
    display: flex;
    flex-direction: column;
  }

  .warning-message {
    font-size: 1rem;
    color: red;
    white-space: nowrap; /* Prevent line breaks */
  }
</style>


