<template>
  <div id="app">
    <h3>Calculo de Pandeo Lateral</h3>
    <form @submit.prevent="getPandeoLateral">
      <select v-model="selected.tipo">
        <option disabled value="">Seleccione un elemento</option>
        <option v-bind:key="tipo" v-for="tipo in excel['Tipos']">
          {{ tipo }}
        </option>
      </select>
      <select id="tipos" v-model="selected.name">
        <option disabled value="">Seleccione un elemento</option>
        <option v-bind:key="datos" v-for="datos in excel[selected.tipo]">
          {{ datos }}
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
      <select v-model="selected.K2">
        <option>0.7</option>
        <option>1</option>
        <option>1.3</option>
      </select>
      <p>
        <input placeholder="Resistencia N deseada" v-model="selected.resNecN" />
        <input placeholder="L() m " v-model="selected.L" />
        <input placeholder="C₁" v-model="selected.C1" />
        <input placeholder="βₗₜ" v-model="selected.Blt" />
        <input placeholder="E (GPa)" v-model="selected.E" />
        <input placeholder="G (GPa)" v-model="selected.G" />
      </p>
      <p>
        <button id="button-1" type="submit" variant="dark">
          Calcular PandeoLateral
        </button>
      </p>
    </form>
    <table class="table">
      <thead>
        <tr>
          <th>MLTw</th>
          <th>Mltv</th>
          <th>Mcr</th>
          <th>λLT</th>
          <th>Φ</th>
          <th>Xₗₜ</th>
          <th>MbRd</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ pandeo["Mltw"] }}</td>
          <td>{{ pandeo["Mltv"] }}</td>
          <td>{{ pandeo["Mcr"] }}</td>
          <td>{{ pandeo["Esblt"] }}</td>
          <td>{{ pandeo["fi"] }}</td>
          <td>{{ pandeo["xlt"] }}</td>
          <td>{{ pandeo["MbRd"] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      selected: {
        name: '',
        tipo: '',
        coeficiente: '',
        tipoAcero: '',
        resNecN: '',
        L: '',
        C1: '',
        Blt: '',
        K2: '',
        E: '',
        G: ''
      },
      pandeo: [],
      excel: {}
    }
  },
  methods: {
    getPandeoLateral: function () {
      const path = 'http://127.0.0.1:5000/PandeoLateral'
      axios
        .post(path, {
          name: this.selected.name,
          coeficiente: this.selected.coeficiente,
          tipoAcero: this.selected.tipoAcero,
          resNecN: this.selected.resNecN,
          L: this.selected.L,
          C1: this.selected.C1,
          Blt: this.selected.Blt,
          K2: this.selected.K2,
          E: this.selected.E,
          G: this.selected.G
        })
        .then((body) => {
          this.pandeo = body.data
        })
        .catch((err) => {
          console.log(err)
        })
      return false
    },
    getExcel: function () {
      const path = 'http://127.0.0.1:5000/data'
      axios
        .get(path)
        .then((body) => {
          this.excel = body.data
        })
        .catch((err) => {
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
.app {
  text-align: center;
  align-content: center;
}
.table {
  font-size: 1.5rem;
  margin-left: auto;
  margin-right: auto;
  border-spacing: 2cm;
  border: 1px solid;
}
</style>
