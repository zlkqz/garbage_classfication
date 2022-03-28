<template>
    <div class="border">
        <div class="seconds">{{left}}s</div>
        <div class="fill" :style="{width: 150*precentage+'px',backgroundColor: color}"></div>
    </div>
    
</template>

<script>
export default {
    name: 'CountTimer',
    data(){
        return{
            //总时间,可以更改
            total: 20,
            //剩余时间，无需变动，开始时会自动等于总时间
            left: 0,
            //加时道具，一次加多少时间
            addAmount: 5,
            precentage: 1,
            color: '#7FFFAA'
        }
    },
    methods: {
        watchColor(){
            if(this.precentage > 2/3){
                this.color = '#7FFFAA'
            }else if(this.precentage < 2/3&&this.precentage > 1/3){
                this.color = 'yellow'
            }else if(this.precentage < 1/3){
                this.color = 'red'
            }
        },
        //使用加时道具时调用此方法
        addTimeAmount(){
            let theoryLeft = this.left + this.addAmount;
            this.left = theoryLeft >= this.total? this.total: theoryLeft;
            this.precentage = this.left/this.total;
            this.watchColor();
        },
        //请在点击要玩游戏时调用这个方法
        startGame(){
            const that = this;
            that.left = that.total;
            const timer = setInterval(function(){
                that.left--;
                if(that.left <= 0){
                    clearInterval(timer);
                    //调用父组件游戏结束的事件
                    //gameover();
                }
                that.precentage = that.left/that.total;
                that.watchColor();
            },1000)
        },  
    },
    mounted(){
        this.startGame();
    }
}
</script>

<style scoped>
/* 时间条的外边框 */
.border {
    position: relative;
    width: 150px;
    height: 15px;
    border: 2px solid orange;
    border-radius: 8px;
}
/* 时间条的秒数显示 */
.seconds {
    position: absolute;
    left: 67px;
    font-size: 10px;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-weight: 700;
}
/* 时间条的填充物 */
.fill {
    height: 15px;
    border-radius: 6px;
}
</style>