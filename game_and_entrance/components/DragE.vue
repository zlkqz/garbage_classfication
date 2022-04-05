
<template>
  <div id="DragExample">
    <CountTimer class="CT" ref="CountT"></CountTimer>
    <div class="scorepad">
      <img src="../assets/toolbar.png">
      <span class="pointnum" :style="{color: fontColor}">{{point}}</span>
    </div>
    <div class="tools">
      <div>
        <img
          src="../assets/加时.png"
          @click="addtime()"
          draggable="false"
        /><span class="addtimenum">{{ cnt_addtime }}</span>
      </div>
      <div>
        <img
          src="../assets/清理.png"
          @click="allReload()"
          draggable="false"
        /><span class="clearallnum">{{ cnt_clearall }}</span>
      </div>
    </div>
    <div v-if="Count_turn">
      <img
        src="../assets/加时.png"
        class="Picture timeadd"
        @click="ChangingT()"
        draggable="false"
      />
    </div>
    <div v-if="Clear_turn">
      <img
        src="../assets/清理.png"
        class="Picture clearall"
        @click="ChangingClear()"
        draggable="false"
      />
    </div>
    <div class="rORwTwo" v-show="turn[0]"><img :src="imgUrl_rORw" /></div>
    <div class="rORwOne" v-show="turn[1]"><img :src="imgUrl_rORw" /></div>
    <div class="rORwFour" v-show="turn[2]"><img :src="imgUrl_rORw" /></div>
    <div class="rORwThree" v-show="turn[3]"><img :src="imgUrl_rORw" /></div>
    <VueDragResize
      class="demo"
      @dragstop="onActivatedA(order[0])"
      @dragging="ChangingA()"
      :isActive="true"
      :z="1"
      :isResizable="false"
      ref="apple"
      ><img
        @mouseenter="TouchVideoA()"
        :src="imgUrl[0]"
        class="Picture"
        :style="{ opacity: omoA }"
      />
      <audio
        src="../assets/按钮按键-很酷-用户界面-游戏提示音_系统提示音(Cool _爱给网_aigei_com.mp3"
        id="audioA"
      ></audio>
    </VueDragResize>
    <VueDragResize
      class="demo"
      @dragstop="onActivatedB(order[1])"
      @dragging="ChangingB()"
      :isActive="true"
      :z="1"
      :isResizable="false"
      ref="banana"
      ><img
        @mouseenter="TouchVideoB()"
        :src="imgUrl[1]"
        class="Picture"
        :style="{ opacity: omoB }" /><audio
        src="../assets/按钮按键-很酷-用户界面-游戏提示音_系统提示音(Cool _爱给网_aigei_com.mp3"
        id="audioB"
      ></audio
    ></VueDragResize>
    <VueDragResize
      class="demo"
      @dragstop="onActivatedC(order[2])"
      @dragging="ChangingC()"
      :isActive="true"
      :z="1"
      :isResizable="false"
      ref="cherry"
      ><img
        @mouseenter="TouchVideoC()"
        :src="imgUrl[2]"
        class="Picture"
        :style="{ opacity: omoC }"
      /><audio
        src="../assets/按钮按键-很酷-用户界面-游戏提示音_系统提示音(Cool _爱给网_aigei_com.mp3"
        id="audioC"
      ></audio>
    </VueDragResize>
    <VueDragResize
      class="demo"
      @dragstop="onActivatedD(order[3])"
      @dragging="ChangingD()"
      :isActive="true"
      :z="1"
      :isResizable="false"
      ref="date"
      ><img
        @mouseenter="TouchVideoD()"
        :src="imgUrl[3]"
        class="Picture"
        :style="{ opacity: omoD }"
      /><audio
        src="../assets/按钮按键-很酷-用户界面-游戏提示音_系统提示音(Cool _爱给网_aigei_com.mp3"
        id="audioD"
      ></audio>
    </VueDragResize>
    <VueDragResize
      class="demo"
      @dragstop="onActivatedE(order[4])"
      @dragging="ChangingE()"
      :isActive="true"
      :z="1"
      :isResizable="false"
      ref="egg"
      ><img
        @mouseenter="TouchVideoE()"
        :src="imgUrl[4]"
        class="Picture"
        :style="{ opacity: omoE }" />
      <audio
        src="../assets/按钮按键-很酷-用户界面-游戏提示音_系统提示音(Cool _爱给网_aigei_com.mp3"
        id="audioE"
      ></audio
    ></VueDragResize>
    <div class="TrashCan_K"><img draggable="false" :src="imgUrl_TC_K" /></div>
    <div class="TrashCan_O"><img draggable="false" :src="imgUrl_TC_O" /></div>
    <div class="TrashCan_P"><img draggable="false" :src="imgUrl_TC_P" /></div>
    <div class="TrashCan_R"><img draggable="false" :src="imgUrl_TC_R" /></div>
    <audio
      id="audio"
      :src="
        require('../assets/39辑 - AudioJungel精选合集-快乐的时光(Ha_爱给网_aigei_com.mp3')
      "
    ></audio>
    <audio
      id="audioT"
      :src="
        require('../assets/《天天来塔防》资源素材-Sounds-UI 单板层积材选择(_爱给网_aigei_com.mp3')
      "
    ></audio>
    <audio
      id="PGaudio"
      :src="
        require('../assets/11000游戏常用音效-明亮的提示音_爱给网_aigei_com.mp3')
      "
    ></audio>
    <audio
      id="audioW"
      :src="
        require('../assets/警告-系统警告回答错误-游戏提示_爱给网_aigei_com.mp3')
      "
    ></audio>
    <audio
      id="addtime"
      :src="
        require('../assets/警告-系统警告回答错误-游戏提示_爱给网_aigei_com.mp3')
      "
    ></audio>
    <audio
      id="cleartool"
      :src="require('../assets/游戏成功音效_爱给网_aigei_com.mp3')"
    ></audio>
    <audio
      id="addtimetool"
      :src="require('../assets/跳跃(Jump)_爱给网_aigei_com.mp3')"
    ></audio>
    <audio
      id="clear"
      :src="require('../assets/UI叮咚音效_爱给网_aigei_com.mp3')"
    ></audio>
    <audio
      id="success"
      :src="
        require('../assets/《天天来塔防》资源素材-Sounds-UI 的成功(UI_s_爱给网_aigei_com.mp3')
      "
    ></audio>
  </div>
</template>

<script>
import CountTimer from "../components/CountTimer.vue";
import VueDragResize from "vue-drag-resize";
import TrashCan_K from "../assets/垃圾分类-厨余n.png";
import TrashCan_O from "../assets/垃圾分类-其他n.png";
import TrashCan_P from "../assets/垃圾分类-有害n.png";
import TrashCan_R from "../assets/垃圾分类-可回收n.png";
export default {
  name: "DragE",
  components: {
    VueDragResize,
    CountTimer,
  },
  data() {
    return {
      keyword: "",
      cnt_addtime: 0,
      cnt_clearall: 0,
      point: 0,
      eachpoint: 20,
      continuousPoint: 0,
      fontColor: 'white',
      myFontSize: 30,
      omoA: 1,
      omoB: 1,
      omoC: 1,
      omoD: 1,
      omoE: 1,
      omoT: 1,
      Count_turn: 0,
      Clear_turn: 0,
      timeaddCnt: 0,
      m: [0, 1, 2, 3, 4],
      turn: [0, 0, 0, 0],
      Origin_top: [10, 100, 150, 160, 0], //一开始对于每一个图片在其css中设置一个固定的位置，随后再通过随机的方法得到它的位置
      Origin_left: [600, 400, 200, 710, 900],
      imgUrl: [],
      imgUrl_rORw: require("../assets/对话框.png"),
      imgUrl_TC_K: TrashCan_K,
      imgUrl_TC_O: TrashCan_O,
      imgUrl_TC_P: TrashCan_P,
      imgUrl_TC_R: TrashCan_R,
      n: 12,
      STO: 0,
      cnt: 0,
      cnt_ca: 0,
      SpecialTurn: [0, 0, 0, 0, 0],
      order: [0, 1, 2, 3, 4],
    };
  },
  watch: {
     'point': function(newVal,oldVal){
        const that = this;
        that.fontColor = newVal > oldVal? 'green':'red';
        setTimeout(function(){
           that.fontColor = 'white';
        },200)
     }
  },
  methods: {
    allReload() {
      var cnt = 0;
      if (this.cnt_clearall > 0) {
        for (cnt = 0; cnt < 5; cnt++) {
          this.m[cnt] = Math.random();
          this.m[cnt] = Math.ceil(this.m[cnt] * this.n);

          switch (this.m[cnt]) {
            case 1:
              this.imgUrl[cnt] = require("../assets/" + "paper.png");
              break;
            case 2:
              this.imgUrl[cnt] = require("../assets/smoke.png");
              break;
            case 3:
              this.imgUrl[cnt] = require("../assets/battery.png");
              break;
            case 4:
              this.imgUrl[cnt] = require("../assets/fishbone.png");
              break;
            case 5:
              this.imgUrl[cnt] = require("../assets/can.png");
              break;
            case 6:
              this.imgUrl[cnt] = require("../assets/卫生纸.png");
              break;
            case 7:
              this.imgUrl[
                cnt
              ] = require("../assets/毒药,毒物,有毒药物,poison.png");
              break;
            case 8:
              this.imgUrl[cnt] = require("../assets/骨头.png");
              break;
            case 9:
              this.imgUrl[cnt] = require("../assets/皮鞋.png");
              break;
            case 10:
              this.imgUrl[cnt] = require("../assets/纸杯.png");
              break;
            case 11:
              this.imgUrl[cnt] = require("../assets/有害垃圾-废弃温度计.png");
              break;
            case 12:
              this.imgUrl[cnt] = require("../assets/杀虫剂领用.png");
              break;
          }
        }
        this.cnt_clearall--;
        this.point += 5 * this.eachpoint;
        let clear = document.getElementById("clear");
        clear.play();
      } else {
        let addtime = document.getElementById("audioW");
        addtime.play();
      }
    },
    PositionCT() {
      if ((this.cnt - 2) % 6 === 0) {
        this.Count_turn = 1;
      } else {
        this.Count_turn = 0;
      }
    },
    PositionCA() {
      if ((this.cnt_ca - 5) % 8 === 0) {
        this.Clear_turn = 1;
      } else {
        this.Clear_turn = 0;
      }
    },
    addtime() {
      if (this.cnt_addtime > 0) {
        this.$refs.CountT.addTimeAmount();
        this.cnt_addtime -= 1;
        let addtimetool = document.getElementById("addtimetool");
        addtimetool.play();
        //提示音为添加
      } else {
        let addtime = document.getElementById("audioW");
        addtime.play();
      }
    },
    TouchVideoA() {
      let audioA = document.getElementById("audioA");
      audioA.play();
    },
    TouchVideoB() {
      let audioB = document.getElementById("audioB");
      audioB.play();
    },
    TouchVideoC() {
      let audioC = document.getElementById("audioC");
      audioC.play();
    },
    TouchVideoD() {
      let audioD = document.getElementById("audioD");
      audioD.play();
    },
    TouchVideoE() {
      let audioE = document.getElementById("audioE");
      audioE.play();
    },
    PointGetVideo() {
      let PGaudio = document.getElementById("PGaudio");
      PGaudio.play();
    },
    audioAutoPlay() {
      let audio = document.getElementById("audio");
      audio.play();
    },
    Oncall() {
      console.log("i'm Oncall");
    },
    ChangingA() {
      this.SpecialTurn[0] = 1;
      setInterval(() => {
        if (this.SpecialTurn[0] === 1) {
          switch (this.STO) {
            case 0:
              this.omoA -= 0.001;
              if (this.omoA <= 0.3) {
                this.STO = 1;
              }
              break; //还未解决在各类定位函数里的值重置this.opacity，以及对this.scale的switch构写
            default:
              this.omoA += 0.001;
              if (this.omoA >= 1) {
                this.STO = 0;
              }
              break;
          }
        }
      }, 10);
    },
    ChangingB() {
      this.SpecialTurn[1] = 1;
      setInterval(() => {
        if (this.SpecialTurn[1] === 1) {
          switch (this.STO) {
            case 0:
              this.omoB -= 0.001;
              if (this.omoB <= 0.3) {
                this.STO = 1;
              }
              break; //还未解决在各类定位函数里的值重置this.omoB，以及对this.scale的switch构写
            default:
              this.omoB += 0.001;
              if (this.omoB >= 1) {
                this.STO = 0;
              }
              break;
          }
        }
      }, 10);
    },
    ChangingC() {
      this.SpecialTurn[2] = 1;
      setInterval(() => {
        if (this.SpecialTurn[2] === 1) {
          switch (this.STO) {
            case 0:
              this.omoC -= 0.001;
              if (this.omoC <= 0.3) {
                this.STO = 1;
              }
              break; //还未解决在各类定位函数里的值重置this.omoC，以及对this.scale的switch构写
            default:
              this.omoC += 0.001;
              if (this.omoC >= 1) {
                this.STO = 0;
              }
              break;
          }
        }
      }, 10);
    },
    ChangingD() {
      this.SpecialTurn[3] = 1;
      setInterval(() => {
        if (this.SpecialTurn[3] === 1) {
          switch (this.STO) {
            case 0:
              this.omoD -= 0.001;
              if (this.omoD <= 0.3) {
                this.STO = 1;
              }
              break; //还未解决在各类定位函数里的值重置this.omoD，以及对this.scale的switch构写
            default:
              this.omoD += 0.001;
              if (this.omoD >= 1) {
                this.STO = 0;
              }
              break;
          }
        }
      }, 10);
    },
    ChangingE() {
      this.SpecialTurn[4] = 1;
      setInterval(() => {
        if (this.SpecialTurn[4] === 1) {
          switch (this.STO) {
            case 0:
              this.omoE -= 0.001;
              if (this.omoE <= 0.3) {
                this.STO = 1;
              }
              break; //还未解决在各类定位函数里的值重置this.omoE，以及对this.scale的switch构写
            default:
              this.omoE += 0.001;
              if (this.omoE >= 1) {
                this.STO = 0;
              }
              break;
          }
        }
      }, 10);
    },
    ChangingT() {
      this.omoT = 1;
      let audioT = document.getElementById("audioT");
      audioT.play();
      this.cnt_addtime++;
      this.Count_turn = 0;
    },
    ChangingClear() {
      let cleartool = document.getElementById("cleartool");
      cleartool.play();
      this.cnt_clearall++;
      this.Clear_turn = 0;
    },
    rORwOn(turn) {
      if (turn !== 4) {
        this.turn[0] = 0;
        this.turn[1] = 0;
        this.turn[2] = 0;
        this.turn[3] = 0;
        this.turn[turn] = 1;
      }
    },
    rORwOff() {
      this.turn[0] = 0;
      this.turn[1] = 0;
      this.turn[2] = 0;
      this.turn[3] = 0;
    },
    BacktoriginA(turn) {
      this.omoA = 1;
      this.SpecialTurn[0] = 0;
      this.rORwOn(turn);
      this.$refs.apple.top = this.Origin_top[0];
      this.$refs.apple.right = this.Origin_left[0];
      this.$refs.apple.left = 1120 - this.$refs.apple.right;
      console.log(this.$refs.apple.top);
      console.log(this.$refs.apple.left);
      let audioW = document.getElementById("audioW");
      audioW.play();
    },
    BacktoriginB(turn) {
      this.omoB = 1;
      this.SpecialTurn[1] = 0;
      this.rORwOn(turn);
      this.$refs.banana.top = this.Origin_top[1];
      this.$refs.banana.left = this.Origin_left[1];
      this.$refs.banana.right = 1120 - this.$refs.banana.left;
      let audioW = document.getElementById("audioW");
      audioW.play();
    },
    BacktoriginC(turn) {
      this.rORwOn(turn);
      this.$refs.cherry.top = this.Origin_top[2];
      this.$refs.cherry.left = this.Origin_left[2];
      this.$refs.cherry.right = 1120 - this.$refs.cherry.left;
      this.SpecialTurn[2] = 0;
      this.omoC = 1;
      let audioW = document.getElementById("audioW");
      audioW.play();
    },
    BacktoriginD(turn) {
      this.rORwOn(turn);
      this.$refs.date.top = this.Origin_top[3];
      this.$refs.date.left = this.Origin_left[3];
      this.$refs.date.right = 1120 - this.$refs.date.left;
      this.SpecialTurn[3] = 0;
      this.omoD = 1;
      let audioW = document.getElementById("audioW");
      audioW.play();
    },
    BacktoriginE(turn) {
      this.rORwOn(turn);
      this.$refs.egg.top = this.Origin_top[4];
      this.$refs.egg.left = this.Origin_left[4];
      this.$refs.egg.right = 1120 - this.$refs.egg.left;
      this.omoE = 1;
      this.SpecialTurn[4] = 0;
      let audioW = document.getElementById("audioW");
      audioW.play();
    },
    onActivatedA(order) {
      console.log(order);
      if (this.$refs.apple.top < 300 || this.$refs.apple.left < 163) {
        this.BacktoriginA(4);
      } else {
        switch (this.m[order] % 4) {
          case 1:
            if (this.$refs.apple.left >= 195 && this.$refs.apple.left <= 311) {
              this.turn[0] = 0;
              this.turn[1] = 0;
              this.turn[2] = 0;
              this.turn[3] = 0;

              this.PositionCreatedA(order);
            } else {
              this.BacktoriginA(1);
            }
            break;
          case 2:
            if (this.$refs.apple.left >= 898 && this.$refs.apple.left <= 1004) {
              this.turn[0] = 0;
              this.turn[1] = 0;
              this.turn[2] = 0;
              this.turn[3] = 0;

              this.PositionCreatedA(order);
            } else {
              this.BacktoriginA(2);
            }
            break;
          case 3:
            if (this.$refs.apple.left >= 678 && this.$refs.apple.left <= 781) {
              this.turn[0] = 0;
              this.turn[1] = 0;
              this.turn[2] = 0;
              this.turn[3] = 0;

              this.PositionCreatedA(order);
            } else {
              this.BacktoriginA(3);
            }
            break;
          case 0:
            if (this.$refs.apple.left >= 444 && this.$refs.apple.left <= 554) {
              this.turn[0] = 0;
              this.turn[1] = 0;
              this.turn[2] = 0;
              this.turn[3] = 0;

              this.PositionCreatedA(order);
            } else {
              this.BacktoriginA(0);
            }
            break;
        }
      }
      this.$forceUpdate();
    },
    onActivatedB(order) {
      console.log(order);
      if (this.$refs.banana.top < 300 || this.$refs.banana.left < 163) {
        this.BacktoriginB(4);
      } else {
        switch (this.m[order] % 4) {
          case 1:
            if (
              this.$refs.banana.left >= 195 &&
              this.$refs.banana.left <= 311
            ) {
              this.PositionCreatedB(order);
            } else {
              this.BacktoriginB(1);
            }
            break;
          case 2:
            if (
              this.$refs.banana.left >= 898 &&
              this.$refs.banana.left <= 1004
            ) {
              this.PositionCreatedB(order);
            } else {
              this.BacktoriginB(2);
            }
            break;
          case 3:
            if (
              this.$refs.banana.left >= 678 &&
              this.$refs.banana.left <= 781
            ) {
              this.PositionCreatedB(order);
            } else {
              this.BacktoriginB(3);
            }
            break;
          case 0:
            if (
              this.$refs.banana.left >= 444 &&
              this.$refs.banana.left <= 554
            ) {
              this.PositionCreatedB(order);
            } else {
              this.BacktoriginB(0);
            }
            break;
        }
      }
      this.$forceUpdate();
    },
    onActivatedC(order) {
      console.log(order);
      if (this.$refs.cherry.top < 300 || this.$refs.cherry.left < 163) {
        this.BacktoriginC(4);
      } else {
        switch (this.m[order] % 4) {
          case 1:
            if (
              this.$refs.cherry.left >= 195 &&
              this.$refs.cherry.left <= 311
            ) {
              this.PositionCreatedC(order);
            } else {
              this.BacktoriginC(1);
            }
            break;
          case 2:
            if (
              this.$refs.cherry.left >= 898 &&
              this.$refs.cherry.left <= 1004
            ) {
              this.PositionCreatedC(order);
            } else {
              this.BacktoriginC(2);
            }
            break;
          case 3:
            if (
              this.$refs.cherry.left >= 678 &&
              this.$refs.cherry.left <= 781
            ) {
              this.PositionCreatedC(order);
            } else {
              this.BacktoriginC(3);
            }
            break;
          case 0:
            if (
              this.$refs.cherry.left >= 444 &&
              this.$refs.cherry.left <= 554
            ) {
              this.PositionCreatedC(order);
            } else {
              this.BacktoriginC(0);
            }
            break;
        }
      }
      this.$forceUpdate();
    },
    onActivatedD(order) {
      console.log(order);
      if (this.$refs.date.top < 300 || this.$refs.date.left < 163) {
        this.BacktoriginD(4);
      } else {
        switch (this.m[order] % 4) {
          case 1:
            if (this.$refs.date.left >= 195 && this.$refs.date.left <= 311) {
              this.PositionCreatedD(order);
            } else {
              this.BacktoriginD(1);
            }
            break;
          case 2:
            if (this.$refs.date.left >= 898 && this.$refs.date.left <= 1004) {
              this.PositionCreatedD(order);
            } else {
              this.BacktoriginD(2);
            }
            break;
          case 3:
            if (this.$refs.date.left >= 678 && this.$refs.date.left <= 781) {
              this.PositionCreatedD(order);
            } else {
              this.BacktoriginD(3);
            }
            break;
          case 0:
            if (this.$refs.date.left >= 444 && this.$refs.date.left <= 554) {
              this.PositionCreatedD(order);
            } else {
              this.BacktoriginD(0);
            }
            break;
        }
      }
      this.$forceUpdate();
    },
    onActivatedE(order) {
      console.log(order);
      if (this.$refs.egg.top < 300 || this.$refs.egg.left < 163) {
        this.BacktoriginE(4);
      } else {
        switch (this.m[order] % 4) {
          case 1:
            if (this.$refs.egg.left >= 195 && this.$refs.egg.left <= 311) {
              this.PositionCreatedE(order);
            } else {
              this.BacktoriginE(1);
            }
            break;
          case 2:
            if (this.$refs.egg.left >= 898 && this.$refs.egg.left <= 1004) {
              this.PositionCreatedE(order);
            } else {
              this.BacktoriginE(2);
            }
            break;
          case 3:
            if (this.$refs.egg.left >= 678 && this.$refs.egg.left <= 781) {
              this.PositionCreatedE(order);
            } else {
              this.BacktoriginE(3);
            }
            break;
          case 0:
            if (this.$refs.egg.left >= 444 && this.$refs.egg.left <= 554) {
              this.PositionCreatedE(order);
            } else {
              this.BacktoriginE(0);
            }
            break;
        }
      }
      this.$forceUpdate();
    },
    PositionCreatedA(order) {
      this.cnt += 1;
      this.cnt_ca += 1;
      this.PointGetVideo();
      this.rORwOff();
      this.point += this.eachpoint;
      this.STO = 0;
      this.SpecialTurn[0] = 0;
      this.omoA = 1;
      do {
        this.Origin_top[order] = Math.random();
        this.Origin_top[order] = Math.ceil(this.Origin_top[0] * 400);
      } while (this.Origin_top[order] >= 250);

      do {
        this.Origin_left[order] = Math.random();
        this.Origin_left[order] = Math.ceil(
          this.Origin_left[0] * 500 + 200 * Math.random()
        );
      } while (this.Origin_left[order] <= 163);

      //a
      this.$refs.apple.top = this.Origin_top[order];
      this.$refs.apple.right = this.Origin_left[order];
      this.$refs.apple.left = 1120 - this.$refs.apple.right;
      this.m[order] = Math.random();
      this.m[order] = Math.ceil(this.m[order] * this.n);
      switch (this.m[order]) {
        case 1:
          this.imgUrl[0] = require("../assets/paper.png");
          break;
        case 2:
          this.imgUrl[0] = require("../assets/smoke.png");
          break;
        case 3:
          this.imgUrl[0] = require("../assets/battery.png");
          break;
        case 4:
          this.imgUrl[0] = require("../assets/fishbone.png");
          break;
        case 5:
          this.imgUrl[0] = require("../assets/can.png");
          break;
        case 6:
          this.imgUrl[0] = require("../assets/卫生纸.png");
          break;
        case 7:
          this.imgUrl[0] = require("../assets/毒药,毒物,有毒药物,poison.png");
          break;
        case 8:
          this.imgUrl[0] = require("../assets/骨头.png");
          break;
        case 9:
          this.imgUrl[0] = require("../assets/皮鞋.png");
          break;
        case 10:
          this.imgUrl[0] = require("../assets/纸杯.png");
          break;
        case 11:
          this.imgUrl[0] = require("../assets/有害垃圾-废弃温度计.png");
          break;
        case 12:
          this.imgUrl[0] = require("../assets/杀虫剂领用.png");
          break;
      }
      this.PositionCT();
      this.PositionCA();
    },
    PositionCreatedB(order) {
      this.cnt += 1;
      this.cnt_ca += 1;
      this.PointGetVideo();
      this.rORwOff();
      this.point += this.eachpoint;
      this.STO = 0;
      this.SpecialTurn[1] = 0;
      this.omoB = 1;
      do {
        this.Origin_top[order] = Math.random();
        this.Origin_top[order] = Math.ceil(this.Origin_top[1] * 50);
      } while (this.Origin_top[order] >= 250);
      do {
        this.Origin_left[order] = Math.random();
        this.Origin_left[order] = Math.ceil(
          this.Origin_left[1] * 200 + 460 * Math.random() + 300 * Math.random()
        );
      } while (this.Origin_left[order] <= 163);
      this.$refs.banana.top = this.Origin_top[order];
      this.$refs.banana.left = this.Origin_left[order];
      this.$refs.banana.right = 1120 - this.$refs.banana.right;
      this.m[order] = Math.random();
      this.m[order] = Math.ceil(this.m[order] * this.n);
      switch (this.m[order]) {
        case 1:
          this.imgUrl[1] = require("../assets/paper.png");
          break;
        case 2:
          this.imgUrl[1] = require("../assets/smoke.png");
          break;
        case 3:
          this.imgUrl[1] = require("../assets/battery.png");
          break;
        case 4:
          this.imgUrl[1] = require("../assets/fishbone.png");
          break;
        case 5:
          this.imgUrl[1] = require("../assets/can.png");
          break;
        case 6:
          this.imgUrl[1] = require("../assets/卫生纸.png");
          break;
        case 7:
          this.imgUrl[1] = require("../assets/毒药,毒物,有毒药物,poison.png");
          break;
        case 8:
          this.imgUrl[1] = require("../assets/骨头.png");
          break;
        case 9:
          this.imgUrl[1] = require("../assets/皮鞋.png");
          break;
        case 10:
          this.imgUrl[1] = require("../assets/纸杯.png");
          break;
        case 11:
          this.imgUrl[1] = require("../assets/有害垃圾-废弃温度计.png");
          break;
        case 12:
          this.imgUrl[1] = require("../assets/杀虫剂领用.png");
          break;
      }
      this.PositionCT();
      this.PositionCA();
    },
    PositionCreatedC(order) {
      this.cnt += 1;
      this.cnt_ca += 1;
      this.PointGetVideo();
      this.point += this.eachpoint;
      this.rORwOff();
      this.STO = 0;
      this.SpecialTurn[2] = 0;
      this.omoC = 1;
      do {
        this.Origin_top[order] = Math.random();
        this.Origin_top[order] = Math.ceil(this.Origin_top[2] * 200);
      } while (this.Origin_top[order] >= 250);
      do {
        this.Origin_left[order] = Math.random();
        this.Origin_left[order] = Math.ceil(this.Origin_left[2] * 200 + 80);
      } while (this.Origin_left[order] <= 163);
      this.$refs.cherry.top = this.Origin_top[order];
      this.$refs.cherry.left = this.Origin_left[order];
      this.$refs.cherry.right = 1120 - this.$refs.cherry.left;
      this.m[order] = Math.random();
      this.m[order] = Math.ceil(this.m[order] * this.n);
      switch (this.m[order]) {
        case 1:
          this.imgUrl[2] = require("../assets/paper.png");
          break;
        case 2:
          this.imgUrl[2] = require("../assets/smoke.png");
          break;
        case 3:
          this.imgUrl[2] = require("../assets/battery.png");
          break;
        case 4:
          this.imgUrl[2] = require("../assets/fishbone.png");
          break;
        case 5:
          this.imgUrl[2] = require("../assets/can.png");
          break;
        case 6:
          this.imgUrl[2] = require("../assets/卫生纸.png");
          break;
        case 7:
          this.imgUrl[2] = require("../assets/毒药,毒物,有毒药物,poison.png");
          break;
        case 8:
          this.imgUrl[2] = require("../assets/骨头.png");
          break;
        case 9:
          this.imgUrl[2] = require("../assets/皮鞋.png");
          break;
        case 10:
          this.imgUrl[2] = require("../assets/纸杯.png");
          break;
        case 11:
          this.imgUrl[2] = require("../assets/有害垃圾-废弃温度计.png");
          break;
        case 12:
          this.imgUrl[2] = require("../assets/杀虫剂领用.png");
          break;
      }
      this.PositionCT();
      this.PositionCA();
    },

    PositionCreatedD(order) {
      this.cnt += 1;
      this.cnt_ca += 1;
      this.PointGetVideo();
      this.point += this.eachpoint;
      this.rORwOff();
      this.STO = 0;
      this.SpecialTurn[3] = 0;
      this.omoD = 1;
      do {
        this.Origin_top[order] = Math.random();
        this.Origin_top[order] = Math.ceil(this.Origin_top[3] * 2 - 50);
      } while (this.Origin_left[order] <= 163);
      do {
        this.Origin_left[order] = Math.random();
        this.Origin_left[order] = Math.ceil(this.Origin_left[3] * 440 + 300);
      } while (this.Origin_left[order] <= 163);
      this.$refs.date.top = this.Origin_top[order];
      this.$refs.date.left = this.Origin_left[order];
      this.$refs.date.right = 1120 - this.$refs.date.left;
      this.m[order] = Math.random();
      this.m[order] = Math.ceil(this.m[order] * this.n);
      switch (this.m[order]) {
        case 1:
          this.imgUrl[3] = require("../assets/paper.png");
          break;
        case 2:
          this.imgUrl[3] = require("../assets/smoke.png");
          break;
        case 3:
          this.imgUrl[3] = require("../assets/battery.png");
          break;
        case 4:
          this.imgUrl[3] = require("../assets/fishbone.png");
          break;
        case 5:
          this.imgUrl[3] = require("../assets/can.png");
          break;
        case 6:
          this.imgUrl[3] = require("../assets/卫生纸.png");
          break;
        case 7:
          this.imgUrl[3] = require("../assets/毒药,毒物,有毒药物,poison.png");
          break;
        case 8:
          this.imgUrl[3] = require("../assets/骨头.png");
          break;
        case 9:
          this.imgUrl[3] = require("../assets/皮鞋.png");
          break;
        case 10:
          this.imgUrl[3] = require("../assets/纸杯.png");
          break;
        case 11:
          this.imgUrl[3] = require("../assets/有害垃圾-废弃温度计.png");
          break;
        case 12:
          this.imgUrl[3] = require("../assets/杀虫剂领用.png");
          break;
      }
      this.PositionCT();
      this.PositionCA();
    },
    PositionCreatedE(order) {
      this.cnt += 1;
      this.cnt_ca += 1;
      this.PointGetVideo();
      this.point += this.eachpoint;
      this.rORwOff();
      this.STO = 0;
      this.SpecialTurn[4] = 0;
      this.omoE = 1;
      do {
        this.Origin_top[order] = Math.random();
        this.Origin_top[order] = Math.ceil(this.Origin_top[4] * 150);
      } while (this.Origin_top[order] >= 250);
      do {
        this.Origin_left[order] = Math.random();
        this.Origin_left[order] = Math.ceil(this.Origin_left[4] * 150 + 140);
      } while (this.Origin_left[order] <= 163);
      this.$refs.egg.top = this.Origin_top[order];
      this.$refs.egg.left = this.Origin_left[order];
      this.$refs.egg.right = 1120 - this.$refs.egg.left;
      this.m[order] = Math.random();
      this.m[order] = Math.ceil(this.m[order] * this.n);
      switch (this.m[order]) {
        case 1:
          this.imgUrl[4] = require("../assets/paper.png");
          break;
        case 2:
          this.imgUrl[4] = require("../assets/smoke.png");
          break;
        case 3:
          this.imgUrl[4] = require("../assets/battery.png");
          break;
        case 4:
          this.imgUrl[4] = require("../assets/fishbone.png");
          break;
        case 5:
          this.imgUrl[4] = require("../assets/can.png");
          break;
        case 6:
          this.imgUrl[4] = require("../assets/卫生纸.png");
          break;
        case 7:
          this.imgUrl[4] = require("../assets/毒药,毒物,有毒药物,poison.png");
          break;
        case 8:
          this.imgUrl[4] = require("../assets/骨头.png");
          break;
        case 9:
          this.imgUrl[4] = require("../assets/皮鞋.png");
          break;
        case 10:
          this.imgUrl[4] = require("../assets/纸杯.png");
          break;
        case 11:
          this.imgUrl[4] = require("../assets/有害垃圾-废弃温度计.png");
          break;
        case 12:
          this.imgUrl[4] = require("../assets/杀虫剂领用.png");
          break;
      }
      this.PositionCT();
      this.PositionCA();
    },
  },
  beforeMount() {
    var cnt = 0;
    for (cnt = 0; cnt < 5; cnt++) {
      this.m[cnt] = Math.random();
      this.m[cnt] = Math.ceil(this.m[cnt] * this.n);

      switch (this.m[cnt]) {
        case 1:
          this.imgUrl[cnt] = require("../assets/" + "paper.png");
          break;
        case 2:
          this.imgUrl[cnt] = require("../assets/smoke.png");
          break;
        case 3:
          this.imgUrl[cnt] = require("../assets/battery.png");
          break;
        case 4:
          this.imgUrl[cnt] = require("../assets/fishbone.png");
          break;
        case 5:
          this.imgUrl[cnt] = require("../assets/can.png");
          break;
        case 6:
          this.imgUrl[cnt] = require("../assets/卫生纸.png");
          break;
        case 7:
          this.imgUrl[cnt] = require("../assets/毒药,毒物,有毒药物,poison.png");
          break;
        case 8:
          this.imgUrl[cnt] = require("../assets/骨头.png");
          break;
        case 9:
          this.imgUrl[cnt] = require("../assets/皮鞋.png");
          break;
        case 10:
          this.imgUrl[cnt] = require("../assets/纸杯.png");
          break;
        case 11:
          this.imgUrl[cnt] = require("../assets/有害垃圾-废弃温度计.png");
          break;
        case 12:
          this.imgUrl[cnt] = require("../assets/杀虫剂领用.png");
          break;
      }
    }
  },
  mounted() {
    var turn = 0;
    this.$refs.apple.top = this.Origin_top[0];
    this.$refs.apple.right = this.Origin_left[0];
    this.$refs.apple.left = 1120 - this.$refs.apple.right;
    console.log(this.$refs.apple.top);
    console.log(this.$refs.apple.left);
    //b
    this.$refs.banana.top = this.Origin_top[1];
    this.$refs.banana.left = this.Origin_left[1];
    this.$refs.banana.right = 1120 - this.$refs.banana.left;

    this.$refs.cherry.top = this.Origin_top[2];
    this.$refs.cherry.left = this.Origin_left[2];
    this.$refs.cherry.right = 1120 - this.$refs.cherry.left;

    this.$refs.date.top = this.Origin_top[3];
    this.$refs.date.left = this.Origin_left[3];
    this.$refs.date.right = 1120 - this.$refs.date.left;

    this.$refs.egg.top = this.Origin_top[4];
    this.$refs.egg.left = this.Origin_left[4];
    this.$refs.egg.right = 1120 - this.$refs.egg.left;
    console.log(this.$refs.CountT.left);
    setInterval(() => {
      if (this.$refs.CountT.left === 0 && turn === 0) {
        let success = document.getElementById("success");
        success.play();
        alert("已经结束哩");
        turn = 1;
      }
    }, 300);
    document.addEventListener("mousemove", this.audioAutoPlay, false);
    let ev = new Event("mousemove");
    document.dispatchEvent(ev);
    let oAudio = document.querySelector("#audio");
    oAudio.onended = function () {
      //播放完毕，重新循环播放
      oAudio.load();
      oAudio.play();
    };
  },
};
</script>
<style type="text/css">
body {
   position: relative;
  background: no-repeat;
  overflow: hidden;
}
.tools {
  position: absolute;
  background-color: rgb(254, 245, 230);
  width: 86px;
  top: 20vh;
}
.tools > div {
  height: 80px;
  width: 80px;
  border: 3px solid orange;
  border-bottom: 0;
}
.tools > div:hover {
  cursor: pointer;
}
.tools div:nth-last-child(1) {
  border-bottom: 3px solid orange;
}
.tools img {
  height: 80px;
  width: 80px;
  position: absolute;
}
.tools div:nth-child(1) img {
  top: 3px;
  left: 3px;
}
.scorepad {
  position: relative;
  width: 250px;
  height: 130px;
  margin: 0 auto;
}
.scorepad > img {
   position: absolute;
   height: 130px;
   width: 250px;
}
.pointnum {
   position: absolute;
   font-size: 40px;
   font-weight: bold;
   width: 250px;
   top: 13px;
   text-align: center;
}
.box {
  margin-top: 50px;
  line-height: 40px;
  width: 210px;
  height: 550px;
  padding: 2px 2px 2px 2px;
  border: 1px solid #797979;
  background-color: #facd91;
  box-sizing: border-box;
  box-shadow: 8px 8px 16px 0px rgba(175, 80, 80, 0.35);
}
.addtimenum {
  position: absolute;
  top: 2px;
  left: 3px;
  margin-bottom: 80px;
  font-size: 20px;
  font-weight: bold;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-style: italic;
  color: rgba(227, 51, 233, 0.664);
}
.clearallnum {
  font-size: 20px;
  font-weight: bold;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-style: italic;
  color: rgba(227, 51, 233, 0.664);
}
.clearall {
  top: 200px;
  left: 900px;
  z-index: 4;
}
.timeadd {
  top: 0px;
  left: 300px;
  z-index: 4;
}
.CT {
  float: left;
  top: 20px;
}
.Picture {
  transform: scale(0.4);
  position: absolute;
}
.Picture:hover {
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  transition-duration: 1s;
  transition-property: transform, scale;
  transform: scale(0.5);
  z-index: 2;
}
.demo.active::before {
  display: none;
}
.TrashCan_K {
  transform: scale(0.8);
  background: rgba(255, 255, 255, 0.3);
  top: 395px;
  left: 500px;
  border-radius: 50px;
  position: absolute;
}
/*.TrashCan_K:hover{
  transform: scale(0.8);
  top:395px;
  left: 250px;
  background: rgba(255,255,255,0.7);
  border-radius: 10%;
  
  position: absolute;
}*/
.TrashCan_O {
  transform: scale(0.8);
  background: rgba(255, 255, 255, 0.3);
  top: 395px;
  left: 950px;
  border-radius: 50px;
  position: absolute;
}
/*.TrashCan_O:hover{
  transform: scale(0.8);
  top:395px;
  left: 250px;
  background: rgba(255,255,255,0.7);
  border-radius: 10%;
  
  position: absolute;
}*/
.TrashCan_R {
  transform: scale(0.8);
  top: 395px;
  left: 250px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 50px;
  position: absolute;
}
/*.TrashCan_R:hover{
  transform: scale(0.8);
  top:395px;
  left: 250px;
  background: rgba(255,255,255,0.7);
  border-radius: 10%;
  
  position: absolute;
}*/
.TrashCan_P {
  transform: scale(0.8);
  top: 395px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 50px;
  left: 730px;
  position: absolute;
}
/*.TrashCan_P:hover{
  transform: scale(0.8);
  top:395px;
  left: 250px;
  background: rgba(255,255,255,0.7);
  position: absolute;
}*/
.rORwOne {
  transform: scale(0.17);
  left: -40px;
  top: 100px;
  position: absolute;
}
.rORwTwo {
  transform: scale(0.17);

  left: 200px;
  top: 100px;
  position: absolute;
}
.rORwThree {
  transform: scale(0.17);
  left: 440px;
  top: 100px;
  position: absolute;
}
.rORwFour {
  transform: scale(0.17);
  left: 680px;
  top: 100px;
  position: absolute;
}
</style>