<template>
  <div>

    <div :style="{backgroundImage:imageOne}" class='main_content_div'>

      <div @mouseover="changeImageOne" class='div_one'>
      </div>

      <div @mouseover="changeImageTwo" class='div_two'>
      </div>

      <div @mouseover="changeImageThree" class='div_three'>
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: 'Content',
  data() {
    return {
      imageOne: 'url(' + require('../../assets/images/water.jpg') + ')',
      imageTwo: 'url(' + require('../../assets/images/rope.jpg') + ')',
      imageThree: 'url(' + require('../../assets/images/window.jpg') + ')',
    }
  },
  methods: {
    changeImageOne() {
      this.imageOne = 'url(' + require('../../assets/images/rope.jpg') + ')'
    },
    changeImageTwo(){
      this.imageOne = 'url(' + require('../../assets/images/window.jpg') + ')'
    },
    changeImageThree(){
      this.imageOne = 'url(' + require('../../assets/images/water.jpg') + ')'
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
  border-right: 2px dotted white;
}

.div_two {
  border-right: 2px dotted white;
}

.div_three {
  /* border: 2px solid yellow; */
}
</style>
