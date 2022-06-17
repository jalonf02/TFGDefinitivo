<template>
<div id="app" style="margin-top:10px">
 <h3  @mouseover="hover = true" @mouseleave="hover = false">Calculo de pandeo de barras a compresión</h3>
 <div class="supizq" v-show="!datosIntroducidos">
    <form v-show="!informacionIntroducida">
      <p>Selección del tipo de acero y coeficiente:</p>
    <select v-model="selected.tipoAcero">
      <option disabled value="">Seleccione tipo de acero</option>
      <option v-bind:key="aux" v-for="aux in excel3['TiposAcero']">
      {{aux}}
      </option>
    </select>
    <select v-model="selected.coeficiente">
      <option disabled value="">Seleccione el coeficiente</option>
      <option v-bind:key="aux2" v-for="aux2 in excel2['Coeficientes']">
      {{aux2}}
      </option>
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
    <p></p>
    <button id="button-1" type="button" v-on:click="cambioInformacion()" variant="dark">Introducir datos</button>
    </form>
    <form v-show="informacionIntroducida2">
    <p> Introduzca L() m:</p>
    <input placeholder="L() m " v-model="selected.L">
    <p> Introduzca βy y βz:</p>
    <input placeholder="βy" v-model="selected.By">
    <input placeholder="βz" v-model="selected.Bz">
    <p> Introduzca NEd:</p>
    <input placeholder="NEd" v-model="selected.resNecN">
    <p>
    <button id="button-1" type="button" v-on:click="cambioInformacion2()" variant="dark">Introducir datos</button>
    </p>
    </form>
 </div>
<div class="supder">
  <h4 class="titulo" v-show="ocultar">Desarrollo paso a paso</h4>
{{nextPaso["texto"]}}
{{nextPaso["resultado01"]}}{{nextPaso["resultado0"]}}
{{nextPaso["resultado11"]}}{{nextPaso["resultado1"]}}
<button id="button4" type="submit" v-show="ocultar2" v-on:click="getPasoAnterior()" variant="dark">Anterior</button>
<button id="button2" type="submit" v-show="ocultar" v-on:click="getPasoSiguiente()" variant="dark">Siguiente</button>
<button id="button2" type="reset" v-show="ocultar" variant="dark">Introducir nuevos datos</button>
<img id="imagenPaso" src ="../assets/CalculoFyD.png" v-show="ocultar" class="imagen"/>
</div>
<p></p>
<div class="abajo">
  <button id="button3" type="submit" v-show="ocultar" v-on:click="getPandeoCompresion()" variant="dark">Mostrar todos los resultados</button>
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
                <td>{{pandeo[0]}}</td>
                <td>{{pandeo[2]}}</td>
                <td>{{pandeo[4]}}</td>
                <td>{{pandeo[6]}}</td>
                <td>{{pandeo[8]}}</td>
                <td>{{pandeo[10]}}</td>
                <td>{{pandeo[12]}}</td>
                <td>{{pandeo[14]}}</td>
            </tr>
            <tr>
                <td>Eje Z</td>
                <td>{{pandeo[1]}}</td>
                <td>{{pandeo[3]}}</td>
                <td>{{pandeo[5]}}</td>
                <td>{{pandeo[7]}}</td>
                <td>{{pandeo[9]}}</td>
                <td>{{pandeo[11]}}</td>
                <td>{{pandeo[13]}}</td>
                <td>{{pandeo[15]}}</td>
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
      hover: false,
      imagen: '',
      pandeo: [],
      excel: {},
      excel2: {},
      excel3: {},
      nextPaso: [],
      paso: 0,
      contadorElementos: 0,
      informacionIntroducida: false,
      ocultar: false,
      ocultar2: false,
      informacionIntroducida2: false,
      datosIntroducidos: false
    }
  },
  methods: {
    getImage: function () {
      return '../assets/' + this.imagen
    },
    getPasoAnterior: function () {
      if (this.selected.name !== '' && this.selected.coeficiente !== '' && this.selected.tipoAcero !== '') {
        this.paso = this.paso - 2
        this.contadorElementos = this.contadorElementos - 4
        this.getPasoSiguiente()
      }
      return false
    },
    cambioInformacion: function () {
      if (this.selected.name !== '' && this.selected.coeficiente !== '' && this.selected.tipoAcero !== '') {
        this.informacionIntroducida = true
        this.informacionIntroducida2 = true
        this.nextPaso['texto'] = 'El tipo de acero seleccionado es ' + this.selected.tipoAcero + '.\n' +
        'El coeficiente seleccionado es ' + this.selected.coeficiente + '.\n' +
        'El perfil seleccionado es ' + this.selected.name + '.\n\n' +
        'Ahora, para el cálculo de pandeo de barras a compresión será necesario añadir los siguientes valores: \n\n' +
        'Primero, debemos introducir tanto la longitud de la barra (L) en metros.' +
        ' Además, serán necesarios los coeficientes β tanto para el eje y como  para el eje x.' +
        'Por último, se debe añadir el esfuerzo axil (NEd) en kN ya que será necesario para cáculos posteriores.'
      }
      return false
    },
    cambioInformacion2: function () {
      if (this.selected.restNecN !== '' && this.selected.L !== '' && this.selected.By !== '' && this.selected.Bz !== '') {
        this.informacionIntroducida2 = false
        this.ocultar = true
        this.datosIntroducidos = true
        this.nextPaso['texto'] = 'La longitud de barra seleccionada es L = ' + this.selected.L + ' m.\n' +
        'El coeficiente β seleccionado para el eje y es ' + this.selected.By + '.\n' +
        'El coeficiente β seleccionado para el eje z es ' + this.selected.Bz + '.\n' +
        'El esfuerzo axil seleccionado para el eje z es Ned = ' + this.selected.resNecN + 'kN.\n\n' +
        'Ahora, para el cálculo de pandeo de barras a compresión será necesario añadir los siguientes valores: \n\n' +
        'Primero, debemos introducir tanto la longitud de la barra (L) en metros.' +
        'Además, serán necesarios los coeficientes β tanto para el eje x como  para el eje y.'
      }
      return false
    },
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
          'Además, se deberá indicar con que perfil se desea realizar los cálculos.\n'
        })
        .catch(err => {
          console.log(err)
        })
      const path2 = 'http://127.0.0.1:5000/data2'
      axios.get(path2)
        .then(body => {
          this.excel2 = body.data
        })
        .catch(err => {
          console.log(err)
        })
      const path3 = 'http://127.0.0.1:5000/data3'
      axios.get(path3)
        .then(body => {
          this.excel3 = body.data
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
          this.pandeo[this.contadorElementos] = this.nextPaso['resultado0']
          this.pandeo[this.contadorElementos + 1] = this.nextPaso['resultado1']
          this.contadorElementos = this.contadorElementos + 2
        })
        .catch(err => {
          console.log(err)
        })
      if (this.paso === 0) {
        this.ocultar2 = false
      } else {
        this.ocultar2 = true
      }
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
    height: 400px;
}
.supder{
    float: left;
    width: 54%;
    text-align: left;
    white-space:pre-line;
    height: 400px;
    margin-left: 30px;
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
.imagen{
  width: 100px;
  height: auto;
}
</style>
