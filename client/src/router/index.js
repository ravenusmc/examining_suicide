import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/home/Home';
import About from '@/components/about/About';
import World from '@/components/world/World';
import Fact from '@/components/facts/Fact';
import Graphs from '@/components/graphs/Graphs';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/about',
      name: 'About',
      component: About,
    },
    {
      path: '/world',
      name: 'World',
      component: World,
    },
    {
      path: '/fact',
      name: 'Fact',
      component: Fact,
    },
    {
      path: '/graphs',
      name: 'Graphs',
      component: Graphs,
    },
  ],
  mode: 'history',
});
