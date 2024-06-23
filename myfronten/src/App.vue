<style>
@import './assets/FormComponent.css';

/* Gaya tambahan untuk #app */
#app {
  font-family: Arial, Helvetica, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  flex-direction: column;
}

h1 {
  margin-bottom: 20px;
}
</style>

<template>
  <div id="app">
    <h1>Vue.js Form Input</h1>
    <FormComponent />
  </div>
</template>

<script>
  import FormComponent from './components/FormComponent.vue';

  export default {
    name: 'App',
    components: {
      FormComponent
    }
  };
</script>