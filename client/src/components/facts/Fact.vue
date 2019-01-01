<template>
  <div>
    <Header></Header>
    <Content></Content>
  </div>
</template>

<script>
import Header from './Header';
import Content from './Content';

export default {
  name: 'Fact',
  components: {
    Header,
    Content,
  }
};
</script>

<style scoped>
header {
  margin-top: 30px;
  text-align: center;
}

</style>
