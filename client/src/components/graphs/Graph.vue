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
let countries = ['Albania', 'Anguilla', 'Antigua and Barbuda|', 'Argentina', 'Armenia',
  'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
  'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bermuda', 'Bolivia', 'Bosnia and Herzegovina',
  'Brazil', 'British Virgin Islands', 'Brunei Darussalam', 'Bulgaria',
  'Cabo Verde', 'Canada', 'Cayman Islands', 'Chile', 'Colombia', 'Costa Rica',
  'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark','Dominica',
  'Dominican Republic', 'Ecuador', 'Egypt','El Salvador','Estonia',
  'Falkland Islands (Malvinas)', 'Fiji', 'Finland', 'France', 'French Guiana',
  'Georgia', 'Germany', 'Greece', 'Grenada', 'Guadeloupe', 'Guatemala', 'Guyana',
  'Haiti', 'Honduras', 'Hong Kong SAR', 'Hungary', 'Iceland',
  'Iran (Islamic Rep of)', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica',
  'Japan', 'Jordan', 'Kazakhstan', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
  'Lithuania', 'Luxembourg', 'Macau', 'Malaysia', 'Maldives', 'Malta',
  'Martinique', 'Mauritius', 'Mayotte', 'Mexico', 'Monaco', 'Mongolia',
  'Montenegro', 'Montserrat', 'Morocco','Netherlands', 'Netherlands Antilles',
  'New Zealand', 'Nicaragua', 'Norway', 'Occupied Palestinian Territory',
  'Oman', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
  'Puerto Rico', 'Qatar', 'Republic of Korea', 'Republic of Moldova', 'Reunion',
  'Rodrigues', 'Romania', 'Russian Federation', 'Saint Kitts and Nevis',
  'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent and Grenadines',
  'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Serbia', 'Seychelles',
  'Singapore', 'Slovakia','Slovenia', 'South Africa', 'Spain', 'Sri Lanka',
  'Suriname', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'TFYR Macedonia',
  'Tajikistan', 'Thailand', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
  'Turkmenistan', 'Turks and Caicos Islands', 'Ukraine',
  'United Arab Emirates', 'United Kingdom', 'United States of America',
  'Uruguay', 'Uzbekistan', 'Venezuela (Bolivarian Republic of)',
  'Virgin Islands (USA)', 'Zimbabwe']

let test = [
    ['Saudi Arabia', 200],
    ['United States', 300],
    ['Brazil', 400],
    ['Canada', 700],
    ['France', 201]
]

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
            rows: test,
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
