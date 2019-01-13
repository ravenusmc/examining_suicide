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
     <md-ripple class='briefing_alingment_fix'>
       <md-card-header>
         <div class="md-title font center">Brief Summary</div>
       </md-card-header>
       <md-card-content>
        <p class='font'>
          What I find most interesting about this graph is that suicides, in the
          U.S, were rising until about the mid 80's. Then, in a small way, they
          started to flat line in the 90's. The rate appeared to be neither going
          up nor down during this time frame. Maybe it was that the economy in the
          90's was doing well. It was not until about 2001 that the suicide rate rose
          and really does not appear to be going down. So much happened in the early
          part of the 21st century that may have led to this. The dotcom bubble
          popping, 9-11, the 08 crash, the opiate epidemic, the wars in Iraq and
          Afghanistan. The list can go on and on.
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
  name: 'GraphThree',
  data () {
    return {
      chartData: [],
      chartOptions: {
        height: 500,
        title: 'Total Suicides By Year (U.S)',
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
    const path = 'http://localhost:5000/build_total_suicides_graph_us';
    axios.get(path)
      .then((res) => {
        this.chartData = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }, //End of mounted
}
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

.briefing_alingment_fix {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
