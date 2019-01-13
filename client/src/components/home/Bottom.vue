<template>
  <div class='main_div'>

    <!-- Start of Card One -->
    <md-card md-with-hover>
      <md-ripple>
        <md-card-header>
          <div class="md-title">Quick Facts</div>
        </md-card-header>

        <md-card-content>
          See some quick facts about the data pulling up information about suicides
          around the world
        </md-card-content>

        <md-card-actions>
          <md-button><router-link class='font_color' to="/fact">Quick Facts Page</router-link></md-button>
        </md-card-actions>
      </md-ripple>
    </md-card>
    <!-- End of Card One -->

    <!-- Start of Card Two -->
    <md-card md-with-hover>
      <md-ripple>
        <md-card-header>
          <div class="md-title">Graph Page</div>
        </md-card-header>

        <md-card-content>
          See graphs based on the data focusing on the U.S. There are line
          graphs and a treemap.
        </md-card-content>

        <md-card-actions>
          <md-button><router-link class="nav-link" to="/graphs">Graphs</router-link></md-button>
        </md-card-actions>
      </md-ripple>
    </md-card>
    <!-- End of Card Two -->

    <!-- Start of Card Three-->
    <md-card md-with-hover>
      <md-ripple>
        <md-card-header>
          <div class="md-title">World Map Page</div>
        </md-card-header>

        <md-card-content>
          See a map of the world that shows how many suicides occur in each country
          each year.
        </md-card-content>

        <md-card-actions>
          <md-button><router-link class='font_color' to="/world">World Map Page</router-link></md-button>
        </md-card-actions>
      </md-ripple>
    </md-card>
    <!-- End of Card Three -->

  </div>
</template>

<script>
export default {
  name: 'Bottom',
};
</script>

<style scoped>
.main_div {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 1.5em;
  height: 300px;
}

.font_color {
  color: #f2f2f2;
}

.font_color:hover {
  color: #3a7999;
}

button {
	border: none;
	background: #3a7999;
	color: #f2f2f2;
	padding: 10px;
	font-size: 18px;
	border-radius: 5px;
	position: relative;
	box-sizing: border-box;
	transition: all 500ms ease;
}

button:before {
	content:'';
	position: absolute;
	top: 0px;
	left: 0px;
	width: 100%;
	height: 0px;
	background: rgba(255,255,255,0.3);
	border-radius: 5px;
	transition: all 2s ease;
}


button:hover {
	background: rgba(0,0,0,0);
	color: #3a7999;
	box-shadow: inset 0 0 0 3px #3a7999;
}

button:hover:before {
	height: 42px;
}

</style>
