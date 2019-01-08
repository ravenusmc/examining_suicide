<template>
  <div>

    <header class='center'>
      <h1 class='font title'>World Map</h1>
    </header>

    <div class='data_control_div'>
      <h3 class='font'>Year: {{ year }}</h3>
      <div class='button_div'>
        <md-button @click="increaseYear" class="md-raised md-primary">Increase Year</md-button>
        <md-button @click="decreaseYear" class="md-raised md-primary">Decrease Year</md-button>
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

<style scoped>
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


</style>
