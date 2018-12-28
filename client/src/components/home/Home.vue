<template>
  <div>
    <Header></Header>
    <hr>
    <Content></Content>
    <hr>
  </div>
</template>

<script>
import Header from '@/components/home/Header';
import Content from '@/components/home/Content';

export default {
  name: 'Home',
  components: {
    Header,
    Content,
  },
};
</script>

<style>
</style>
