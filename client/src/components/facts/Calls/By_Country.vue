<template>
  <div>

    <h3>Suicides by Country</h3>
    <form @submit="onSubmit">
      <input type="text"
             v-model="country"
             required
             placeholder="Enter Country"></b-form-input>
      <button type="submit" variant="primary">Submit</button>
      <p>The number of suicides in {{ country }} is: {{ msg }}</p>
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

<style>
</style>
