<template>
  <div class="memo-form">
    
     <div>
         <p>가나다라마사</p>
            <p>{{this.data.title}}</p>
            <p>{{this.data.content}}</p>
        </div>
  </div>
</template>

<script>
export default {
  name: 'memoList',
  data() {
    return {
      title: '팔운동 루틴',
      content: '덤벨컬 5-10 오버헤드 익스프레스 5-10 케이블 익스프레스 5-10'
    };
  }
};
</script>

<style scoped>
.memo-form {
  margin-bottom: 24px;
  padding-bottom: 40px;
  border-bottom: 1px solid #eee;
}
.memo-form form fieldset div {
  position: relative;
  padding: 24px;
  margin-bottom: 20px;
  box-shadow: 0 4px 10px -4px rgba(0, 0, 0, 0.2);
  background: #fff;
}
.memo-form form fieldset div button[type='reset'] {
  position: absolute;
  right: 20px;
  bottom: 20px;
  font-size: 16px;
  background: none;
}
.memo-form form fieldset button[type='submit'] {
  float: right;
  width: 96px;
  padding: 12px 0;
  border-radius: 4px;
  background: #ff5a00;
  color: #fff;
  font-size: 16px;
}
.memo-form form fieldset .memo-form__title-form {
  width: 100%;
  margin-bottom: 12px;
  font-size: 18px;
  line-height: 26px;
}
.memo-form form fieldset .memo-form__content-form {
  width: 100%;
  height: 66px;
  font-size: 14px;
  line-height: 22px;
  vertical-align: top;
}
.memo-form input:focus,
.memo-form textarea {
  outline: none;
}
</style>