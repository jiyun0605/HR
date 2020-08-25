<template>  
        <div class="block">
            <div>
            5kg 단위로 설정해주세요 ex(155, 170, 95)
            <br>
            <input type="text" placeholder="몇을 원하나" v-model="weight">
            <button v-on:click="check">눌러라</button>
            </div>

            <div>
                {{gd}}kg를 만들려면 이렇게 하세요 
                <div v-for="item in lists" :key="item">
                    <p v-if="item.num>=1">             
                        양쪽에 {{item.a}} - {{item.num}}개씩
                    </p>
                </div>
            </div>
        </div>
</template>

<script>    
export default {
    data(){ 
        return{
            lists:[
                    {a:"20kg", num:0},
                    {a:"15kg", num:0},
                    {a:"10kg", num:0},
                    {a:"7.5kg", num:0},
                    {a:"5kg", num:0},
                    {a:"2.5kg", num:0}
                ]
        } 
    },
    methods:{
        Distribution: function(){
            this.reset();
            this.gd = this.weight;
            this.weight = this.weight - 20;

            if(this.weight<=0){
                alert("봉무게만 20이다 이놈아");
            }
            while (this.weight>0){
                if(this.weight >= 40){
                    this.lists[0].num +=1;
                    this.weight = this.weight - 40
                }
                else if(this.weight >= 30){
                    this.lists[1].num +=1;
                    this.weight = this.weight - 30
                }
                else if(this.weight >= 20){
                    this.lists[2].num +=1;
                    this.weight = this.weight - 20
                }
                else if(this.weight >= 15){
                    this.lists[3].num +=1;
                    this.weight = this.weight - 15
                }
                else if(this.weight >= 10){
                    this.lists[4].num +=1;
                    this.weight = this.weight - 10
                }
                else if(this.weight >= 5){
                    this.lists[5].num +=1;
                    this.weight = this.weight - 5
                }
            }
            this.weight = ''
        },
        reset: function(){
            for(var i=0;i<6;i++){
                this.lists[i].num = 0;            
            }
        },
        check: function(){
            if(this.weight%5 != 0){
                alert("5단위로 입력해주세요.");
            }
            else{
                this.Distribution();
            }

        }
    }
}
</script>

<style src="../assets/style.css"></style>
