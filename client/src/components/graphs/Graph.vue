<template>
  <div>
    <h1>Graph Page</h1>
    <!-- <vue-chart
    chart-type="BarChart"
    :columns="columns"
    :rows="rows"
    :options="options"
></vue-chart> -->
<vue-chart
    chart-type="GeoChart"
    :columns="columns"
    :rows="rows"
    :options="options"
></vue-chart>
  </div>

</template>
<script>
export default {
    data: function () {
        return {
            columns: [{
                'type': 'string',
                'label': 'Country'
            }, {
                'type': 'number',
                'label': 'Suicides'
            }],
            rows: [
                ['Albania', 200],
                ['United States', 300],
                ['Brazil', 400],
                ['Canada', 700],
                ['France', 201]
            ],
            options: {
                title: 'Suicide by Countries',
                width: 900,
                height: 500,
            }
        }
    },
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
</style>
