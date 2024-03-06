<template>
  <div>
    <!-- For JPG files -->
    <label for="jpgFileInput" class="file-label">{{ selectedJpgFileName || 'Select JPG Files' }}</label>
    <input id="jpgFileInput" type="file" accept=".jpg" multiple @change="handleJpgUpload" class="file-input"> 

    <!-- Progress bar -->
    <div class="progress-container" v-if="selectedFileName">
      <div class="progress-bar-container">
        <div class="progress-bar" :style="{ width: uploadProgress + '%' }"></div>
      </div>
      <div class="progress-text">{{ uploadProgress }}%</div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const uploadProgress = ref(0);
const selectedFileName = ref('');

const handleJpgUpload = async (event) => {
  const files = event.target.files;
  const formData = new FormData();

  // Update selectedFileName to show progress bar
  selectedFileName.value = `${files.length} file(s) selected`;

  // Append all selected files to the FormData object
  Array.from(files).forEach((file) => {
    formData.append('jpg', file);
  });

  try {
    const response = await fetch('http://localhost:5000/upload_jpgs', {
      method: 'POST',
      body: formData,
      // Optional: Add headers if needed
    });

    if (response.ok) {
      // File upload successful
      console.log('Files uploaded successfully.');
      // Handle any further actions or UI updates

      // Start the progress animation
      uploadProgress.value = 0;
      const interval = setInterval(() => {
        uploadProgress.value += 10;
        if (uploadProgress.value >= 100) {
          clearInterval(interval);
          // Reset input and progress after animation
          selectedFileName.value = '';
          uploadProgress.value = 0;
        }
      }, 500);
    } else {
      // Handle error
      console.error('Files upload failed.');
      // Display error message or take appropriate action
    }
  } catch (error) {
    console.error('An error occurred while uploading the files:', error);
    // Display error message or take appropriate action
  }
};
</script>

<style scoped>
/* File input styles */
.file-label {
  display: block;
  padding: 10px;
  border: 2px solid #3498db;
  border-radius: 5px;
  font-size: 16px;
  color: #3498db;
  cursor: pointer;
  transition: border-color 0.3s ease;
}

.file-input {
  display: none; /* Hide the file input */
}

.file-label:hover {
  border-color: #2980b9;
}

/* Progress bar styles */
.progress-container {
  width: 100%;
  margin-top: 10px;
}

.progress-bar-container {
  position: relative;
  width: 100%;
  height: 20px;
  background-color: #f0f0f0;
  border-radius: 10px;
}

.progress-bar {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  background-color: #3498db;
  border-radius: 10px;
  transition: width 0.3s ease; /* Set the default animation duration */
}

.progress-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 14px;
  color: #333;
}
</style>
