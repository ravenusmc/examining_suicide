<template>
  <div class='content_area'>

    <div>
      <p>This page is about letting the user look at some of the data statistics
        such as find the mean in some data or some other basic statistics. Yes,
        compared to the graph page, this page me be quite boring. So, if you want
        to see some excitement head on over to the graph page. Other than that,
        I'll put some photo's on this page to help liven it up.
      </p>
    </div>

    <ByCountry></ByCountry>

  </div>
</template>

<script>

import ByCountry from './Calls/By_Country';

export default {
  name: 'Content',
  data() {
    return {
      msg: '',
      country: '',
    }
  },
  components: {
    ByCountry
  },

};

</script>

<style scoped>

.content_area {
  margin-left: 5%;
  margin-right: 5%;
  border: 2px solid black;
}

</style>
