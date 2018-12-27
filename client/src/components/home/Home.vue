<template>
  <div>
    <Header></Header>
    <Content></Content>
  </div>
</template>

<script>
import Header from '@/components/home/Header';
import Content from '@/components/home/Content';

export default {
  name: 'Home',
  components: {
    Header,
    Content
  },
};
</script>

<style>
</style>
