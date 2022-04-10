<template>
    <div class="result-window" :style="{bottom: btmSize + 'vh'}">
      <div class="back" @click="this.$emit('getBack')"><img src="../assets/down.png"></div>
      <div class="img-container"><img :src="imgsrc"></div>
      <hr>
      <div class="result" v-html="classification"></div>
    </div>
</template>

<script>
export default {
  name: "ShowResult",
  props: ['imgsrc','classification'],
  data() {
    return {
      btmSize: -70
    };
  },
  methods: {
    fadeIn(){
      this.btmSize = -70;
      const timer = setInterval(() => {
        this.btmSize = this.btmSize + 3;
        if(this.btmSize >= 0){
          clearInterval(timer);
          this.btmSize = 0
        }
      }, 1);
    }
  }
};
</script>

<style scoped>
.result-window {
  position: absolute;
  z-index: 2;
  width: 100%;
  height: 63vh;
  background-color: rgb(240,240,240);
  border-radius: 1vh 1vh 0 0;
}
.title {
  position: absolute;
  z-index: 2;
  height: 20vh;
}
.img-container{
  width: 72vw;
  height: 44vh;
  margin: 3vw 0 3vw 14vw;
  display: flex;
  justify-content: center;
  align-items: center;
}
img {
  max-width: 100%;
  max-height: 100%;
}
.back {
  margin-left: 43vw;
  margin-top: 4vw;
  width: 14vw;
  height: 7vw;
  background-color: rgb(230,230,230);
  border-radius: 3vw;
  line-height: 7vw;
  text-align: center;
}
.result {
  position: absolute;
  bottom: 3.5vh;
  width: 100%;
  text-align: center;
}
</style>
