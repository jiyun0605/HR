<template>
    <div class="block">
        <h3>파운드로 변환</h3>
        <input type="text" v-model="kilogram" placeholder="0kg">
        <p>{{this.change()}}파운드</p>
        
    </div>
</template>
<script>
export default {
    data(){
        return{
            pound:'',
            kilogram:''
        }
    },
    methods:{
        change:function(){
            this.pound = this.kilogram * 2.2;
            return Math.ceil(this.pound);
        }
    }
}
</script>
<style src="../assets/style.css"></style>
