<template>
  <section>

    <header class='center'>
      <h1 class='font'>Focus on U.S. Suicide Data</h1>
    </header>

    <main class='font'>

      <h2 class='center font'>Number of Suicides by Age Group</h2>

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


      <h2 class='center'>Quick Summary of Age Groups</h2>
      <div class='age_group_summary'>
        <p>
          I wanted to take this time to briefly talk about the above data. One thing
          that instantly jumps out at me is that fact that in all three columns,
          the age group with the most number of suicides is the 35-54 years group. It
          does not matter if male or female, this is the most leathal age group to be
          in regards to suicide.
        </p>

        <p>
          A second factor that can really jump out at you is that the number of
          males committing suicide is always way higher. The question would be why?
          Could it be because of how much males are seen as the main 'bread winner'
          in modern American society? It could also be argued that males also have
          less of a role in society. Something that we will look at on the graph
          page.
        </p>
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
    };
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
  font-size: 20px;
}

.age_div {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 2em;
  border: 2px solid black;
}

.age_group_summary {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 3em;
}

span {
  font-weight: bold;
}


</style>
