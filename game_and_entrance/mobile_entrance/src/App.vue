<template>
  <div style="height: 100%; weight: 100%">
    <div class="cover" v-show="hasGotFile"></div>
    <img class="title" src="./assets/title.png">
    <div v-show="wrongPut" class="warning">只能接收png/jpg/jpeg<br>&emsp;但您选择为{{filetype}}</div>
    <div class="selectFile" @click="selectFile">选择图片</div>
    <input
      style="display: none"
      type="file"
      ref="selectFile"
      accept="image/*"
      @change="getFile($event)"
    />
    <transition name="gradual">
      <show-result
        v-show="hasGotFile"
        :imgsrc="this.imgSrc"
        :classification="this.classification"
        @getBack="this.getBack"
        ref="showResult"
      />
    </transition>
  </div>
</template>

<script>
import ShowResult from "./components/ShowResult.vue";
import axios from "axios";

export default {
  name: "App",
  components: { ShowResult },
  data() {
    return {
      wrongPut: false,
      hasGotFile: false,
      classification: "识别中......",
      filetype: '',
      imgSrc: "",
    };
  },
  methods: {
    selectFile() {
      this.$refs.selectFile.dispatchEvent(new MouseEvent("click"));
    },
    toggle() {
      this.hasGotFile = !this.hasGotFile;
    },
    getFile(e) {
      const that = this;
      const file = e.target.files[0];
      if (!file.type.includes('jpeg') && !file.type.includes('jpg') && !file.type.includes('png')){
        that.wrongPut = true;
        that.filetype = file.type.split('/')[1];
        setTimeout(()=> {
          that.wrongPut = false;
        }, 70000)
        return;
      }
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = function (e) {
        that.imgSrc = e.target.result;
        axios({
          url: "http://1.117.150.150:5000/predict",
          method: "post",
          headers: { "Content-Type": "application/json" },
          data: JSON.stringify({
            img: that.imgSrc.split(",")[1],
          })
        })
          .then((res) => {
            that.classification = "识别结果：<strong>"+ res.data+"</strong>";
          })
          .catch((err) => {
            that.classification = "识别失败"
            console.error(err);
          });
        that.toggle();
        that.$refs.showResult.fadeIn();
      };
    },
    getBack() {
      this.toggle();
      const that = this;
      setTimeout(function () {
        that.imgSrc = "";
        that.classification = "识别中......";
      }, 500);
    },
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
html,
body,
#app {
  height: 100%;
  width: 100%;
}
body {
  background: url("assets/background.png") no-repeat center center;
  background-size: 100vw 100vh;
  overflow: hidden;
}
.title {
  position: absolute;
  width: 86vw;
  height: 27vw;
  top: 8vh;
  left: 7vw;
}
.warning {
  position: absolute;
  color: red;
  top: calc(26vh + 32vw);
  left: 29vw;
}
.cover {
  position: relative;
  width: 100%;
  height: 100%;
  background-color: white;
  opacity: 0.2;
  z-index: 1;
}
.selectFile {
  position: absolute;
  top: 28vh;
  left: 17.5vw;
  padding: 5vw 0;
  color: white;
  width: 65vw;
  height: 12vw;
  border: 2px solid white;
  border-radius: 6vw;
  background-color: transparent;
  line-height: 12vw;
  text-align: center;
  font-size: 18px;
  opacity: 0.8;
}
.selectFile:active {
  background-color: rgb(240, 240, 240, 0.4);
}
.gradual-leave-to {
  transform: translateY(100%);
}
.gradual-enter-active,
.gradual-leave-active {
  transition: 0.5s ease-in-out;
}
</style> 
