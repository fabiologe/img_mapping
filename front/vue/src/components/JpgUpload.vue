<template>
  <div>
    <input type="file" multiple @change="uploadFiles">
    <div v-if="uploading">
      <progress :value="progress" max="100"></progress>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      uploading: false,
      progress: 0,
      eventSource: null
    };
  },
  methods: {
    uploadFiles(event) {
      this.uploading = true;
      const files = event.target.files;
      const formData = new FormData();
      for (let i = 0; i < files.length; i++) {
        formData.append('jpg', files[i]); // Append all files with the same key 'jpg'
        console.log(`${files[i].name} uploaded`);
      }

      // Reset the file input value to clear the selection
      event.target.value = '';

      fetch('http://localhost:5000/upload_jpgs', {
        method: 'POST',
        body: formData
      })
      .then(response => {
        if (response.ok) {
          this.setupEventSource();
        } else {
          throw new Error('Failed to upload files');
        }
      })
      .catch(error => {
        console.error(error);
        this.uploading = false;
      });
    },
    setupEventSource() {
      this.eventSource = new EventSource('http://localhost:5000/upload_progress');
      this.eventSource.onmessage = (event) => {
        this.progress = parseInt(event.data);
        if (this.progress === 100) {
          this.uploading = false;
          this.eventSource.close();
        }
      };
      this.eventSource.onerror = () => {
        this.eventSource.close();
        this.uploading = false;
      };
    }
  }
};
</script>



