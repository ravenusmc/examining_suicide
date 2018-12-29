<template>
  <div>

    <div :style="{backgroundImage:imageOne}" class='main_content_div'>

      <div @mouseover="changeImageOne" class='div_one'>
        <div class='text_div'>
          <h4 class='font center'>What This Project Is:</h4>
          <p>This project uses data, from the World Health
            organization, to do some basic data analysis on data
            that deals with suicide. The project will allow a user
            to get some quick facts on the data as well as to look
            at somee graphs of the data.
          </p>
        </div>
      </div>

      <div @mouseover="changeImageTwo" class='div_two'>
        <div class='text_div'>
          <h4 class='font center'>What This Project Is Not:</h4>
          <p>This project uses data, from the World Health
            organization, to do some basic data analysis on data
            that deals with suicide. The project will allow a user
            to get some quick facts on the data as well as to look
            at somee graphs of the data.
          </p>
        </div>
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
    };
  },
  methods: {
    changeImageOne() {
      this.imageOne = 'url(' + require('../../assets/images/rope.jpg') + ')';
    },
    changeImageTwo() {
      this.imageOne = 'url(' + require('../../assets/images/window.jpg') + ')';
    },
    changeImageThree() {
      this.imageOne = 'url(' + require('../../assets/images/water.jpg') + ')';
    },
  },
};
</script>

<style>
.font {
  font-family: 'Thasadith', sans-serif;
}

.text_div {
  margin-top: 50px;
  background-color: rgba(255, 0, 0, 0.7);
  padding: 12px;
}

.center {
  text-align: center;
}

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
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.div_three {
  /* border: 2px solid yellow; */
}
</style>
