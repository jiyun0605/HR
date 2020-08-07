<template>
  <li class="memo-item">
    <strong>{{memo.title}}</strong>
    <p @dblclick="handleDbClick">
      <template v-if="!isEditing">{{memo.content}}</template>
      <input
        v-else
        type="text"
        ref="content"
        :value="memo.content"
        @blur="handleBlur"
        @keydown.enter="updateMemo"
      />
    </p>
    <button type="button">
      <i class="fas fa-times" @click="deleteMemo"></i>
    </button>
  </li>
</template>

<script>
export default {
  name: 'memo',
  props: {
    memo: {
      type: Object
    },
    editingId: {
      type: Number
    }
  },
  // data() {
  //   return {
  //     isEditing: false
  //   };
  // },
  computed: {
    isEditing() {
      return this.memo.id === this.editingId;
    }
  },
  methods: {
    deleteMemo() {
      const { id } = this.memo;
      this.$emit('deleteMemo', id);
    },
    handleBlur() {
      // this.isEditing = false;
      this.$emit('resetEditingId');
    },
    handleDbClick() {
      // this.isEditing = true;
      this.$emit('setEditingId', this.memo.id);
      this.$nextTick(() => this.$refs.content.focus());
    },
    updateMemo({ target: { value } }) {
      const { id } = this.memo;
      const content = value.trim();
      if (content.length <= 0) return false;
      this.$emit('updateMemo', { id, content });
      this.isEditing = false;
    }
  }
};
</script>

<style scoped>
.memo-item {
  overflow: hidden;
  position: relative;
  margin-bottom: 20px;
  padding: 24px;
  box-shadow: 0 4px 10px -4px rgba(0, 0, 0, 0.2);
  background-color: #fff;
}
.memo-item button {
  background: none;
  position: absolute;
  right: 20px;
  top: 20px;
  font-size: 20px;
  color: #e5e5e5;
  border: 0;
}
.memo-item strong {
  display: block;
  margin-bottom: 12px;
  font-size: 18px;
  /* font-weight: normal; */
  word-break: break-all;
}
.memo-item p {
  margin: 0;
  font-size: 14px;
  line-height: 22px;
  color: #666;
}
.memo-item p input[type='text'] {
  box-sizing: border-box;
  width: 100%;
  font-size: inherit;
  border: 1px solid #999;
}
</style>