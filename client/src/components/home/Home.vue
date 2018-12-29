<template>
  <div>
    <Header></Header>
    <hr>
    <Content></Content>
    <hr>
    <Bottom></Bottom>
  </div>
</template>

<script>
import Header from '@/components/home/Header';
import Content from '@/components/home/Content';
import Bottom from '@/components/home/Bottom';

export default {
  name: 'Home',
  components: {
    Header,
    Content,
    Bottom,
  },
};
</script>

<style>
</style>
