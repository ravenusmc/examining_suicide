<template>
  <div>
    <header>
      <div class='title_div'>
        <h1>Learning About Suicide</h1>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style>
header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 500px;
  background-image: url('../../assets/images/cliff.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.title_div {
  padding: 15px;
  border: 2px solid white;
  border-radius: 12px;
  background-color: rgba(0, 0, 0, 0.7);
}
</style>
