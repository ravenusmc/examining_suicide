<template>
  <div>

    <div class='second_graph'>

      <md-card md-with-hover>
        <md-ripple>
          <md-card-content>
            <GChart
              type="LineChart"
              :resizeDebounce="500"
              :data="chartData"
              :options="chartOptions"/>
          </md-card-content>
        </md-ripple>
      </md-card>

      <md-card md-with-hover class='first_chart_paragraph'>
       <md-ripple>
         <md-card-header>
           <div class="md-title font center">Brief Summary</div>
         </md-card-header>
         <md-card-content>
          <p class='font'>
          </p>
         </md-card-content>
       </md-ripple>
     </md-card>

    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GraphFour',
  data () {
    return {
      chartData: [],
      chartOptions: {
        height: 500,
        title: 'Total Suicides By Year (U.S Female)',
        curveType: 'function',
        legend: { position: 'top' },
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
    const path = 'http://localhost:5000/build_total_suicides_graph_us_females';
    axios.get(path)
      .then((res) => {
        this.chartData = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }, //End of mounted
};
</script>

<style scoped>
.font {
  font-family: 'Thasadith', sans-serif;
}

.center {
  text-align: center;
}

.second_graph {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 1em;
  margin-left: 5%;
  margin-right: 5%;
}
</style>
