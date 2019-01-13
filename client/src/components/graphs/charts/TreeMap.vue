<template>
  <div>

    <div class='second_graph'>

      <md-card md-with-hover>
        <md-ripple>
          <md-card-content class='test'>
            <div class='test' id="viz"></div>
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
            I don't believe it's any surprise that a majority of the countries,
            on the tree map, are wealthier countries. I've heard how in developed
            countries the rate of suicide is higher. What really interest me is
            why the Ukraine is in the top 5. I believe that this should be looked
            at closer. Could it have something to do with being part of the Soviet
            Union and then the collapse of the Soviet Union in the late 80's and
            early 90's that Ukraine was not able to get back on its feet with the
            economy?
          </p>
         </md-card-content>
       </md-ripple>
     </md-card>

    </div>

  </div>
</template>

<script>
import axios from 'axios';

//This function will add commas to a number in javascript.
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

var data = [
  { id: "Russia", value: 1500992},
  { id: "U.S", value: 1201401},
  { id: "Japan", value: 937614 },
  { id: "France", value: 395500},
  { id: "Ukraine", value: 365170}
];

export default {
  name: 'TreeMap',
  data () {
    return {
      data: [
        { id: "Russia", value: 1500992},
        { id: "U.S", value: 1201401},
        { id: "Japan", value: 937614 },
        { id: "France", value: 395500},
        { id: "Ukraine", value: 365170}
      ]
    }
  },//End of data object
  mounted() {
    console.log(this.data[0].id)
    new d3plus.Treemap()
      .select("#viz")
      .data(this.data)
      .tooltipConfig({
        body: function(d) {
          var table = "<table class='tooltip-table'>";
          table += "<tr><td class='title'>Suicides:</td><td class='data'>" + numberWithCommas(d.value) + "</td></tr>";
          table += "</table>";
          return table;
        },
      })
      .groupBy(["id"])
      .sum("value")
      .render();
  }, //End of mounted
};
</script>

<style scoped>
#viz {
  height: 200px;
  width: 500px;
}

.tooltip-table {
  z-index: 100 !important;
}

/* .test {
  z-index: -10;
} */

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
