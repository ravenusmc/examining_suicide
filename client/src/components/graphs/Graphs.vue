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

  <TreeMap></TreeMap>

  <!-- Graphs I need

  4. Show age group-bar chart?
  5. Tree chart of top 5 countries

  -->

  </div>
</template>

<script>
import axios from 'axios';
import GraphOne from './charts/GraphOne';
import GraphTwo from './charts/GraphTwo';
import GraphThree from './charts/GraphThree';
import GraphFour from './charts/GraphFour';
import TreeMap from './charts/TreeMap';

export default {
  components: {
    GraphOne,
    GraphTwo,
    GraphThree,
    GraphFour,
    TreeMap
  },
  data () {
    return {
    }
  },//End of data object
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
