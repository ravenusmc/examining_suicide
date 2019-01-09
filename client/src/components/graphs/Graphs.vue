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

  <!-- Graphs I need

  1. Graph of suicides in U.S.
  2. Graph of suicides in males - U.S.
  3.  Graph of suicides in females -U.S
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

export default {
  components: {
    GraphOne,
    GraphTwo,
    GraphThree,
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
