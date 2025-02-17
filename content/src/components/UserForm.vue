<template>
  <div class="user-form">
    <div class="header">
      <h1 class="brand">Yodiko</h1>
      <img :src="userIcon" alt="User Icon" class="user-icon" />
    </div>
    <div class="user-info">
      <div class="user-details">
        <h2>{{ userName }}</h2>
        <p>{{ userRole }}</p>
      </div>
    </div>
    <p class="greeting">Hello {{ userName }}, seems like you are looking for some data in the projects folder. How can I help you?</p>
    <textarea v-model="message" placeholder="Your message here..." rows="4"></textarea>
    <div class="buttons">
      <button @click="submitMessage">Send</button>
      <button @click="closeWindow">Close</button>
    </div>
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
      message: '',
      typewriterText: 'I need to perform a task to...please help.', // Text to be typed out
      typewriterIndex: 0 // Current index of the text being typed
    };
  },
  mounted() {
    this.typeWriter();
  },
  methods: {
    typeWriter() {
      if (this.typewriterIndex < this.typewriterText.length) {
        this.message += this.typewriterText.charAt(this.typewriterIndex);
        this.typewriterIndex++;
        setTimeout(this.typeWriter, 100); // Adjust the speed of typing here
      }
    },
    submitMessage() {
      // this.message = ''; // Clear the input after submission
      if (window.pyqt) {
        window.pyqt.close_window(); // Call the close_window signal
      }
    },
    closeWindow() {
      console.log("Close button clicked"); // Debug statement
      if (window.pyqt) {
        console.log("Emitting terminate_app signal"); // Debug statement
        window.pyqt.terminate_app(); // Call the terminate_app signal
      }
    }
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  font-family: 'Roboto', sans-serif;
  background-color: #f4f4f9;
}

.user-form {
  width: 100%;
  height: 100%; /* Use full height of the window */
  max-width: 600px;
  margin: 0 auto; /* Center the form horizontally */
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.brand {
  font-weight: 700;
  font-size: 24px;
  color: #333;
}

.user-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.user-icon {
  width: 80px;
  height: 80px;
  border-radius: 50%;
}

.user-details {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  margin-left: auto;
}

.user-details h2 {
  margin: 0;
  font-size: 20px;
  color: #333;
}

.user-details p {
  margin: 0;
  color: #777;
}

.greeting {
  margin-bottom: 20px;
  color: #555;
  text-align: left;
}

textarea {
  flex-grow: 1; /* Allow the textarea to grow and fill the available space */
  width: 100%;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  resize: none;
  box-sizing: border-box;
  font-size: 16px;
  color: #333;
  margin-bottom: 20px;
}

.buttons {
  display: flex;
  justify-content: space-between;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

button:last-child {
  margin-left: auto;
  background-color: #dc3545;
}

button:last-child:hover {
  background-color: #c82333;
}

button:nth-child(3) {
  background-color: #6c757d;
}

button:nth-child(3):hover {
  background-color: #5a6268;
}
</style>
