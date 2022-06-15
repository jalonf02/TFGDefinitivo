<template>
<div id="app">
 <h3>Calculo de resistencias en tipos de acero</h3>
    <form @submit.prevent="getResistencias">
    <select v-model="selected.tipo">
      <option disabled value="">Seleccione un elemento</option>
      <option v-bind:key="tipo" v-for="tipo in excel['Tipos']">
      {{tipo}}
      </option>
    </select>
    <select id="tipos" v-model="selected.name">
      <option disabled value="">Seleccione un elemento</option>
      <option v-bind:key="datos" v-for="datos in excel[selected.tipo]">
      {{datos}}
      </option>
    </select>
    <select v-model="selected.tipoAcero">
      <option>S235</option>
      <option>S275</option>
      <option>S355</option>
      <option>S450</option>
    </select>
    <select v-model="selected.coeficiente">
      <option>1</option>
      <option>1.05</option>
      <option>1.1</option>
      <option>1.25</option>
    </select>
    <p></p>
    <input v-bind:style="resN < resistencias['Resistencia N'] ? 'color: red':'' "  v-model="resN" placeholder="Resistencia N">
    <input v-bind:style="resMy < resistencias['Resistencia My'] ? 'color: red':'' " v-model="resMy" placeholder="Resistencia My">
    <input v-bind:style="resMz < resistencias['Resistencia Mz'] ? 'color: red':'' " v-model="resMz" placeholder="Resistencia Mz">
    <p>
    <button id="button-1" type="submit" variant="dark">Calcular resistencias</button>
    </p>
    </form>
    <p></p>
    <p></p>
    <p>Resistencia N: {{resistencias["Resistencia N"] }}</p>
    <p>Resistencia My: {{resistencias["Resistencia My"] }}</p>
    <p>Resistencia Mz: {{resistencias["Resistencia Mz"] }}</p>
</div>
</template>

<script>
import axios from 'axios'
export default{
  data () {
    return {
      selected: {
        name: '',
        tipo: '',
        coeficiente: '',
        tipoAcero: ''
      },
      resistencias: [],
      excel: {}
    }
  },
  methods: {
    getResistencias: function () {
      const path = 'http://127.0.0.1:5000/dataentry'
      axios.post(path, {
        name: this.selected.name,
        coeficiente: this.selected.coeficiente,
        tipoAcero: this.selected.tipoAcero
      }
      )
        .then(body => {
          this.resistencias = body.data
        })
        .catch(err => {
          console.log(err)
        })
      return false
    },
    getExcel: function () {
      const path = 'http://127.0.0.1:5000/data'
      axios.get(path)
        .then(body => {
          this.excel = body.data
        })
        .catch(err => {
          console.log(err)
        })
      return false
    }
  },
  beforeMount () {
    this.getExcel()
  }
}
</script>
