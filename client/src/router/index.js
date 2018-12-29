import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/home/Home';
import About from '@/components/about/About';
import Graph from '@/components/graphs/Graph';
import Fact from '@/components/facts/Fact';

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
      path: '/graph',
      name: 'Graph',
      component: Graph,
    },
    {
      path: '/fact',
      name: 'Fact',
      component: Fact,
    },
  ],
  mode: 'history',
});
