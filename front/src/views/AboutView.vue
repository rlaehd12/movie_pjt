<template>
  <div>

    <h1 @click="gettest">test</h1>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'TesT',
  methods:{
    gettest(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/',
      })
      .then((res)=>{
        console.log(res);
      })
      .catch((err)=>{
        console.log(err);
      })
    }
  }

}
</script>

<style>

</style>
