<template>
<div id="app" style="margin-top:10px">
 <h3>Calculo de barras a compresión</h3>
 <div class="supizq">
    <form @submit.prevent="getPandeoCompresion">
      <p>Selección del tipo de acero y coeficiente:</p>
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
    <p> Selección del perfil:</p>
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
    <p> Introduzca L() m:</p>
    <input placeholder="L() m " v-model="selected.L">
    <p> Introduzca βy y βz:</p>
    <input placeholder="βy" v-model="selected.By">
    <input placeholder="βz" v-model="selected.Bz">
    <p> Introduzca NEd:</p>
    <input placeholder="NEd" v-model="selected.resNecN">
    <p>
    <button id="button-1" type="submit" v-on:click="oculto = true" variant="dark">Resolver directamente</button>
    </p>
    </form>
 </div>
<div class="supder">
  <h4 class="titulo">Desarrollo paso a paso</h4>
{{nextPaso["texto"]}}
{{nextPaso["formula0"]}}
{{nextPaso["resultado01"]}}{{nextPaso["resultado0"]}}
{{nextPaso["formula1"]}}
{{nextPaso["resultado11"]}}{{nextPaso["resultado1"]}}
<button id="button2" type="submit" v-show="ocultar" v-on:click="getPasoSiguiente()" variant="dark">Siguiente paso</button>
</div>
<p></p>
<div class="abajo">
  <p></p>
    <table class = "table" id="tablaContenido">
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
                <td>{{pandeo["0"]}}</td>
                <td>{{pandeo["2"]}}</td>
                <td>{{pandeo["4"]}}</td>
                <td>{{pandeo["6"]}}</td>
                <td>{{pandeo["8"]}}</td>
                <td>{{pandeo["10"]}}</td>
                <td>{{pandeo["12"]}}</td>
                <td>{{pandeo["14"]}}</td>
            </tr>
            <tr>
                <td>Eje Z</td>
                <td>{{pandeo["1"]}}</td>
                <td>{{pandeo["3"]}}</td>
                <td>{{pandeo["5"]}}</td>
                <td>{{pandeo["7"]}}</td>
                <td>{{pandeo["9"]}}</td>
                <td>{{pandeo["11"]}}</td>
                <td>{{pandeo["13"]}}</td>
                <td>{{pandeo["15"]}}</td>
            </tr>
        </tbody>
    </table>
  </div>
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
      excel: {},
      nextPaso: [],
      paso: 0,
      contadorElementos: 0,
      ocultar: true
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
          this.nextPaso['texto'] = 'El primer paso seria seleccionar en los desplegables el tipo de acero y su coeficiente.\n' +
          'Además, se deberá indicar con que perfil se desea realizar los cálculos.\n' +
          'A continuación, para los cálculos necesarios relacionados con el pandeo de compresión necesitaras introducir el valor de L() en metros y los valores de βy y βz respectivamente.\n' +
          'Por último, se deberá introducir también el valor de NEd para cálculos posteriores.'
        })
        .catch(err => {
          console.log(err)
        })
      return false
    },
    getPasoSiguiente: function () {
      const path = 'http://127.0.0.1:5000/PanCom' + this.paso
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
          this.nextPaso = body.data
          this.paso = this.paso + 1
        })
        .catch(err => {
          console.log(err)
        })
      if (this.paso === 7) {
        this.ocultar = false
      } else {
        this.ocultar = true
      }
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
    font-size: 1rem;
    margin-left: auto;
    margin-right: auto;
    border-spacing:2cm;
    border: 1px solid;
}
.supizq{
    float: left;
    width: 40%;
    text-align: left;
    margin-left: 30px;
}
.supder{
    float: left;
    width: 50%;
    text-align: left;
    white-space:pre-line;
}
.abajo{
  float: left;
  width: 100%;
}
.titulo{
  text-align: center;
  margin-top: 0px;
  margin-bottom: 0px;
}
</style>
