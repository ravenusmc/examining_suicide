<template>
  <div>

    <header class='center'>
      <h1 class='font title'>World Map</h1>
    </header>

    <div class='data_control_div'>
      <h3 class='font'>Year: {{ year }}</h3>
      <div class='button_div'>
        <button @click="increaseYear">Increase Year</button>
        <button @click="decreaseYear">Decrease Year</button>
      </div>
    </div>
    <p>{{msg}}</p>

    <div class='map_div'>
      <vue-chart
          chart-type="GeoChart"
          :columns="columns"
          :rows="rows"
          :options="options"></vue-chart>
    </div>

  </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            msg: '',
            year: 1979,
            columns: [{
                'type': 'string',
                'label': 'Country'
            }, {
                'type': 'number',
                'label': 'Suicides'
            }],
            rows: [],
            options: {
                title: 'Suicide by Countries',
                width: 900,
                height: 500,
            }
        }
    }, //End of data object.
    methods: {
      getMapData(payload){
        const path = 'http://localhost:5000/build_world_map';
        axios.post(path, payload)
            .then((res) => {
              this.rows = res.data;
            })
            .catch((error) => {
                console.log(error);
                this.getMessage();
            });
      },
      increaseYear(evt){
        if (this.year > 2015){
          alert("There is no Data past 2016")
        }else {
          this.year++
          evt.preventDefault();
          const payload = {
            year: this.year
          };
          this.getMapData(payload);
        }
      },
      decreaseYear(evt) {
        if (this.year < 1980){
          alert('Data cannot go less than 1979')
        }else {
          this.year--
          evt.preventDefault();
          const payload = {
            year: this.year
          };
          this.getMapData(payload);
        }
      },
    },//End of methods
    mounted(){
      const path = 'http://localhost:5000/build_world_map';
      axios.get(path)
        .then((res) => {
          this.rows = res.data;
          console.log(combined)
        })
        .catch((error) => {
          console.log(error);
        });
    },//End of mounted call
}

</script>
<style>
.center {
  text-align: center;
}

header {
  margin-top: 50px;
}

.font {
  font-family: 'Anton', sans-serif;
  font-size: 20px;
}

.data_control_div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.button_div {
  display: flex;
  flex-direction: row;
  padding: 10px;
}

.map_div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* CSS for the button */
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
  margin-right: 20px;
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
