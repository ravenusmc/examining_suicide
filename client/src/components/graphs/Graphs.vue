<template>
  <div>

  <header class='center'>
    <md-content class="md-elevation-19">
      <h1 class='font'>Graph Page</h1>
    </md-content>
  </header>

  <GraphOne></GraphOne>

  <hr>

  <GraphTwo></GraphTwo>

  <hr>

  <GraphThree></GraphThree>

  <hr>

  <GraphFour></GraphFour>

  <hr>

  <h2 class='center'>Graph's of Suicides By Age Group (U.S.)</h2>

    <form @submit="onSubmit">
      <select v-model="age" name="age">
        <option v-for="age in age_group" :value="age">{{age}}</option>
      </select>
      <button type="submit" variant="primary">Submit</button>
    </form>
    <component :is="component"></component>

  <hr>

  <h2 class='center'>TreeMap of Top 5 Countries with Most Suicides</h2>

  <TreeMap></TreeMap>

  <!-- Graphs I need
  4. Show age group-bar chart?
  -->

  </div>
</template>

<script>
import axios from 'axios';
//Importing components 
import GraphOne from './charts/GraphOne';
import GraphTwo from './charts/GraphTwo';
import GraphThree from './charts/GraphThree';
import GraphFour from './charts/GraphFour';
import TreeMap from './charts/TreeMap';
import First from './ageGraphs/First';
import Second from './ageGraphs/Second';

export default {
  components: {
    GraphOne,
    GraphTwo,
    GraphThree,
    GraphFour,
    TreeMap,
    First,
    Second,
  },
  data () {
    return {
      age: '',
      age_group: ['5-14 years', '15-24 years', '25-34 years',
      '35-54 years', '55-74 years', '75+ years'],
      component: 'First',
    }
  },//End of data object
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        age: this.age
      };
      if (this.age == '5-14 years'){
        this.component = 'First'
      }else if (this.age == '15-24 years'){
        this.component = 'Second'
      }else if (this.age == '25-34 years'){
        this.component = 'Second'
      }else if (this.age == '35-54 years'){
        this.component = 'Second'
      }else if (this.age == '55-74 years'){
        this.component = 'Second'
      }else if (this.age == '75+ years'){
        this.component = 'Second'
      }
    },
  },
}


</script>

<style scoped>
.font {
  font-family: 'Thasadith', sans-serif;
}

.center {
  text-align: center;
}

header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 50px;
  margin-bottom: 30px;
}

</style>
