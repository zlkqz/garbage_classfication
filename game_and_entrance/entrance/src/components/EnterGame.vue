<template>
    <div class="start-container" @mousedown="clicking" @mouseup="clicked">
        <img src="../assets/startgame.png" class="startbtn" :class="{down: isMouseDown}">
    </div>
</template>

<script>
export default {
    name: 'EnterGame',
    data(){
        return{
            isMouseDown: false
        };
    },
    methods: {
        startGame(){
            window.location.href = "#"
        },
        clicking(){
            this.isMouseDown = true;
        },
        clicked(){
            this.isMouseDown = false
        }
    }
}
</script>

<style scoped>
    .start-container {
        position: absolute;
        top: 64vh;
        left: 44vw;
        box-shadow: -1px -1px 30px black;
    }
    .start-container:hover {
        cursor: pointer;
    }
    .startbtn {
        height: 9vh;
        width: 26vh;
    }
    .down {
        opacity: 0.8;
    }
</style>