<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
// import DragE from "../src/components/DragE.vue"
export default {
  name: 'App',
  components: {
  // DragE
      },
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
body{
    position: relative;
    background: url('assets/preview.jpg') no-repeat center center;
    background-size: cover;
}
</style>
