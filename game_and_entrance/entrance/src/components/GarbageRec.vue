<template>
    <div class="btn-container" @click="this.$emit('selectFile')" @mousedown="clicking" @mouseup="clicked"> 
        <img src="../assets/uploadfile.png" class="upload-photo" :class="{down: isMouseDown}">
    </div>
</template>

<script>
export default {
    name: 'GarbageRec',
    data(){
        return{
            isMouseDown: false
        };
    },
    methods: {
        test(){
            alert("As")
            console.log(this)
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
    .btn-container {
        position: absolute;
        top: 47vh;
        left: 41vw;
        box-shadow: -2px -2px 30px black;
    }
    .btn-container:hover {
        cursor: pointer;
    }
    .upload-photo {
        border-radius: 5px;
        height: 14vh;
        width: 38.6vh;
    }
    .down {
        opacity: 0.9;
    }
</style>