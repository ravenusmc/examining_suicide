<template>
  <div>

  <header class='center'>
    <h1>Graph Page</h1>
  </header>

<GChart
  type="LineChart"
  :resizeDebounce="500"
  :data="chartData"
  :options="chartOptions"/>


<!-- <vue-chart
chart-type="BarChart"
:columns="columns"
:rows="rows"
:options="options"
></vue-chart> -->
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      chartData: [],
      // chartData: [
      //   ['Year', 'Deaths'],
      //   ['1979', 300.0],
      //   ['1980', 1200.0],
      //   ['1981', 1500],
      //   ['1982', 2000],
      //   ['2014', 998],
      //   ['2015', 500],
      // ],
      chartOptions: {
        chart: {
          title: 'Suicides By Year',
        },
        hAxis: {
          title: 'Year'
        },
        vAxis: {
          title: 'Suicides'
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

// export default {
//   name: 'Graph',
//   data: function () {
//            return {
//                columns: [{
//                    'type': 'string',
//                    'label': 'Year'
//                }, {
//                    'type': 'number',
//                    'label': 'Suicide'
//                }],
//                rows: [
//                    ['2004', 1000],
//                    ['2005', 1170],
//                    ['2006', 660],
//                    ['2007', 1030]
//                ],
//                options: {
//                    title: 'Suicides by Year',
//                    hAxis: {
//                        title: 'Money',
//                        minValue: '2004',
//                        maxValue: '2007'
//                    },
//                    vAxis: {
//                        title: 'Year',
//                        minValue: 500,
//                        maxValue: 1200
//                    },
//                    width: 900,
//                    height: 500,
//                }
//            }
//        },
// };
</script>

<style>
.center {
  text-align: center;
}

header {
  margin-top: 50px;
}
</style>
