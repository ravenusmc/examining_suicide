<template>
  <div class='content_area'>

    <p>This page is about letting the user look at some of the data statistics
      such as find the mean in some data or some other basic statistics. Yes,
      compared to the graph page, this page me be quite boring. So, if you want
      to see some excitement head on over to the graph page. Other than that,
      I'll put some photo's on this page to help liven it up.
    </p>

    <p>Data Area 1: </p>
    <form @submit="onSubmit">
      <input
                   type="text"
                   v-model="country"
                   required
                   placeholder="Enter Country"></b-form-input>
      <button type="submit" variant="primary">Submit</button>
      <p>{{ msg }}</p>
    </form>
    <button type="button" @click="getMessage" class="btn btn-primary">Press Me</button>


  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Content',
  data() {
    return {
      msg: '',
      country: '',
    }
  },
  methods: {
  getMessage() {
    const path = 'http://localhost:5000/suicides_by_country';
    axios.get(path)
      .then((res) => {
        this.msg = res.data;
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getSuicideByCountry(payload) {
  const path = 'http://localhost:5000/suicides_by_country';
  axios.post(path, payload)
      // .then(() => {
      //     this.getMessage();
      // })
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
};

</script>

<style scoped>

.content_area {
  margin-left: 5%;
  margin-right: 5%;
  border: 2px solid black;
}

</style>
