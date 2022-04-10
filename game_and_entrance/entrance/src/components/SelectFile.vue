<template>
  <div>
    <div class="cover"></div>
    <div class="operate-window" :style="{ opacity: boxopacity }">
      <div class="top-bar">请上传图片</div>
      <div class="vice-bar">
        <input
          type="file"
          style="display: none"
          ref="fileinput"
          @change="selected()"
        />
        <div class="open-file" @click="openFile">本地文件</div>
        <div class="chosen" v-show="hasInfo">
          <img src="../assets/CG_icon.png" draggable="false" />
          <div class="photo-name">
            {{ photoName }}
          </div>
          <el-progress
            class="progress"
            :percentage="this.percentage"
            color="#6dd37e"
            :status="this.status"
            :stroke-width="8"
            v-show="submitStatus == 1"
          />
          <div v-show="this.submitStatus == 0" class="wait-progress">
            等待上传识别
          </div>
          <div v-show="this.submitStatus == 2" class="result">
            识别结果：<strong>{{ CVResult }}</strong>
          </div>
        </div>
        <div class="warning" v-show="!hasInfo">{{ warning }}</div>
      </div>
      <div class="watch-file" @drop.prevent="getImg($event)" @dragover.prevent>
        请将图片拖拽到此处
      </div>
      <div class="tail-bar">
        <div class="cancel" @click="exit">退出识别</div>
        <div class="submit" @click="recognize">开始识别</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SelectFile",
  data() {
    return {
      CVResult: "",
      hasInfo: false,
      boxopacity: 0,
      warning: "",
      photo: null,
      photoName: "",
      percentage: 0,
      status: "",
      submitStatus: 0,
    };
  },
  methods: {
    init() {
      this.hasInfo = false;
      this.photo = null;
      this.percentage = 0;
      this.submitStatus = 0;
      this.status = "";
    },
    fadeIn() {
      const that = this;
      let i = 0;
      const timer = setInterval(function () {
        i = i + 0.1;
        that.boxopacity = i;
        if (i >= 1) {
          clearInterval(timer);
        }
      }, 40);
    },
    openFile() {
      this.$refs.fileinput.dispatchEvent(new MouseEvent("click"));
    },
    getImg(e) {
      this.init();
      if (e.dataTransfer.items.length == 1) {
        if (
          e.dataTransfer.items[0].type.includes("jpg") ||
          e.dataTransfer.items[0].type.includes("jpeg") ||
          e.dataTransfer.items[0].type.includes("png")
        ) {
          this.photoName = e.dataTransfer.files[0].name;
          this.photo = e.dataTransfer.items[0].getAsFile();
          this.hasInfo = true;
        } else {
          this.warning = "错误：只能接受png/jpg/jpeg文件";
        }
      } else if (e.dataTransfer.items.length > 1) {
        this.warning = "错误：最多只能放入一张图片";
      }
    },
    selected() {
      this.init();
      const file = this.$refs.fileinput.files;
      if (file.length == 1) {
        if (file[0].type.includes("jpg") || file[0].type.includes("jpeg")) {
          this.photoName = file[0].name;
          this.photo = file[0];
          this.hasInfo = true;
        } else {
          this.warning = "错误：只能接受jpg/jpeg文件";
        }
      } else if (file.length > 1) {
        this.warning = "错误：最多只能放入一张图片";
      }
    },
    exit() {
      this.$emit("cancelWindow");
      this.init();
      this.warning = "";
    },
    recognize() {
      const that = this;
      that.submitStatus = 1;
      if (that.photo) {
        const reader = new FileReader();
        reader.readAsDataURL(that.photo);
        reader.onloadend = function (e) {
          axios({
            url: "http://1.117.150.150:5000/predict",
            method: "post",
            headers: { "Content-Type": "application/json"},
            data: JSON.stringify({
              img: e.target.result.split(',')[1]
            }),
            onUploadProgress: (progressEvent) => {
              let progress =
                ((progressEvent.loaded / progressEvent.total) * 100) | 0;
              that.percentage = progress;
            },
          })
            .then((res) => {
              that.status = "success";
              that.submitStatus = 2;
              that.CVResult = res.data;
            })
            .catch(() => {
              that.status = "exception";
            });
        };
      } else {
        this.warning = "错误：尚未选择图片";
        this.init();
      }
    },
  },
};
</script>

<style scoped>
.cover {
  width: 100%;
  height: 100vh;
  background-color: black;
  opacity: 0.5;
}
.operate-window {
  position: absolute;
  z-index: 1;
  height: 537px;
  width: 700px;
  left: calc(50% - 350px);
  top: calc(50% - 269px);
  background-color: white;
}
.top-bar {
  background-color: rgb(248, 248, 248);
  height: 43px;
  width: 100%;
  line-height: 43px;
  text-indent: 1rem;
}
.vice-bar {
  position: relative;
  height: 67px;
}
.open-file {
  position: absolute;
  height: 38px;
  width: 80px;
  background-color: rgb(133, 206, 97);
  border-radius: 6px;
  color: white;
  left: 1rem;
  bottom: 10px;
  line-height: 38px;
  text-align: center;
  font-size: 14px;
}
.warning {
  bottom: 0;
  position: absolute;
  height: 41px;
  right: 1rem;
  color: rgb(245, 108, 108);
  line-height: 38px;
}
.chosen {
  position: absolute;
  bottom: 10px;
  height: 41px;
  width: 220px;
  right: 1rem;
}
.chosen > img {
  width: 41px;
  height: 41px;
}
.progress {
  position: absolute;
  width: 209px;
  left: 48px;
  top: 27px;
}
.wait-progress {
  position: absolute;
  width: 209px;
  left: 48px;
  top: 25px;
  color: gray;
  font-size: 11px;
}
.result {
  position: absolute;
  width: 209px;
  left: 48px;
  top: 22px;
  color: red;
  font-size: 15px;
}
.photo-name {
  position: absolute;
  width: 190px;
  line-height: 20px;
  font-weight: 700;
  left: 48px;
  top: 0;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.watch-file {
  width: 662px;
  height: 345px;
  margin: 0 auto;
  border: 2px gray dashed;
  border-style: dashed;
  border-color: gray;
  line-height: 345px;
  color: rgb(83, 83, 83);
  font-size: 30px;
  text-align: center;
}
.tail-bar {
  width: 100%;
  height: 70px;
  position: relative;
}
.cancel {
  position: absolute;
  height: 38px;
  width: 80px;
  line-height: 38px;
  text-align: center;
  bottom: 13px;
  right: 110px;
  color: white;
  background-color: rgb(203, 203, 203);
  border-radius: 4px;
  font-size: 15px;
}
.submit {
  position: absolute;
  height: 38px;
  width: 80px;
  line-height: 38px;
  text-align: center;
  bottom: 13px;
  right: 15px;
  color: white;
  background-color: rgb(32, 165, 58);
  border-radius: 4px;
  font-size: 15px;
}
.cancel:hover {
  background-color: red;
  cursor: pointer;
}
.submit:hover {
  background-color: rgb(16, 149, 42);
  cursor: pointer;
}
.open-file:hover {
  height: 36px;
  width: 78px;
  line-height: 36px;
  cursor: pointer;
}
</style>
