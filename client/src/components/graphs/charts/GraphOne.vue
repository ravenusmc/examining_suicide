<template>
  <div>

  <div class='center'>
    <GChart
      type="LineChart"
      :resizeDebounce="500"
      :data="chartData"
      :options="chartOptions"/>
  </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GraphOne',
  data () {
    return {
      chartData: [],
      chartOptions: {
        title: 'Total Suicides By Year (World)',
        chart: {
          title: 'Suicides By Year',
        },
        hAxis: {
          title: 'Year',
          gridlines: { count: 15 },
          format: 'YY'
        },
        vAxis: {
          title: 'Suicides',
          gridlines: { count: 5 }
        },
      }
    }
  },//End of data object
  mounted() {
    const path = 'http://localhost:5000/build_total_suicides_graph';
    axios.get(path)
      .then((res) => {
        console.log('hi')
        this.chartData = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }, //End of mounted
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
