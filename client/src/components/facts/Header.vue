<template>
  <div>

    <header>
      <div class='header_div'>
        <h1 class='font'>Data Facts</h1>
      </div>
    </header>

  </div>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style scoped>
.font {
  font-family: 'Thasadith', sans-serif;
  color: white;
}

header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-image: url(../../assets/images/window_face.jpg);
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  text-align: center;
  height: 600px;
}

.header_div {
  border: 2px solid white;
  background-color: rgba(255, 0, 0, 0.3);
  padding: 12px;
  border-radius: 15px;
}

</style>
