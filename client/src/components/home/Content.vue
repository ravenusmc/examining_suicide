<template>
  <div>

    <div :style="{backgroundImage:'url(' + require('../../assets/images/water.jpg') + ')' }" class='main_content_div'>

      <div @mouseover="changeImageOne" class='div_one'>
      </div>

      <div class='div_two'>
      </div>

      <div class='div_three'>
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: 'Content',
  data: {},
  methods: {
    changeImageOne() {
      alert('Hi');
    },
  },
};
</script>

<style>
.main_content_div {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  height: 800px;
  /* background-image: url('../../assets/images/water.jpg'); */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.div_one {
  border: 2px solid yellow;
}

.div_two {
  border: 2px solid red;
}

.div_three {
  border: 2px solid yellow;
}
</style>
