<template>
  <section>

    <header class='center'>
      <h1 class='font'>Focus on U.S. Suicide Data</h1>
    </header>

    <main class='font'>
      <h2 class='center font'>Number of Suicides by age</h2>

      <div class='age_div'>

        <div>
          <h4 class='center'>Combined</h4>
          <ul>
            <li>5-14: </li>
            <li>15-24: </li>
            <li>25-34: </li>
            <li>35-54: </li>
            <li>55-74: </li>
            <li>75+: </li>
          </ul>
        </div>

        <div>
          <h4 class='center'>Male</h4>
          <ul>
            <li>5-14: </li>
            <li>15-24: </li>
            <li>25-34: </li>
            <li>35-54: </li>
            <li>55-74: </li>
            <li>75+: </li>
          </ul>
        </div>

        <div>
          <h4 class='center'>Female</h4>
          <ul>
            <li>5-14: </li>
            <li>15-24: </li>
            <li>25-34: </li>
            <li>35-54: </li>
            <li>55-74: </li>
            <li>75+: </li>
          </ul>
        </div>

      </div>

    </main>

  </section>
</template>

<script>
export default {
  name: 'SectionFour',
};
</script>

<style scoped>
.center {
  text-align: center;
}

.font {
  font-family: 'Thasadith', sans-serif;
}

.age_div {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 2em;
  border: 2px solid black;
}


</style>
