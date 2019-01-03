<template>
  <div>
    <h1>Graph Page</h1>
    <vue-chart
    chart-type="BarChart"
    :columns="columns"
    :rows="rows"
    :options="options"
></vue-chart>
  </div>
</template>
<script>
export default {
  name: 'Graph',
  data: function () {
           return {
               columns: [{
                   'type': 'string',
                   'label': 'Year'
               }, {
                   'type': 'number',
                   'label': 'Sale'
               }],
               rows: [
                   ['2004', 1000],
                   ['2005', 1170],
                   ['2006', 660],
                   ['2007', 1030]
               ],
               options: {
                   title: 'Suicides by Year',
                   hAxis: {
                       title: 'Year',
                       minValue: '200',
                       maxValue: '2007'
                   },
                   vAxis: {
                       title: 'Money',
                       minValue: 300,
                       maxValue: 1200
                   },
                   width: 900,
                   height: 500,
                   curveType: 'function'
               }
           }
       },
};
</script>
<style>
</style>
