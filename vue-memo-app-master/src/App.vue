<template>
  <div id="app">
    <app-header />
    <memoForm/>
    <MemoList/>
    <changeTokg/>
    <changeToPound/>
    <plate/>
  </div>
</template>

<script>
import AppHeader from './components/AppHeader';
import MemoForm from './components/MemoForm';
import MemoList from './components/MemoList';
import changeTokg from './components/changeTokg';
import changeToPound from './components/changeToPound.vue';
import plate from './components/plate';

export default {
  name: 'app',
  components: {
    AppHeader,
    MemoForm,
    MemoList,
    changeTokg,
    changeToPound,
    plate,
    
    
  }
};
</script>

<style>
@import './styles/reset.css';

#app {
  width: 560px;
  margin: 0 auto;
}
</style>
