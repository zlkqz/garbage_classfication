<template>
<div>
  <tempComponent class="GG" v-if="GG_turn"></tempComponent>
  <div id="DragExample" v-if="GG_off">
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
      :key="keyA"
      :isResizable="false"
      ref="apple"
      ><img
        :style="{ opacity: omoA,left:ZuoA+'vw',top:GaoA+'vh',right:YouA+'vw' }"
        @mouseenter="TouchVideoA()"
        :src="imgUrl[0]"
        class="Picture"
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
      :key="keyB"
      :isResizable="false"
      ref="banana"
      ><img
        @mouseenter="TouchVideoB()"
        :src="imgUrl[1]"
        class="Picture"
        :style="{ opacity: omoB,top:GaoB+'vh',left:ZuoB+'vw',right:YouB+'vw' }" /><audio
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
      :key="keyC"
      :isResizable="false"
      ref="cherry"
      ><img
        @mouseenter="TouchVideoC()"
        :src="imgUrl[2]"
        class="Picture"
        :style="{ opacity: omoC,top:GaoC+'vh',left:ZuoC+'vw',right:YouC+'vw' }"
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
      :key="keyD"
      :isResizable="false"
      ref="date"
      ><img
        @mouseenter="TouchVideoD()"
        :src="imgUrl[3]"
        class="Picture"
        :style="{ opacity: omoD,top:GaoD+'vh',left:ZuoD+'vw',right:YouD+'vw'}"
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
      :key="keyE"
      :isResizable="false"
      ref="egg"
      ><img
        @mouseenter="TouchVideoE()"
        :src="imgUrl[4]"
        class="Picture"
        :style="{ opacity: omoE,top:GaoE+'vh',left:ZuoE+'vw',right:YouE+'vw' }" />
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
  </div>
  <audio
      id="success"
      :src="
        require('../assets/《天天来塔防》资源素材-Sounds-UI 的成功(UI_s_爱给网_aigei_com.mp3')
      "
    ></audio>
    <audio
      id="audio"
      :src="
        require('../assets/39辑 - AudioJungel精选合集-快乐的时光(Ha_爱给网_aigei_com.mp3')
      "
    ></audio>
  </div>
</template>

<script>
import CountTimer from "../components/CountTimer.vue";
import VueDragResize from "vue-drag-resize";
import tempComponent from "../components/tempComponent.vue"
import TrashCan_K from "../assets/垃圾分类-厨余n.png";
import TrashCan_O from "../assets/垃圾分类-其他n.png";
import TrashCan_P from "../assets/垃圾分类-有害n.png";
import TrashCan_R from "../assets/垃圾分类-可回收n.png";
export default {
  name: "DragE",
  components: {
    VueDragResize,
    CountTimer,
    tempComponent
  },
  data() {
    return {
      keyword: "",
      top:0,
      cnt_addtime: 0,
      keyA:3,
      keyB:50,
      keyC:90,
      keyD:120,
      keyE:170,
      GaoA:-5,
      GaoB:30,
      GaoC:35,
      GaoD:30,
      GaoE:0,
      ZuoA:20,
      ZuoB:10,
      ZuoC:40,
      ZuoD:55,
      ZuoE:75,
      NGaoA:0,
      NZuoA:0,
      NGaoB:0,
      NZuoB:0,
      NGaoC:0,
      NZuoC:0,
      NGaoD:0,
      NZuoD:0,
      NGaoE:0,
      NZuoE:0,
      YouA:0,
      YouB:0,
      YouC:0,
      YouD:0,
      YouE:0,
      cnt_clearall: 0,
      GG_turn:0,
      GG_off:1,
      point: 0,
      cnt_turn:1,
      eachpoint: 100,
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
      Origin_top: [10, 30, 40, 50, 45], //一开始对于每一个图片在其css中设置一个固定的位置，随后再通过随机的方法得到它的位置
      Origin_left: [30, 40, 80, 90, 65],
      imgUrl: [],
      imgUrl_rORw: require("../assets/对话框.png"),
      imgUrl_TC_K: TrashCan_K,
      imgUrl_TC_O: TrashCan_O,
      imgUrl_TC_P: TrashCan_P,
      imgUrl_TC_R: TrashCan_R,
      n: 41,
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

           this.cnt_turn=1;
      while(this.cnt_turn)
      {
      switch (this.m[cnt]) {
        case 1:
          this.imgUrl[cnt] = require("../assets/" + "paper.png");
          this.cnt_turn=0;
          break;
          case 5:
          this.imgUrl[cnt] = require("../assets/can.png");
          this.cnt_turn=0;
          break;
          case 9:
          this.imgUrl[cnt] = require("../assets/皮鞋.png");
          this.cnt_turn=0;
          break;
           case 13:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/可回收物-玻璃类.png");
          this.cnt_turn=0;break;
          case 17:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/插头.png");
          this.cnt_turn=0;break;
          case 21:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/旧衣服.png");
          this.cnt_turn=0;break;
          case 25:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/枕头.png");
          this.cnt_turn=0;break;
          case 29:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/酒瓶-啤酒-雪花.png");
          this.cnt_turn=0;break;
          case 33:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/砧板.png");
          this.cnt_turn=0;break;
          case 37:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/毛绒玩具.png");
          this.cnt_turn=0;break;
          case 41:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/衣架.png");
          this.cnt_turn=0;break;
        case 2:
          this.imgUrl[cnt] = require("../assets/smoke.png");
          this.cnt_turn=0;break;
          case 6:
          this.imgUrl[cnt] = require("../assets/卫生纸.png");
          this.cnt_turn=0;break;
           case 10:
          this.imgUrl[cnt] = require("../assets/纸杯.png");
          this.cnt_turn=0;break;
          case 14:
          this.imgUrl[cnt] = require("../assets/6其他垃圾/筷子.png");
          this.cnt_turn=0;break;
          case 18:
          this.imgUrl[cnt] = require("../assets/6其他垃圾/贝壳.png");
          this.cnt_turn=0;break;
        case 3:
          this.imgUrl[cnt] = require("../assets/battery.png");
          this.cnt_turn=0;break;
        case 7:
          this.imgUrl[cnt] = require("../assets/毒药,毒物,有毒药物,poison.png");
          this.cnt_turn=0;break;
        case 11:
          this.imgUrl[cnt] = require("../assets/有害垃圾-废弃温度计.png");
          this.cnt_turn=0;break;
           case 15:
          this.imgUrl[cnt] = require("../assets/5有害垃圾/除草剂.png");
          this.cnt_turn=0;break;
           case 19:
          this.imgUrl[cnt] = require("../assets/5有害垃圾/有害垃圾-过期药品.png");
          this.cnt_turn=0;break;
           case 23:
          this.imgUrl[cnt] = require("../assets/5有害垃圾/电池.png");
          this.cnt_turn=0;break;
           case 4:
          this.imgUrl[cnt] = require("../assets/fishbone.png");
          this.cnt_turn=0;break;
          case 8:
          this.imgUrl[cnt] = require("../assets/骨头.png");
          this.cnt_turn=0;break;
        case 12:
          this.imgUrl[cnt] = require("../assets/4厨余垃圾/厨余垃圾-果壳.png");
          this.cnt_turn=0;break;
          case 16:
          this.imgUrl[cnt] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 20:
          this.imgUrl[cnt] = require("../assets/4厨余垃圾/披萨.png");
          this.cnt_turn=0;break;
           case 24:
          this.imgUrl[cnt] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 28:
          this.imgUrl[cnt] = require("../assets/4厨余垃圾/菜.png");
          this.cnt_turn=0;break;
      }
       if(this.cnt_turn)
      {
        this.m[cnt]-=20;
      }
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
              break;
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
     this.GaoA = this.Origin_top[0];
      this.ZuoA = this.Origin_left[0];
     this.YouA =100- this.ZuoA;
      let audioW = document.getElementById("audioW");
      audioW.play();
    },
    BacktoriginB(turn) {
      this.omoB = 1;
      this.SpecialTurn[1] = 0;
      this.rORwOn(turn);
       this.GaoB = this.Origin_top[1];
      this.ZuoB= this.Origin_left[1];
     this.YouB=100- this.ZuoB;
      let audioW = document.getElementById("audioW");
      audioW.play();
    },
    BacktoriginC(turn) {
      this.rORwOn(turn);
       this.GaoC = this.Origin_top[2];
      this.ZuoC = this.Origin_left[2];
     this.YouC =100- this.ZuoC;
      this.SpecialTurn[2] = 0;
      this.keyC+=1;
      this.omoC = 1;
      let audioW = document.getElementById("audioW");
      audioW.play();
    },
    BacktoriginD(turn) {
      this.rORwOn(turn);
       this.GaoD = this.Origin_top[3];
      this.ZuoD = this.Origin_left[3];
     this.YouD =100- this.ZuoD;
      this.SpecialTurn[3] = 0;
      this.omoD = 1;
      this.keyD+=1;
      let audioW = document.getElementById("audioW");
      audioW.play();
    },
    BacktoriginE(turn) {
      this.rORwOn(turn);
       this.GaoE = this.Origin_top[4];
      this.ZuoE = this.Origin_left[4];
     this.YouE=100- this.ZuoE;
      this.omoE = 1;
      this.SpecialTurn[4] = 0;
      let audioW = document.getElementById("audioW");
      audioW.play();
    },
    onActivatedA(order) {
      console.log(order);
       this.NGaoA=(this.$refs.apple.top*100/document.body.clientHeight)+this.GaoA;
       this.NZuoA=(this.$refs.apple.left*100/document.body.clientWidth)+this.ZuoA;
        this.keyA+=1;
       console.log(this.NGaoA);
        console.log(this.NZuoA);
      if (this.NGaoA <44|| this.NZuoA<3.5) {
        this.BacktoriginA(4);
      } else {
        switch (this.m[order] % 4) {
          case 1:
            if (this.NZuoA >3.5 && this.NZuoA <= 17.3) {
 this.Oncall();
              this.PositionCreatedA(order);
            } else {
              if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginA(1);
            }
            break;
          case 0:
            if (this.NZuoA >= 25.5 && this.NZuoA <= 40.6) {
           this.Oncall();
              this.PositionCreatedA(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginA(0);
            }
            break;
          case 3:
            if (this.NZuoA >= 49 && this.NZuoA <=64 ) {

              this.PositionCreatedA(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginA(3);
            }
            break;
          case 2:
            if (this.NZuoA >= 72.5 &&this.NZuoA <= 87.3) {

              this.PositionCreatedA(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginA(2);
            }
            break;
        }
      }
      this.$forceUpdate();
    },
    onActivatedB(order) {
      console.log(order);
       this.NGaoB=(this.$refs.banana.top*100/document.body.clientHeight)+this.GaoB;
       this.NZuoB=this.$refs.banana.left*100/document.body.clientWidth+this.ZuoB;
       this.keyB+=1;
      if (this.NGaoB < 44 || this.NZuoB <3.5 ) {
        this.BacktoriginB(4);
      } else {
        switch (this.m[order] % 4) {
          case 1:
            if (
             this.NZuoB >=3.5 &&
              this.NZuoB <= 17.3
            ) {
              this.PositionCreatedB(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginB(1);
            }
            break;
          case 0:
            if (
             this.NZuoB >= 25.5 &&
              this.NZuoB <= 40.6
            ) {
              this.PositionCreatedB(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginB(0);
            }
            break;
          case 3:
            if (
             this.NZuoB >=49 &&
              this.NZuoB <= 64
            ) {
              this.PositionCreatedB(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginB(3);
            }
            break;
          case 2:
            if (
             this.NZuoB >= 72.5 &&
              this.NZuoB<= 87.3
            ) {
              this.PositionCreatedB(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginB(2);
            }
            break;
        }
      }
      this.$forceUpdate();
    },
    onActivatedC(order) {
      console.log(order);
       this.NGaoC=(this.$refs.cherry.top*100/document.body.clientHeight)+this.GaoC;
       this.NZuoC=this.$refs.cherry.left*100/document.body.clientWidth+this.ZuoC;
      if (this.NGaoC < 44 || this.NZuoC< 3.5) {
        this.BacktoriginC(4);
      } else {
        switch (this.m[order] % 4) {
          case 1:
            if (
              this.NZuoC>= 3.5 &&
              this.NZuoC<= 17.3
            ) {
              this.PositionCreatedC(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginC(1);
            }
            break;
          case 0:
            if (
             this.NZuoC>= 25.5 &&
             this.NZuoC<= 40.6
            ) {
              this.PositionCreatedC(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginC(0);
            }
            break;
          case 3:
            if (
             this.NZuoC>= 49 &&
             this.NZuoC<= 64
            ) {
              this.PositionCreatedC(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginC(3);
            }
            break;
          case 2:
            if (
             this.NZuoC>= 72.5 &&
              this.NZuoC<= 87.3
            ) {
              this.PositionCreatedC(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginC(2);
            }
            break;
        }
      }
      this.$forceUpdate();
    },
    onActivatedD(order) {
      console.log(order);
       this.NGaoD=(this.$refs.date.top*100/document.body.clientHeight)+this.GaoD;
       this.NZuoD=this.$refs.date.left*100/document.body.clientWidth+this.ZuoD;
      if (this.NGaoD < 44 || this.NZuoD < 3.5) {
        this.BacktoriginD(4);
      } else {
        switch (this.m[order] % 4) {
          case 1:
            if (this.NZuoD >= 3.5 && this.NZuoD <= 17.3) {
              this.PositionCreatedD(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginD(1);
            }
            break;
          case 0:
            if (this.NZuoD >= 25.5 && this.NZuoD <= 40.6) {
              this.PositionCreatedD(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginD(0);
            }
            break;
          case 3:
            if (this.NZuoD >= 49 && this.NZuoD <= 64) {
              this.PositionCreatedD(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginD(3);
            }
            break;
          case 2:
            if (this.NZuoD >= 72.5 && this.NZuoD <= 87.3) {
              this.PositionCreatedD(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginD(2);
            }
            break;
        }
      }
      this.$forceUpdate();
    },
    onActivatedE(order) {
      console.log(order);
      this.NGaoE=(this.$refs.egg.top*100/document.body.clientHeight)+this.GaoE;
       this.NZuoE=this.$refs.egg.left*100/document.body.clientWidth+this.ZuoE;
       this.keyE+=1;
      if (this.NGaoE < 44 || this.NZuoE < 3.5) {
        this.BacktoriginE(4);
      } else {
        switch (this.m[order] % 4) {
          case 1:
            if (this.NZuoE >= 3.5 && this.NZuoE <= 17.3) {
              this.PositionCreatedE(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginE(1);
            }
            break;
          case 0:
            if (this.NZuoE >= 25.5 && this.NZuoE <= 40.6) {
              this.PositionCreatedE(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginE(0);
            }
            break;
          case 3:
            if (this.NZuoE >= 49 &&this.NZuoE <= 64) {
              this.PositionCreatedE(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginE(3);
            }
            break;
          case 2:
            if (this.NZuoE >=72.5  &&this.NZuoE <= 87.3) {
              this.PositionCreatedE(order);
            } else {
               if(this.point<=70)
              {
                   this.point=0;
              }
              else{
                this.point-=70;
              }
              this.BacktoriginE(2);
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
        this.Origin_top[order] = Math.ceil(this.Origin_top[0] * 40);
      } while (this.Origin_top[order] <0);

      do {
        this.Origin_left[order] = Math.random();
        this.Origin_left[order] = Math.ceil(this.Origin_left[0] * 50 + 20 * Math.random());
      } while (this.Origin_left[order] <= 10);

      //a
      this.GaoA = this.Origin_top[order];
      this.ZuoA = this.Origin_left[order];
      this.YouA=100-this.ZuoA;
      this.keyA+=1;
      this.m[order] = Math.random();
      this.m[order] = Math.ceil(this.m[order] * this.n);
     this.cnt_turn=1;
      while(this.cnt_turn)
      {
      switch (this.m[order]) {
        case 1:
          this.imgUrl[0] = require("../assets/" + "paper.png");
          this.cnt_turn=0;
          break;
          case 5:
          this.imgUrl[0] = require("../assets/can.png");
          this.cnt_turn=0;
          break;
          case 9:
          this.imgUrl[0] = require("../assets/皮鞋.png");
          this.cnt_turn=0;
          break;
           case 13:
          this.imgUrl[0] = require("../assets/3可回收垃圾/可回收物-玻璃类.png");
          this.cnt_turn=0;break;
          case 17:
          this.imgUrl[0] = require("../assets/3可回收垃圾/插头.png");
          this.cnt_turn=0;break;
          case 21:
          this.imgUrl[0] = require("../assets/3可回收垃圾/旧衣服.png");
          this.cnt_turn=0;break;
          case 25:
          this.imgUrl[0] = require("../assets/3可回收垃圾/枕头.png");
          this.cnt_turn=0;break;
          case 29:
          this.imgUrl[0] = require("../assets/3可回收垃圾/酒瓶-啤酒-雪花.png");
          this.cnt_turn=0;break;
          case 33:
          this.imgUrl[0] = require("../assets/3可回收垃圾/砧板.png");
          this.cnt_turn=0;break;
          case 37:
          this.imgUrl[0] = require("../assets/3可回收垃圾/毛绒玩具.png");
          this.cnt_turn=0;break;
          case 41:
          this.imgUrl[0] = require("../assets/3可回收垃圾/衣架.png");
          this.cnt_turn=0;break;
        case 2:
          this.imgUrl[0] = require("../assets/smoke.png");
          this.cnt_turn=0;break;
          case 6:
          this.imgUrl[0] = require("../assets/卫生纸.png");
          this.cnt_turn=0;break;
           case 10:
          this.imgUrl[0] = require("../assets/纸杯.png");
          this.cnt_turn=0;break;
          case 14:
          this.imgUrl[0] = require("../assets/6其他垃圾/筷子.png");
          this.cnt_turn=0;break;
          case 18:
          this.imgUrl[0] = require("../assets/6其他垃圾/贝壳.png");
          this.cnt_turn=0;break;
        case 3:
          this.imgUrl[0] = require("../assets/battery.png");
          this.cnt_turn=0;break;
        case 7:
          this.imgUrl[0] = require("../assets/毒药,毒物,有毒药物,poison.png");
          this.cnt_turn=0;break;
        case 11:
          this.imgUrl[0] = require("../assets/有害垃圾-废弃温度计.png");
          this.cnt_turn=0;break;
           case 15:
          this.imgUrl[0] = require("../assets/5有害垃圾/除草剂.png");
          this.cnt_turn=0;break;
           case 19:
          this.imgUrl[0] = require("../assets/5有害垃圾/有害垃圾-过期药品.png");
          this.cnt_turn=0;break;
           case 23:
          this.imgUrl[0] = require("../assets/5有害垃圾/电池.png");
          this.cnt_turn=0;break;
           case 4:
          this.imgUrl[0] = require("../assets/fishbone.png");
          this.cnt_turn=0;break;
          case 8:
          this.imgUrl[0] = require("../assets/骨头.png");
          this.cnt_turn=0;break;
        case 12:
          this.imgUrl[0] = require("../assets/4厨余垃圾/厨余垃圾-果壳.png");
          this.cnt_turn=0;break;
          case 16:
          this.imgUrl[0] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 20:
          this.imgUrl[0] = require("../assets/4厨余垃圾/披萨.png");
          this.cnt_turn=0;break;
           case 24:
          this.imgUrl[0] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 28:
          this.imgUrl[0] = require("../assets/4厨余垃圾/菜.png");
          this.cnt_turn=0;break;
      }
       if(this.cnt_turn)
      {
        this.m[order]-=20;
      }
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
        this.Origin_top[order] = Math.ceil(this.Origin_top[1] * 5+8);
      } while (this.Origin_top[order] >= 25);
      do {
        this.Origin_left[order] = Math.random();
        this.Origin_left[order] = Math.ceil(
          this.Origin_left[1] * 20 + 46 * Math.random() + 30 * Math.random()
        );
      } while (this.Origin_left[order] <= 10);
      this.GaoB = this.Origin_top[order];
      this.ZuoB = this.Origin_left[order];
      this.YouB=100-this.ZuoB;
      this.keyB+=1;
      this.m[order] = Math.random();
      this.m[order] = Math.ceil(this.m[order] * this.n);
     this.cnt_turn=1;
      while(this.cnt_turn)
      {
      switch (this.m[order]) {
        case 1:
          this.imgUrl[1] = require("../assets/" + "paper.png");
          this.cnt_turn=0;
          break;
          case 5:
          this.imgUrl[1] = require("../assets/can.png");
          this.cnt_turn=0;
          break;
          case 9:
          this.imgUrl[1] = require("../assets/皮鞋.png");
          this.cnt_turn=0;
          break;
           case 13:
          this.imgUrl[1] = require("../assets/3可回收垃圾/可回收物-玻璃类.png");
          this.cnt_turn=0;break;
          case 17:
          this.imgUrl[1] = require("../assets/3可回收垃圾/插头.png");
          this.cnt_turn=0;break;
          case 21:
          this.imgUrl[1] = require("../assets/3可回收垃圾/旧衣服.png");
          this.cnt_turn=0;break;
          case 25:
          this.imgUrl[1] = require("../assets/3可回收垃圾/枕头.png");
          this.cnt_turn=0;break;
          case 29:
          this.imgUrl[1] = require("../assets/3可回收垃圾/酒瓶-啤酒-雪花.png");
          this.cnt_turn=0;break;
          case 33:
          this.imgUrl[1] = require("../assets/3可回收垃圾/砧板.png");
          this.cnt_turn=0;break;
          case 37:
          this.imgUrl[1] = require("../assets/3可回收垃圾/毛绒玩具.png");
          this.cnt_turn=0;break;
          case 41:
          this.imgUrl[1] = require("../assets/3可回收垃圾/衣架.png");
          this.cnt_turn=0;break;
        case 2:
          this.imgUrl[1] = require("../assets/smoke.png");
          this.cnt_turn=0;break;
          case 6:
          this.imgUrl[1] = require("../assets/卫生纸.png");
          this.cnt_turn=0;break;
           case 10:
          this.imgUrl[1] = require("../assets/纸杯.png");
          this.cnt_turn=0;break;
          case 14:
          this.imgUrl[1] = require("../assets/6其他垃圾/筷子.png");
          this.cnt_turn=0;break;
          case 18:
          this.imgUrl[1] = require("../assets/6其他垃圾/贝壳.png");
          this.cnt_turn=0;break;
        case 3:
          this.imgUrl[1] = require("../assets/battery.png");
          this.cnt_turn=0;break;
        case 7:
          this.imgUrl[1] = require("../assets/毒药,毒物,有毒药物,poison.png");
          this.cnt_turn=0;break;
        case 11:
          this.imgUrl[1] = require("../assets/有害垃圾-废弃温度计.png");
          this.cnt_turn=0;break;
           case 15:
          this.imgUrl[1] = require("../assets/5有害垃圾/除草剂.png");
          this.cnt_turn=0;break;
           case 19:
          this.imgUrl[1] = require("../assets/5有害垃圾/有害垃圾-过期药品.png");
          this.cnt_turn=0;break;
           case 23:
          this.imgUrl[1] = require("../assets/5有害垃圾/电池.png");
          this.cnt_turn=0;break;
           case 4:
          this.imgUrl[1] = require("../assets/fishbone.png");
          this.cnt_turn=0;break;
          case 8:
          this.imgUrl[1] = require("../assets/骨头.png");
          this.cnt_turn=0;break;
        case 12:
          this.imgUrl[1] = require("../assets/4厨余垃圾/厨余垃圾-果壳.png");
          this.cnt_turn=0;break;
          case 16:
          this.imgUrl[1] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 20:
          this.imgUrl[1] = require("../assets/4厨余垃圾/披萨.png");
          this.cnt_turn=0;break;
           case 24:
          this.imgUrl[1] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 28:
          this.imgUrl[1] = require("../assets/4厨余垃圾/菜.png");
          this.cnt_turn=0;break;
      }
       if(this.cnt_turn)
      {
        this.m[order]-=20;
      }
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
        this.Origin_top[order] = Math.ceil(this.Origin_top[2] * 20+9);
      } while (this.Origin_top[order] >= 25);
      do {
        this.Origin_left[order] = Math.random();
        this.Origin_left[order] = Math.ceil(this.Origin_left[2] * 20 + 8);
      } while (this.Origin_left[order] <= 10);
       this.GaoC = this.Origin_top[order];
      this.ZuoC = this.Origin_left[order];
      this.YouC=100-this.ZuoC;
      this.keyC+=1;
      this.m[order] = Math.random();
      this.m[order] = Math.ceil(this.m[order] * this.n);
      this.cnt_turn=1;
      while(this.cnt_turn)
      {
      switch (this.m[order]) {
        case 1:
          this.imgUrl[2] = require("../assets/" + "paper.png");
          this.cnt_turn=0;
          break;
          case 5:
          this.imgUrl[2] = require("../assets/can.png");
          this.cnt_turn=0;
          break;
          case 9:
          this.imgUrl[2] = require("../assets/皮鞋.png");
          this.cnt_turn=0;
          break;
           case 13:
          this.imgUrl[2] = require("../assets/3可回收垃圾/可回收物-玻璃类.png");
          this.cnt_turn=0;break;
          case 17:
          this.imgUrl[2] = require("../assets/3可回收垃圾/插头.png");
          this.cnt_turn=0;break;
          case 21:
          this.imgUrl[2] = require("../assets/3可回收垃圾/旧衣服.png");
          this.cnt_turn=0;break;
          case 25:
          this.imgUrl[2] = require("../assets/3可回收垃圾/枕头.png");
          this.cnt_turn=0;break;
          case 29:
          this.imgUrl[2] = require("../assets/3可回收垃圾/酒瓶-啤酒-雪花.png");
          this.cnt_turn=0;break;
          case 33:
          this.imgUrl[2] = require("../assets/3可回收垃圾/砧板.png");
          this.cnt_turn=0;break;
          case 37:
          this.imgUrl[2] = require("../assets/3可回收垃圾/毛绒玩具.png");
          this.cnt_turn=0;break;
          case 41:
          this.imgUrl[2] = require("../assets/3可回收垃圾/衣架.png");
          this.cnt_turn=0;break;
        case 2:
          this.imgUrl[2] = require("../assets/smoke.png");
          this.cnt_turn=0;break;
          case 6:
          this.imgUrl[2] = require("../assets/卫生纸.png");
          this.cnt_turn=0;break;
           case 10:
          this.imgUrl[2] = require("../assets/纸杯.png");
          this.cnt_turn=0;break;
          case 14:
          this.imgUrl[2] = require("../assets/6其他垃圾/筷子.png");
          this.cnt_turn=0;break;
          case 18:
          this.imgUrl[2] = require("../assets/6其他垃圾/贝壳.png");
          this.cnt_turn=0;break;
        case 3:
          this.imgUrl[2] = require("../assets/battery.png");
          this.cnt_turn=0;break;
        case 7:
          this.imgUrl[2] = require("../assets/毒药,毒物,有毒药物,poison.png");
          this.cnt_turn=0;break;
        case 11:
          this.imgUrl[2] = require("../assets/有害垃圾-废弃温度计.png");
          this.cnt_turn=0;break;
           case 15:
          this.imgUrl[2] = require("../assets/5有害垃圾/除草剂.png");
          this.cnt_turn=0;break;
           case 19:
          this.imgUrl[2] = require("../assets/5有害垃圾/有害垃圾-过期药品.png");
          this.cnt_turn=0;break;
           case 23:
          this.imgUrl[2] = require("../assets/5有害垃圾/电池.png");
          this.cnt_turn=0;break;
           case 4:
          this.imgUrl[2] = require("../assets/fishbone.png");
          this.cnt_turn=0;break;
          case 8:
          this.imgUrl[2] = require("../assets/骨头.png");
          this.cnt_turn=0;break;
        case 12:
          this.imgUrl[2] = require("../assets/4厨余垃圾/厨余垃圾-果壳.png");
          this.cnt_turn=0;break;
          case 16:
          this.imgUrl[2] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 20:
          this.imgUrl[2] = require("../assets/4厨余垃圾/披萨.png");
          this.cnt_turn=0;break;
           case 24:
          this.imgUrl[2] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 28:
          this.imgUrl[2] = require("../assets/4厨余垃圾/菜.png");
          this.cnt_turn=0;break;
      }
       if(this.cnt_turn)
      {
        this.m[order]-=20;
      }
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
        this.Origin_top[order] = Math.ceil(this.Origin_top[3] * 2 +10);
      } while (this.Origin_top[order] <= 0);
      do {
        this.Origin_left[order] = Math.random();
        this.Origin_left[order] = Math.ceil(this.Origin_left[3] * 44 + 30);
      } while (this.Origin_left[order] <= 0);
       this.GaoD = this.Origin_top[order];
      this.ZuoD = this.Origin_left[order];
      this.YouD=100-this.ZuoA;
      this.keyD+=1;
      this.m[order] = Math.random();
      this.m[order] = Math.ceil(this.m[order] * this.n);
      this.cnt_turn=1;
      while(this.cnt_turn)
      {
        this.Oncall();
      switch (this.m[order]) {
        case 1:
          this.imgUrl[3] = require("../assets/" + "paper.png");
          this.cnt_turn=0;
          break;
          case 5:
          this.imgUrl[3] = require("../assets/can.png");
          this.cnt_turn=0;
          break;
          case 9:
          this.imgUrl[3] = require("../assets/皮鞋.png");
          this.cnt_turn=0;
          break;
           case 13:
          this.imgUrl[3] = require("../assets/3可回收垃圾/可回收物-玻璃类.png");
          this.cnt_turn=0;break;
          case 17:
          this.imgUrl[3] = require("../assets/3可回收垃圾/插头.png");
          this.cnt_turn=0;break;
          case 21:
          this.imgUrl[3] = require("../assets/3可回收垃圾/旧衣服.png");
          this.cnt_turn=0;break;
          case 25:
          this.imgUrl[3] = require("../assets/3可回收垃圾/枕头.png");
          this.cnt_turn=0;break;
          case 29:
          this.imgUrl[3] = require("../assets/3可回收垃圾/酒瓶-啤酒-雪花.png");
          this.cnt_turn=0;break;
          case 33:
          this.imgUrl[3] = require("../assets/3可回收垃圾/砧板.png");
          this.cnt_turn=0;break;
          case 37:
          this.imgUrl[3] = require("../assets/3可回收垃圾/毛绒玩具.png");
          this.cnt_turn=0;break;
          case 41:
          this.imgUrl[3] = require("../assets/3可回收垃圾/衣架.png");
          this.cnt_turn=0;break;
        case 2:
          this.imgUrl[3] = require("../assets/smoke.png");
          this.cnt_turn=0;break;
          case 6:
          this.imgUrl[3] = require("../assets/卫生纸.png");
          this.cnt_turn=0;break;
           case 10:
          this.imgUrl[3] = require("../assets/纸杯.png");
          this.cnt_turn=0;break;
          case 14:
          this.imgUrl[3] = require("../assets/6其他垃圾/筷子.png");
          this.cnt_turn=0;break;
          case 18:
          this.imgUrl[3] = require("../assets/6其他垃圾/贝壳.png");
          this.cnt_turn=0;break;
        case 3:
          this.imgUrl[3] = require("../assets/battery.png");
          this.cnt_turn=0;break;
        case 7:
          this.imgUrl[3] = require("../assets/毒药,毒物,有毒药物,poison.png");
          this.cnt_turn=0;break;
        case 11:
          this.imgUrl[3] = require("../assets/有害垃圾-废弃温度计.png");
          this.cnt_turn=0;break;
           case 15:
          this.imgUrl[3] = require("../assets/5有害垃圾/除草剂.png");
          this.cnt_turn=0;break;
           case 19:
          this.imgUrl[3] = require("../assets/5有害垃圾/有害垃圾-过期药品.png");
          this.cnt_turn=0;break;
           case 23:
          this.imgUrl[3] = require("../assets/5有害垃圾/电池.png");
          this.cnt_turn=0;break;
           case 4:
          this.imgUrl[3] = require("../assets/fishbone.png");
          this.cnt_turn=0;break;
          case 8:
          this.imgUrl[3] = require("../assets/骨头.png");
          this.cnt_turn=0;break;
        case 12:
          this.imgUrl[3] = require("../assets/4厨余垃圾/厨余垃圾-果壳.png");
          this.cnt_turn=0;break;
          case 16:
          this.imgUrl[3] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 20:
          this.imgUrl[3] = require("../assets/4厨余垃圾/披萨.png");
          this.cnt_turn=0;break;
           case 24:
          this.imgUrl[3] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 28:
          this.imgUrl[3] = require("../assets/4厨余垃圾/菜.png");
          this.cnt_turn=0;break;
      }
      if(this.cnt_turn)
      {
        this.m[order]-=20;
      }
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
        this.Origin_top[order] = Math.ceil(this.Origin_top[4] * 20+5);
      } while (this.Origin_top[order] >= 25);
      do {
        this.Origin_left[order] = Math.random();
        this.Origin_left[order] = Math.ceil(this.Origin_left[4] * 50+35);
      } while (this.Origin_left[order] <= 10);
       this.GaoE = this.Origin_top[order];
      this.ZuoE = this.Origin_left[order];
      this.YouE=100-this.ZuoE;
      this.keyE+=1;
      this.m[order] = Math.random();
      this.m[order] = Math.ceil(this.m[order] * this.n);
        this.cnt_turn=1;
      while(this.cnt_turn)
      {
      switch (this.m[order]) {
        case 1:
          this.imgUrl[4] = require("../assets/" + "paper.png");
          this.cnt_turn=0;
          break;
          case 5:
          this.imgUrl[4] = require("../assets/can.png");
          this.cnt_turn=0;
          break;
          case 9:
          this.imgUrl[4] = require("../assets/皮鞋.png");
          this.cnt_turn=0;
          break;
           case 13:
          this.imgUrl[4] = require("../assets/3可回收垃圾/可回收物-玻璃类.png");
          this.cnt_turn=0;break;
          case 17:
          this.imgUrl[4] = require("../assets/3可回收垃圾/插头.png");
          this.cnt_turn=0;break;
          case 21:
          this.imgUrl[4] = require("../assets/3可回收垃圾/旧衣服.png");
          this.cnt_turn=0;break;
          case 25:
          this.imgUrl[4] = require("../assets/3可回收垃圾/枕头.png");
          this.cnt_turn=0;break;
          case 29:
          this.imgUrl[4] = require("../assets/3可回收垃圾/酒瓶-啤酒-雪花.png");
          this.cnt_turn=0;break;
          case 33:
          this.imgUrl[4] = require("../assets/3可回收垃圾/砧板.png");
          this.cnt_turn=0;break;
          case 37:
          this.imgUrl[4] = require("../assets/3可回收垃圾/毛绒玩具.png");
          this.cnt_turn=0;break;
          case 41:
          this.imgUrl[4] = require("../assets/3可回收垃圾/衣架.png");
          this.cnt_turn=0;break;
        case 2:
          this.imgUrl[4] = require("../assets/smoke.png");
          this.cnt_turn=0;break;
          case 6:
          this.imgUrl[4] = require("../assets/卫生纸.png");
          this.cnt_turn=0;break;
           case 10:
          this.imgUrl[4] = require("../assets/纸杯.png");
          this.cnt_turn=0;break;
          case 14:
          this.imgUrl[4] = require("../assets/6其他垃圾/筷子.png");
          this.cnt_turn=0;break;
          case 18:
          this.imgUrl[4] = require("../assets/6其他垃圾/贝壳.png");
          this.cnt_turn=0;break;
        case 3:
          this.imgUrl[4] = require("../assets/battery.png");
          this.cnt_turn=0;break;
        case 7:
          this.imgUrl[4] = require("../assets/毒药,毒物,有毒药物,poison.png");
          this.cnt_turn=0;break;
        case 11:
          this.imgUrl[4] = require("../assets/有害垃圾-废弃温度计.png");
          this.cnt_turn=0;break;
           case 15:
          this.imgUrl[4] = require("../assets/5有害垃圾/除草剂.png");
          this.cnt_turn=0;break;
           case 19:
          this.imgUrl[4] = require("../assets/5有害垃圾/有害垃圾-过期药品.png");
          this.cnt_turn=0;break;
           case 23:
          this.imgUrl[4] = require("../assets/5有害垃圾/电池.png");
          this.cnt_turn=0;break;
           case 4:
          this.imgUrl[4] = require("../assets/fishbone.png");
          this.cnt_turn=0;break;
          case 8:
          this.imgUrl[4] = require("../assets/骨头.png");
          this.cnt_turn=0;break;
        case 12:
          this.imgUrl[4] = require("../assets/4厨余垃圾/厨余垃圾-果壳.png");
          this.cnt_turn=0;break;
          case 16:
          this.imgUrl[4] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 20:
          this.imgUrl[4] = require("../assets/4厨余垃圾/披萨.png");
          this.cnt_turn=0;break;
           case 24:
          this.imgUrl[4] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 28:
          this.imgUrl[4] = require("../assets/4厨余垃圾/菜.png");
          this.cnt_turn=0;break;
      }
      if(this.cnt_turn)
      {
        this.m[order]-=20;
      }
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
      this.cnt_turn=1;
      while(this.cnt_turn)
      {
      switch (this.m[cnt]) {
        case 1:
          this.imgUrl[cnt] = require("../assets/" + "paper.png");
          this.cnt_turn=0;
          break;
          case 5:
          this.imgUrl[cnt] = require("../assets/can.png");
          this.cnt_turn=0;
          break;
          case 9:
          this.imgUrl[cnt] = require("../assets/皮鞋.png");
          this.cnt_turn=0;
          break;
           case 13:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/可回收物-玻璃类.png");
          this.cnt_turn=0;break;
          case 17:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/插头.png");
          this.cnt_turn=0;break;
          case 21:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/旧衣服.png");
          this.cnt_turn=0;break;
          case 25:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/枕头.png");
          this.cnt_turn=0;break;
          case 29:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/酒瓶-啤酒-雪花.png");
          this.cnt_turn=0;break;
          case 33:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/砧板.png");
          this.cnt_turn=0;break;
          case 37:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/毛绒玩具.png");
          this.cnt_turn=0;break;
          case 41:
          this.imgUrl[cnt] = require("../assets/3可回收垃圾/衣架.png");
          this.cnt_turn=0;break;
        case 2:
          this.imgUrl[cnt] = require("../assets/smoke.png");
          this.cnt_turn=0;break;
          case 6:
          this.imgUrl[cnt] = require("../assets/卫生纸.png");
          this.cnt_turn=0;break;
           case 10:
          this.imgUrl[cnt] = require("../assets/纸杯.png");
          this.cnt_turn=0;break;
          case 14:
          this.imgUrl[cnt] = require("../assets/6其他垃圾/筷子.png");
          this.cnt_turn=0;break;
          case 18:
          this.imgUrl[cnt] = require("../assets/6其他垃圾/贝壳.png");
          this.cnt_turn=0;break;
        case 3:
          this.imgUrl[cnt] = require("../assets/battery.png");
          this.cnt_turn=0;break;
        case 7:
          this.imgUrl[cnt] = require("../assets/毒药,毒物,有毒药物,poison.png");
          this.cnt_turn=0;break;
        case 11:
          this.imgUrl[cnt] = require("../assets/有害垃圾-废弃温度计.png");
          this.cnt_turn=0;break;
           case 15:
          this.imgUrl[cnt] = require("../assets/5有害垃圾/除草剂.png");
          this.cnt_turn=0;break;
           case 19:
          this.imgUrl[cnt] = require("../assets/5有害垃圾/有害垃圾-过期药品.png");
          this.cnt_turn=0;break;
           case 23:
          this.imgUrl[cnt] = require("../assets/5有害垃圾/电池.png");
          this.cnt_turn=0;break;
           case 4:
          this.imgUrl[cnt] = require("../assets/fishbone.png");
          this.cnt_turn=0;break;
          case 8:
          this.imgUrl[cnt] = require("../assets/骨头.png");
          this.cnt_turn=0;break;
        case 12:
          this.imgUrl[cnt] = require("../assets/4厨余垃圾/厨余垃圾-果壳.png");
          this.cnt_turn=0;break;
          case 16:
          this.imgUrl[cnt] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 20:
          this.imgUrl[cnt] = require("../assets/4厨余垃圾/披萨.png");
          this.cnt_turn=0;break;
           case 24:
          this.imgUrl[cnt] = require("../assets/4厨余垃圾/厨余垃圾-残枝落叶.png");
          this.cnt_turn=0;break;
           case 28:
          this.imgUrl[cnt] = require("../assets/4厨余垃圾/菜.png");
          this.cnt_turn=0;break;
      }
      if(this.cnt_turn)
      {
        this.m[cnt]-=20;
      }
      }
    }
  },
  mounted() {

    this.YouA=100-this.ZuoA;
    this.YouB=100-this.ZuoB;
    this.YouC=100-this.ZuoC;
    this.YouD=100-this.ZuoD;
    this.YouE=100-this.ZuoE;
    this.Origin_top[0]=this.GaoA;
    this.Origin_top[1]=this.GaoB;
    this.Origin_top[2]=this.GaoC;
    this.Origin_top[3]=this.GaoD;
    this.Origin_top[4]=this.GaoE;
    this.Origin_left[0]=this.ZuoA;
    this.Origin_left[1]=this.ZuoB;
    this.Origin_left[2]=this.ZuoC;
    this.Origin_left[3]=this.ZuoD;
    this.Origin_left[4]=this.ZuoE;
   var turn = 0;
         setInterval(() => {
      if (this.$refs.CountT.left=== 0 && turn === 0) {
        let success = document.getElementById("success");
        success.play();
       this.GG_turn=1;
       this.GG_off=0;
       this.$forceUpdate();
        turn = 1;
      }
    }, 20);
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
body{
  overflow: hidden;
   height: 100%;
  width: 100%;
}
html{
  height: 100%;
  width: 100%;
}
.tools {
  position: absolute;
  background-color: rgb(254, 245, 230);
  width: 86px;
  top: 30vh;
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
  border-radius: 45%;
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
  top: 62vh;
  left: 33vw;
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
  top: 62vh;
  left: 80vw;
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
  top: 62vh;
  left: 10vw;
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
  top: 62vh;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 50px;
  left: 57vw;
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
  left: -15vw;
  top: 13vh;
  position: absolute;
}
.rORwTwo {
  transform: scale(0.17);

  left: 8vw;
  top: 13vh;
  position: absolute;
}
.rORwThree {
  transform: scale(0.17);
  left: 31vw;
  top: 13vh;
  position: absolute;
}
.rORwFour {
  transform: scale(0.17);
  left: 49vw;
  top: 13vh;
  position: absolute;
}
</style>