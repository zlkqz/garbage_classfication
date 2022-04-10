<template>
  <div style="width: 100%;height: 100%">
    <garbage-rec @selectFile="selectFile"></garbage-rec>
    <enter-game @click="jumpOut"/>
    <select-file v-show="newWindow" @cancelWindow="this.newWindow = false" ref="chooseFile"></select-file>
  </div>
</template>

<script>
import EnterGame from './components/EnterGame.vue'
import GarbageRec from './components/GarbageRec.vue'
import SelectFile from './components/SelectFile.vue'

export default {
  name: 'App',
  data(){
    return{
      newWindow: false
    }
  },
  components: {
    GarbageRec,
    EnterGame,
    SelectFile
  },
  methods: {
    selectFile(){
      this.newWindow = true;
      this.$refs.chooseFile.boxopacity = 0;
      this.$refs.chooseFile.fadeIn();
    },
    jumpOut(){
      window.location.href= "http://1.117.150.150:8080/project/entrance/game/index.html";
    }
  }
}
</script>

<style>
  * {
    margin: 0;
    padding: 0;
  }
  body {
    background-image: url("../public/background.png");
    background-size: 1396px 767px;
    background-size: 100% 100%;
    background-position: center 0%;
    background-repeat: no-repeat;
    background-attachment: fixed;
    position: relative;
    overflow-y: hidden;
  }
</style>
