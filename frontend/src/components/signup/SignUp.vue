<template>
    <div>
        <div class="input_row">
            <label for="id">아이디</label>
            <input type="text" id="id" v-model="user.userid">
        </div>
        <div class="input_row">
            <label for="password">비밀번호</label>
            <input type="password" id="password" v-model="user.password">
        </div>
        <div class="input_row">
            <label for="name">이름</label>
            <input type="text" id="name" v-model="user.name">
        </div>
        <div>
            <button v-on:click="signUp">가입하기</button>
        </div>
    </div>
</template>


<script>
export default {
    data() {
        return {
            user: {
                userid: '',
                name: '',
                password: ''
            },
        }
    },
    methods: {
        signUp: function () {
            console.log("실행")
            this.$http.post('http://localhost:3000/signUp', { 
                'userid': this.user.userid,
                'name': this.user.name,
                'password': this.user.password,
            });
            this.checkStatus();
        },
        checkStatus: function(){
            this.$http.get(`http://localhost:3000/signUp`)
            .then((res) => {
                console.log(res)
            })
        }
    }
}
</script>
<style src="./signup.css"/>