<template>
  <div>
    <AppHeader />
    <MemoForm/>
    <changeToKg/>
    <changeToPd/>
    <Plate/>
  </div>
</template>

<script>
import AppHeader from '../components/AppHeader';
import MemoForm from '../components/MemoForm';
import changeToKg from '../components/changeToKg';
import changeToPd from '../components/changeToPd.vue';
import Plate from '../components/Plate';

export default {
    components: {
        AppHeader,
        MemoForm,
        changeToKg,
        changeToPd,
        Plate,
  }
}
</script>