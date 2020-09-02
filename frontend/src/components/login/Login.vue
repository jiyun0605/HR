<template>
    <div class="">
        <div class="input_row">
            <label for="id">아이디</label>
            <input type="text" id="id" v-model="user.userid">
        </div>
        <div class="input_row">
            <label for="password">비밀번호</label>
            <input type="password" id="password" v-model="user.password">
        </div>  
        <button v-on:click="login">로그인</button>
        <br>
        <a href="/signUp">회원 가입하기</a>
    </div>
</template>


<script>
export default {
     created(){
        // this.$http.get('http://localhost:3000/userList')
        //     .then((res) => {
        //         this.userData = res.data
        //     })
        this.$http.get('http://localhost:3000/login')
            .catch((err) => {
                if(err.response.status == 400){
                    this.$router.push('/unit')
                }
            })
    },
    data() {
        return {
            user: {
                userid: '',
                password: ''
            },
            userdata:[]
        }
},
    methods: {
        login: function() {
            //alert(this.user.userid)
                // if(this.user.userid == this.userData.filter(function(userData){
                //     return this.user.id == userData
                // })){
                //     alert("id일치")
                //     alert("main 페이지로 이동");
                //     this.$router.push('/')
                // }
                this.$http.post('http://localhost:3000/login', { 
                'userid': this.user.userid,
                'password': this.user.password,
                })
            }
        },
}
</script>

<style src="./login.css" />