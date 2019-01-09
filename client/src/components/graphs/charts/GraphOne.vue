<template>
  <div>
    <div class='first_chart'>
      
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
           This first chart shows the total number of suicides for the world. What
           I first want to point out is that the dip in 1983 is not caused by a
           sudden drop of suicides world wide. Instead, its a drop from the fact that
           the WHO has no data from the Soviet Block during that year. Also, the large
           drop off of suicides in 2016 is not because suicide is going away. I believe
           it's because of lack of reporting to the WHO. Another fact that I'd like
           to point out is that there does seem to be a slight up tick in suicides right
           after the 2008 recession. Finally, I would like to again say that I'm
           not 100% sure how good the data is. I believe that the counts themselves are
           right but some countries appear to not be reporting some years. This could
           drastically disrupt the data.
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
  name: 'GraphOne',
  data () {
    return {
      chartData: [],
      chartOptions: {
        height: 500,
        title: 'Total Suicides By Year (World)',
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
    const path = 'http://localhost:5000/build_total_suicides_graph';
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

header {
  margin-top: 50px;
}

.first_chart {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 1em;
  margin-left: 5%;
  margin-right: 5%;
}

.first_chart_paragraph {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-right: 30px;
}

</style>
