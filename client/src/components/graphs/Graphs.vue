<template>
  <div>

  <header class='center'>
    <h1>Graph Page</h1>
  </header>

  <GraphOne></GraphOne>

  </div>
</template>

<script>
import axios from 'axios';
import GraphOne from './charts/GraphOne';

export default {
  components: {
    GraphOne
  },
  data () {
    return {
    }
  },//End of data object
}


</script>

<style>
.center {
  text-align: center;
}

header {
  margin-top: 50px;
}

</style>
