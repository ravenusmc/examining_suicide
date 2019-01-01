<template>
  <div id="app">
    <Navbar></Navbar>
    <transition name="slide-fade">
      <router-view/>
    </transition>
    <Footer></Footer>
  </div>
</template>

<script>
import Navbar from '@/components/support/Navbar';
import Footer from '@/components/support/Footer';

export default {
  name: 'App',
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style>

.slide-fade-enter-active {
  transition: all .3s ease;
}
.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}

</style>
