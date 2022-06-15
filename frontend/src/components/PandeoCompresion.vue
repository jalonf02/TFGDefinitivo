<template>
<div id="app">
 <h3>Calculo de barras a compresión</h3>
    <form @submit.prevent="getPandeoCompresion">
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
    <p>
    <input placeholder="Resistencia N deseada" v-model="selected.resNecN">
    <input placeholder="L() m " v-model="selected.L">
    <input placeholder="βy" v-model="selected.By">
    <input placeholder="βz" v-model="selected.Bz">
    </p>
    <p>
    <button id="button-1" type="submit" variant="dark">Calcular PandeoLateral</button>
    </p>
    </form>
    <table class = "table">
        <thead>
            <tr>
                <th></th>
                <th>Lₖ (mm)</th>
                <th>λmec</th>
                <th>λreducida</th>
                <th>curva</th>
                <th>X</th>
                <th>Ncr</th>
                <th>Nb,Rd</th>
                <th>interac.</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Eje Y</td>
                <td>{{pandeo["Lky"]}}</td>
                <td>{{pandeo["lambday"]}}</td>
                <td>{{pandeo["lamRedY"]}}</td>
                <td>{{pandeo["curvaY"]}}</td>
                <td>{{pandeo["xy"]}}</td>
                <td>{{pandeo["Ncry"]}}</td>
                <td>{{pandeo["Nbdrdy"]}}</td>
                <td>{{pandeo["interaccion y"]}}</td>
            </tr>
            <tr>
                <td>Eje Z</td>
                <td>{{pandeo["Lkz"]}}</td>
                <td>{{pandeo["lambdaz"]}}</td>
                <td>{{pandeo["lamRedZ"]}}</td>
                <td>{{pandeo["curvaZ"]}}</td>
                <td>{{pandeo["xz"]}}</td>
                <td>{{pandeo["Ncrz"]}}</td>
                <td>{{pandeo["Nbdrdz"]}}</td>
                <td>{{pandeo["interaccion z"]}}</td>
            </tr>
        </tbody>
    </table>
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
        tipoAcero: '',
        resNecN: '',
        L: '',
        By: '',
        Bz: ''
      },
      pandeo: [],
      excel: {}
    }
  },
  methods: {
    getPandeoCompresion: function () {
      const path = 'http://127.0.0.1:5000/PandeoCompresion'
      axios.post(path, {
        name: this.selected.name,
        coeficiente: this.selected.coeficiente,
        tipoAcero: this.selected.tipoAcero,
        resNecN: this.selected.resNecN,
        L: this.selected.L,
        By: this.selected.By,
        Bz: this.selected.Bz
      }
      )
        .then(body => {
          this.pandeo = body.data
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

<style scoped>
.app{
    text-align: center;
    align-content: center;
}
.table{
    font-size: 1.5rem;
    margin-left: auto;
    margin-right: auto;
    border-spacing:2cm;
    border: 1px solid;
}
</style>
