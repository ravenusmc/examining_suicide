// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';
import VueCharts from 'vue-charts';
import VueGoogleCharts from 'vue-google-charts'

Vue.config.productionTip = false;
//Charting libraries 
Vue.use(VueCharts)
Vue.use(VueGoogleCharts)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
