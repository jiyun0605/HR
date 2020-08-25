<template>
  <div class="memo-app">
    <memo-form @addMemo="addMemo" />
    <ul class="memo-list">
      <memo
        v-for="memo in memos"
        :key="memo.id"
        :memo="memo"
        @deleteMemo="deleteMemo"
        @updateMemo="updateMemo"
        :editingId="editingId"
        @setEditingId="SET_EDITING_ID"
        @resetEditingId="RESET_EDITING_ID"
      />
    </ul>
  </div>
</template>

<script>
import Memo from './Memo';
import MemoForm from './MemoForm';
import { mapActions, mapState, mapMutations } from 'vuex';

export default {
  name: 'memoApp',
  components: {
    MemoForm,
    Memo
  },
  // data() {
  //   return {
  //     memos: []
  //   };
  // },
  created() {
    // this.memos = localStorage.memos ? JSON.parse(localStorage.memos) : [];
    // memoAPICore.get('/').then(({ data }) => (this.memos = data));
    this.fetchMemos();
  },
  computed: {
    ...mapState(['memos', 'editingId'])
  },
  methods: {
    // addMemo(payload) {
    //   memo-form에서 올려 받은 데이터를 컴포넌트 내부에 추가
    //   this.memos.unshift(payload);
    //   this.storeMemo();
    //   memoAPICore.post('/', payload).then(({ data }) => this.memos.unshift(data));
    // },
    // deleteMemo(id) {
    //   const targetIndex = this.memos.findIndex(v => v.id === id);
    //   // this.memos.splice(targetIndex, 1);
    //   // this.storeMemo();
    //   memoAPICore.delete(`/${id}`).then(() => this.memos.splice(targetIndex, 1));
    // },
    // updateMemo(payload) {
    //   const { id, content } = payload;
    //   const targetIndex = this.memos.findIndex(v => v.id === id);
    //   const targetMemo = this.memos[targetIndex];
    //   // this.memos.splice(targetIndex, 1, { ...targetMemo, content });
    //   // this.storeMemo();
    //   memoAPICore.put(`/${id}`, { content }).then(() => this.memos.splice(targetIndex, 1, { ...targetMemo, content }));
    // },
    // storeMemo() {
    //   const memosToString = JSON.stringify(this.memos);
    //   localStorage.setItem('memos', memosToString);
    // }
    ...mapMutations(['SET_EDITING_ID', 'RESET_EDITING_ID']),
    ...mapActions(['fetchMemos', 'addMemo', 'deleteMemo', 'updateMemo'])
  }
};
</script>

<style scoped>
.memo-list {
  padding: 20px 0;
  margin: 0;
}
</style>