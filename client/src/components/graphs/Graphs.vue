<template>
  <div>
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
                   'label': 'Suicide'
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
                       title: 'Money',
                       minValue: '2004',
                       maxValue: '2007'
                   },
                   vAxis: {
                       title: 'Year',
                       minValue: 500,
                       maxValue: 1200
                   },
                   width: 900,
                   height: 500,
               }
           }
       },
};
</script>

<style>
</style>
