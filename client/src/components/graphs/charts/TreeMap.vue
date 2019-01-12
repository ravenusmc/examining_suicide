<template>
  <div>

    <div class='second_graph'>



      <md-card md-with-hover>
        <md-ripple>
          <md-card-content>
            <div id="viz"></div>
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
      .tooltip(true)
      .legend(false)
      .tooltipConfig({
        className: 'tree-tooltip',
        title: 'Suicides',
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

.tree-tooltip {
  z-index: 1000;
}

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
