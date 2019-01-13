<template>
  <div>

  <header class='center'>
    <md-content class="md-elevation-19">
      <h1 class='font'>Graph Page</h1>
    </md-content>
  </header>

  <GraphOne></GraphOne>

  <GraphTwo></GraphTwo>

  <div class='graph_alignment'>
    <GraphThree></GraphThree>
    <GraphFour></GraphFour>
  </div>

  <hr>

  <h2 class='center'>Graph's of Suicides By Age Group (U.S.)</h2>

  <div class='age_group_graphs'>

    <form @submit="onSubmit">
      <select v-model="age" name="age">
        <option v-for="age in age_group" :value="age">{{age}}</option>
      </select>
      <md-button type="submit" class="md-raised md-primary">Change Graph</md-button>
    </form>
    <component :is="component"></component>
    
  </div>

  <hr>

  <h2 class='center'>TreeMap of Top 5 Countries with Most Suicides</h2>

  <TreeMap></TreeMap>

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

.graph_alignment {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 1em;
  margin-left: 5%;
  margin-right: 5%;
}

.age_group_graphs {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* CSS for the form */
form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

</style>
