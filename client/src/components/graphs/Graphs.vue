<template>
  <div>

  <header class='center'>
    <h1 class='font'>Graph Page</h1>
  </header>

  <GraphOne></GraphOne>

  <hr>

  <GraphTwo></GraphTwo>

  </div>
</template>

<script>
import axios from 'axios';
import GraphOne from './charts/GraphOne';
import GraphTwo from './charts/GraphTwo';

export default {
  components: {
    GraphOne,
    GraphTwo,
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
  margin-top: 50px;
  margin-bottom: 30px;
}

</style>
