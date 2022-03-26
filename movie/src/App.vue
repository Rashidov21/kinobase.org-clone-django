<template>
  <div id="app">
    <nav>
      <Nav/>
    </nav>
    <router-view/>
    <Footer/>
  </div>
</template>

<script>
import Nav from './components/Nav';
import Footer from './components/Footer';
export default {
  components:{
    Nav,
    Footer
  }
}
</script>
<style>
@import "assets/css/bootstrap.css";
@import "assets/css/font-awesome.css";
@import "assets/css/style.css";
  
</style>

