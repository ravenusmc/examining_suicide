<template>
  <div>

    <h3 class='font'>Suicides by Country</h3>
    <form @submit="onSubmit">
      <select v-model="country" name="country">
        <option v-for="country in countries" :value="country">{{country}}</option>
      </select>
      <button type="submit" variant="primary">Submit</button>
      <p class='font'>The number of suicides in {{ country }} is: {{ msg }}</p>
    </form>

  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ByCountry',
  data() {
    return {
      msg: '',
      country: '',
      countries: ['Albania', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia',
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
                 'Virgin Islands (USA)', 'Zimbabwe'],
    }
  },
  methods: {
    getSuicideByCountry(payload) {
    const path = 'http://localhost:5000/suicides_by_country';
    axios.post(path, payload)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
            console.log(error);
            this.getMessage();
        });
      },
      onSubmit(evt) {
        evt.preventDefault();
        const payload = {
          country: this.country
        };
        this.getSuicideByCountry(payload);
      },
    },
  }
</script>

<style scoped>
.font {
  font-family: 'Thasadith', sans-serif;
}

button {
	border: none;
	background: #3a7999;
	color: #f2f2f2;
	padding: 10px;
	font-size: 18px;
	border-radius: 5px;
	position: relative;
	box-sizing: border-box;
	transition: all 500ms ease;
}

button:before {
	content:'';
	position: absolute;
	top: 0px;
	left: 0px;
	width: 100%;
	height: 0px;
	background: rgba(255,255,255,0.3);
	border-radius: 5px;
	transition: all 2s ease;
}


button:hover {
	background: rgba(0,0,0,0);
	color: #3a7999;
	box-shadow: inset 0 0 0 3px #3a7999;
}

button:hover:before {
	height: 42px;
}
</style>
