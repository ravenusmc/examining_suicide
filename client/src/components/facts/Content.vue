<template>
  <div class='content_area'>

    <h1 class='font center'>Examining The Data</h1>

    <section class='section_one'>

      <div>
        <p class='font'>
          This page is about letting the user look at some of the data statistics
          such as find the mean in some data or some other basic statistics. Yes,
          compared to the graph page, this page me be quite boring. So, if you want
          to see some excitement head on over to the graph page. Other than that,
          I'll put some photo's on this page to help liven it up.
        </p>

        <p class='font'>
          The first data that we can look at is suicide by country. Simply choose
          a country over to the right and when you submit it, the number of suicides
          that occured in that country will come back. I will say thought that the
          WHO data does not all start at the same year. I know that Albania's starts
          in 1985 while the U.S's data starts in 1979.
        </p>
      </div>

      <div class='by_country'>
        <ByCountry></ByCountry>
      </div>

    </section>

    <SectionTwo></SectionTwo>

    <hr>

    <SectionThree></SectionThree>

    <SectionFour></SectionFour>

  </div>
</template>

<script>

import ByCountry from './Calls/By_Country';
import SectionTwo from './Calls/Section_Two';
import SectionThree from './Calls/Section_Three';
import SectionFour from './Calls/Section_Four';
import SectionFive from './Calls/Section_Five';

export default {
  name: 'Content',
  data() {
    return {
      msg: '',
      country: '',

    }
  },
  components: {
    ByCountry,
    SectionTwo,
    SectionThree,
    SectionFour,
    SectionFive
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

.content_area {
  margin-top: 25px;
  margin-left: 5%;
  margin-right: 5%;
}

/* CSS for section one */
.section_one {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
}

.by_country {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* CSS for section two */
.section_two {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
}

</style>
