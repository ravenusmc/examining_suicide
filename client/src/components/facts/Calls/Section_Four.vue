<template>
  <section>

    <header class='center'>
      <h1 class='font'>Focus on U.S. Suicide Data</h1>
    </header>

    <main class='font'>
      <h2 class='center font'>Number of Suicides by age</h2>

      <div class='age_div'>

        <div>
          <h4 class='center'>Combined</h4>
          <ul>
            <li v-for="(num,index) in combined"><span>{{ age_groups[index] }}:</span>  {{num}} Suicides</li>
          </ul>
        </div>

        <div>
          <h4 class='center'>Male</h4>
          <ul>
            <li v-for="(num,index) in male"><span>{{ age_groups[index] }}:</span>  {{num}} Suicides</li>
          </ul>
        </div>

        <div>
          <h4 class='center'>Female</h4>
          <ul>
            <li v-for="(num,index) in female"><span>{{ age_groups[index] }}:</span>  {{num}} Suicides</li>
          </ul>
        </div>

      </div>

    </main>

  </section>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SectionFour',
  data() {
    return {
      age_groups: ['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years'],
      combined: [],
      male: [],
      female: [],
    }
  },
  mounted() {
    const path = 'http://localhost:5000/suicides_by_age_combined';
    axios.get(path)
      .then((res) => {
        this.combined = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
    const path2 = 'http://localhost:5000/suicides_by_age_group_male';
    axios.get(path2)
      .then((res) => {
          this.male = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    const path3 = 'http://localhost:5000/suicides_by_age_group_female';
    axios.get(path3)
      .then((res) => {
          this.female = res.data;
      })
      .catch((error) => {
          console.log(error);
      });
  },
};
</script>

<style scoped>
.center {
  text-align: center;
}

.font {
  font-family: 'Thasadith', sans-serif;
}

.age_div {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 2em;
  border: 2px solid black;
}

span {
  font-weight: bold;
}


</style>
