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

.header {
  display: flex;
  justify-content: space-between;
  width: 100%;
  align-items: center;
  margin-bottom: 20px;
}

.brand {
  font-weight: bold;
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

.greeting {
  margin-bottom: 10px;
  text-align: left;
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

.buttons {
  display: flex;
  width: 100%;
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

button:last-child {
  margin-left: auto; /* Move the last button (Close) to the right */
}
</style>
