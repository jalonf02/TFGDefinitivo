<template>
<div id="app">

 <h3>Calculo de Resistencias</h3>
    <form @submit="submit">
  
    <select v-model="selected.name">
      <option disabled value="">Seleccione un elemento</option>
      <option>IPE 200</option>
      <option>IPE 400</option>
      <option>IPE 600</option>
    </select>
    
    <button @click="submit" id="button-1" type="submit" variant="dark">Submit</button>
     
  </form>
    <p>Valor: {{ selected.name }}</p>

</div>

</template>
<script>
import axios from 'axios';
export default{
 
  data(){
    return {
       selected:{
        name:"",
      },
    };
  },
  methods:{
    submit:function(){
      const path = 'http://127.0.0.1:5000/dataentry'
      axios.post(path, {
        name:this.selected.name,
        }
      )
      .then(response => {
        console.log(response);
      })
      .catch(err =>{
        console.log(err);
      });
    },
  }
}
</script>

