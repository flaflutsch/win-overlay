<template>
  <div class="user-form">
    <div class="user-info">
      <img :src="userIcon" alt="User Icon" class="user-icon" />
      <div class="user-details">
        <h2>{{ userName }}</h2>
        <p>{{ userRole }}</p>
      </div>
    </div>
    <textarea v-model="message" placeholder="Your message here..." rows="4"></textarea>
    <button @click="submitMessage">Absenden</button>
  </div>
</template>

<script>
import userIcon from '@/assets/user-icon.png'; // Adjust the path as necessary

export default {
  data() {
    return {
      userIcon: userIcon, // Use the imported image
      userName: 'John Doe', // Replace with the actual user name
      userRole: 'Verwaltung',
      message: ''
    };
  },
  methods: {
    submitMessage() {
      alert(`Message submitted: ${this.message}`);
      this.message = ''; // Clear the input after submission
      if (window.pyqt) {
        window.pyqt.close_window(); // Call the close_window signal
      }
    }
  }
};
</script>

<style scoped>
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.user-form {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  box-sizing: border-box; /* Ensuring the border is included in the element's dimensions */
  padding: 10px; /* Adding padding to the form */
}

.user-info {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 20px;
}

.user-icon {
  width: 100px; /* Set the width of the icon */
  height: 100px; /* Set the height of the icon */
  border-radius: 50%;
}

.user-details {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  margin-left: auto;
}

textarea {
  width: 100%; /* Set the width to 100% */
  max-width: 600px; /* Set a max-width to ensure it doesn't get too wide */
  margin: 0 auto; /* Center the textarea */
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: none;
  box-sizing: border-box; /* Ensuring the padding and border are included in the element's dimensions */
}

button {
  margin-top: 10px;
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
