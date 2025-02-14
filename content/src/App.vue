<template>
    <div id="app">
      <UserForm />
    </div>
  </template>
  
  <script>
  import UserForm from './components/UserForm.vue';
  
  export default {
    components: {
      UserForm
    }
  };
  </script>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  </style>
  