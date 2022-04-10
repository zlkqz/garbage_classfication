<template>
  <div>
    <div class="cover"></div>
    <div class="total">
      <div class="over">&nbsp;游 戏 结 束~</div>
      <div class="pictureK"></div>
      <div class="pictureO"></div>
      <div class="pictureP"></div>
      <div class="pictureR"></div>
      <button class="again" @click="jump">再来一次</button>
      <div>
        <button class="return" @click="quit">返回主页</button>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "tempComponent",
  methods: {
    jump() {
      location.reload();
      //this.$router.push('/oo')
    },
    quit(){
      window.location.href = "http://1.117.150.150:8080/project/entrance"
    }
  },
};
</script>

<style>
.cover {
    position: absolute;
    z-index: 2;
    top: 0;
    height: 100vh;
    width: 100vw;
    background-color: rgba(33,33,33,0.8);
}
.pictureK {
  position: absolute;
  background: url("../assets/科普-厨余垃圾.png") no-repeat;
  background-size: 100%;
  width: 18vw;
  top: 40vh;
  left: 2vw;
  height: 7.7vw;
  transition: height 1s;
}

.pictureK:hover {
  height: 20vw;
  z-index: 2;
}
.pictureO {
      position: absolute;
  background: url("../assets/科普-其他垃圾.png") no-repeat;
  background-size: 100%;
  width: 18vw;
  top: 15vh;
  left: 17vw;
  height: 7.7vw;
  transition: height 1s;
}

.pictureO:hover {
  height: 20vw;
  z-index: 2;
}
.pictureP {
      position: absolute;
  background: url("../assets/科普-有害垃圾.png") no-repeat;
  background-size: 100%;
  width: 18vw;
  top: 40vh;
  left: 32vw;
  height: 7.7vw;
  transition: height 1s;
}

.pictureP:hover {
  height: 20vw;
    z-index: 2;
}
.pictureR {
      position: absolute;
  background: url("../assets/科普-可回收垃圾.png") no-repeat;
  background-size: 100%;
  width: 18vw;
  top: 15vh;
  left: 47vw;
  height: 7.7vw;
  transition: height 1s;
}

.pictureR:hover {
  height: 20vw;
    z-index: 2;
}

.total {
    position: relative;
    width: 80vw;
    height: 80vh;
    border-radius: 10vh;
    top: 10vh;
    left: 10vw;
    z-index: 3;
    background-color: white;
    background: url("../assets/overBack2.jpeg");
    background-size: cover;
}

.over {
    position: absolute;
    width: 100%;
    text-shadow: 1px 0 0 orange,0 1px 0 orange,-1px 0 0 orange,-1px 0 0 orange;
    text-align: center;
    margin: 0 auto;
    top: 1vh;
  animation: myfirst 5.2s;
  box-shadow: 20px;
  color: rgba(181, 55, 33, 0.66);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 10vh;
  font-weight: 1000;
  animation-iteration-count: infinite;
}
.return {
    position: absolute;
    right: 4vw;
    bottom: 9vh;
  padding: 3vh;
  text-decoration: none;
  border-radius: 10px;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  font-weight: 1000;
  font-size: 20px;
  color: rgba(234, 224, 35, 0.874);
  background-color: rgba(225, 225, 41, 0.7);
  background-image: linear-gradient(
    rgba(245, 60, 236, 0.542),
    #fb06ef91,
    #f708bc4b
  );
}

.return:hover {
  box-shadow: 3px 3px 5px rgba(241, 182, 20, 0.589);
  text-decoration: none;
  border-radius: 20px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-weight: 1000;
  font-size: 20px;
  color: rgba(234, 224, 35, 0.967);
  background-color: rgba(252, 11, 11, 0.538);
  background-image: linear-gradient(
    rgba(248, 37, 238, 0.815),
    #fb06b67a,
    #f708bbf6
  );
}

.again {
    position: absolute;
    right: 4vw;
    bottom: 22vh;
  padding: 3vh;
  text-decoration: none;
  border-radius: 10px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-weight: 1000;
  font-size: 20px;
  color: rgba(234, 224, 35, 0.874);
  background-color: rgba(225, 225, 41, 0.7);
  background-image: linear-gradient(
    rgba(245, 60, 236, 0.542),
    #fb06ef91,
    #f708bc4b
  );
}

.again:hover {
  box-shadow: 3px 3px 5px rgba(241, 182, 20, 0.589);
  text-decoration: none;
  border-radius: 20px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-weight: 1000;
  font-size: 20px;
  color: rgba(234, 224, 35, 0.967);
  background-color: rgba(252, 11, 11, 0.538);
  background-image: linear-gradient(
    rgba(248, 37, 238, 0.887),
    #fb06b6b4,
    #f708bbfd
  );
}

@keyframes myfirst {
  0% {
    color: rgba(181, 55, 33, 0.66);
  }

  20% {
    color: rgba(237, 50, 17, 0.815);
  }

  50% {
    color: rgba(214, 214, 24, 0.694);
  }

  50% {
    color: rgba(250, 250, 26, 0.694);
  }

  50% {
    color: rgba(204, 208, 3, 0.722);
  }

  70% {
    color: rgba(114, 213, 33, 0.838);
  }

  75% {
    color: rgba(60, 186, 31, 0.548);
  }

  80% {
    color: rgba(175, 206, 39, 0.802);
  }

  85% {
    color: rgba(206, 185, 28, 0.686);
  }

  90% {
    color: rgba(212, 160, 28, 0.856);
  }

  95% {
    color: rgba(212, 71, 28, 0.856);
  }

  100% {
    color: rgba(181, 55, 33, 0.66);
  }
}
</style>