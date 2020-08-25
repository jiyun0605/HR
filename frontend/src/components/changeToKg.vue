<template>
    <div class="block">
        <h3>킬로그램으로 변환</h3>
        <input type="text" v-model="pound" placeholder="0파운드">
        <p>{{this.change()}}kg</p>
    </div>
</template>

<script>
export default {
    data(){
        return{
            pound:'',
            kilogram:' '
        }
    },
    methods:{
        change:function(){
            this.kilogram = this.pound / 2.2;
            return Math.ceil(this.kilogram);
        }
    }
}
</script>   
<style src="../assets/style.css"></style>
