<template>
  <div id="app" style="margin-top: 10px">
    <h3>Calculo de resistencias en tipos de acero</h3>
    <div class="supizq" v-show="!datosIntroducidos">
      <form v-show="!informacionIntroducida">
        <p>Selección del tipo de acero y coeficiente:</p>
        <select v-model="selected.tipoAcero">
          <option disabled value="">Seleccione tipo de acero</option>
          <option v-bind:key="aux" v-for="aux in excel3['TiposAcero']">
            {{ aux }}
          </option>
        </select>
        <select v-model="selected.coeficiente">
          <option disabled value="">Seleccione el coeficiente</option>
          <option v-bind:key="aux2" v-for="aux2 in excel2['Coeficientes']">
            {{ aux2 }}
          </option>
        </select>
        <p>Selección del perfil:</p>
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
        <p></p>
        <button
          id="button-1"
          type="button"
          v-on:click="cambioInformacion()"
          variant="dark"
        >
          Introducir datos
        </button>
      </form>
      <p></p>
      <form v-show="informacionIntroducida2">
        <input
          v-bind:style="
            resN < resistencias['Resistencia N'] ? 'color: red' : ''
          "
          v-model="resN"
          placeholder="Resistencia N"
        />
        <select v-model="selected.clase">
          <option>1</option>
          <option>2</option>
          <option>3</option>
        </select>
        <button
          id="button-2"
          type="button"
          v-on:click="cambioInformacion2()"
          variant="dark"
        >
          Introducir Datos
        </button>
      </form>
      <form v-show="informacionIntroducida3">
        <input
          v-bind:style="
            resMy < resistencias['Resistencia My'] ? 'color: red' : ''
          "
          v-model="resMy"
          placeholder="Resistencia My"
        />
        <input
          v-bind:style="
            resMz < resistencias['Resistencia Mz'] ? 'color: red' : ''
          "
          v-model="resMz"
          placeholder="Resistencia Mz"
        />
        <button
          id="button-3"
          type="button"
          v-on:click="cambioInformacion3()"
          variant="dark"
        >
          Introducir datos
        </button>
      </form>
    </div>
    <div class="supder">
      <h4 class="titulo" v-show="ocultar">Desarrollo paso a paso</h4>
      {{ nextPaso["texto"] }}
      {{ nextPaso["formula0"] }}
      {{ nextPaso["resultado01"] }}{{ nextPaso["resultado0"] }}
      {{ nextPaso["formula1"] }}
      {{ nextPaso["resultado11"] }}{{ nextPaso["resultado1"] }}
      <button
        id="button4"
        type="submit"
        v-show="ocultar2"
        v-on:click="getPasoAnterior()"
        variant="dark"
      >
        Anterior
      </button>
      <button
        id="button2"
        type="submit"
        v-show="ocultar"
        v-on:click="getPasoSiguiente()"
        variant="dark"
      >
        Siguiente
      </button>
      <button id="button2" type="reset" v-show="ocultar" variant="dark">
        Introducir nuevos datos
      </button>
    </div>
    <div class="abajo">
      <button
        id="button4"
        type="submit"
        v-show="ocultar"
        v-on:click="getResistencias()"
        variant="dark"
      >
        Mostrar todos los resultados
      </button>
      <p></p>
      <table class="table" id="tablaContenido">
        <thead>
          <tr>
            <th></th>
            <th>N (kN)</th>
            <th>My (kNm)</th>
            <th>Mz (kNm)</th>
            <th>Interaccion CTE</th>
            <th>Interaccion EC-3</th>
            <th>Vz (kN)</th>
            <th>Vy (kN)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Ed=</td>
            <td>{{ resN }}</td>
            <td>{{ resMy }}</td>
            <td>{{ resMz }}</td>
            <td>{{ resistencias[5] }}</td>
            <td>{{ resistencias[6] }}</td>
            <td>{{ Vy }}</td>
            <td>{{ Vz }}</td>
          </tr>
          <tr>
            <td>Rd</td>
            <td>{{ resistencias[0] }}</td>
            <td>{{ resistencias[1] }}</td>
            <td>{{ resistencias[2] }}</td>
            <td></td>
            <td></td>
            <td>{{ resistencias[3] }}</td>
            <td>{{ resistencias[4] }}</td>
          </tr>
        </tbody>
      </table>
    </div>
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
        clase: ''
      },
      resistencias: [],
      excel: {},
      excel2: {},
      excel3: {},
      nextPaso: [],
      resN: '',
      resMy: '',
      resMz: '',
      paso: 0,
      contadorElementos: 0,
      informacionIntroducida: false,
      ocultar: false,
      ocultar2: false,
      informacionIntroducida2: false,
      informacionIntroducida3: false,
      datosIntroducidos: false
    }
  },
  methods: {
    cambioInformacion: function () {
      if (this.selected.name !== '' && this.selected.coeficiente !== '' && this.selected.tipoAcero !== '') {
        this.informacionIntroducida = true
        this.informacionIntroducida2 = true
        this.nextPaso['texto'] =
          'El tipo de acero seleccionado es ' +
          this.selected.tipoAcero +
          '.\n' +
          'El coeficiente seleccionado es ' +
          this.selected.coeficiente +
          '.\n' +
          'El perfil seleccionado es ' +
          this.selected.name +
          '.\n\n' +
          'Ahora, para el cálculo de pandeo de barras a compresión será necesario añadir los siguientes valores: \n\n' +
          'Primero, debemos introducir tanto la longitud de la barra (L) en metros.' +
          ' Además, serán necesarios los coeficientes β tanto para el eje y como  para el eje x.' +
          'Por último, se debe añadir el esfuerzo axil (NEd) en kN ya que será necesario para cáculos posteriores.'
      }
      return false
    },
    cambioInformacion2: function () {
      if (this.selected.resN !== '' && this.selected.clase !== '') {
        this.informacionIntroducida2 = false
        this.informacionIntroducida3 = true
        this.ocultar = true
        this.nextPaso['texto'] =
          'La longitud de barra seleccionada es L = ' +
          this.selected.L +
          ' m.\n' +
          'El coeficiente β seleccionado para el eje y es ' +
          this.selected.By +
          '.\n' +
          'El coeficiente β seleccionado para el eje z es ' +
          this.selected.Bz +
          '.\n' +
          'El esfuerzo axil seleccionado para el eje z es Ned = ' +
          this.selected.resNecN +
          'kN.\n\n' +
          'Ahora, para el cálculo de pandeo de barras a compresión será necesario añadir los siguientes valores: \n\n' +
          'Primero, debemos introducir tanto la longitud de la barra (L) en metros.' +
          'Además, serán necesarios los coeficientes β tanto para el eje x como  para el eje y.'
      }
      return false
    },
    getResistencias: function () {
      const path = 'http://127.0.0.1:5000/dataentry'
      axios
        .post(path, {
          name: this.selected.name,
          coeficiente: this.selected.coeficiente,
          tipoAcero: this.selected.tipoAcero,
          clase: this.selected.clase,
          resN: this.resN,
          resMy: this.resMy,
          resMz: this.resMz
        })
        .then((body) => {
          this.resistencias = body.data
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
      const path2 = 'http://127.0.0.1:5000/data2'
      axios
        .get(path2)
        .then((body) => {
          this.excel2 = body.data
        })
        .catch((err) => {
          console.log(err)
        })
      const path3 = 'http://127.0.0.1:5000/data3'
      axios
        .get(path3)
        .then((body) => {
          this.excel3 = body.data
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
  font-size: 1rem;
  margin-left: auto;
  margin-right: auto;
  border-spacing: 2cm;
  border: 1px solid;
}
.supizq {
  float: left;
  width: 40%;
  text-align: left;
  margin-left: 30px;
  height: 400px;
}
.supder {
  float: left;
  width: 54%;
  text-align: left;
  white-space: pre-line;
  height: 400px;
  margin-left: 30px;
}
.abajo {
  float: left;
  width: 100%;
}
.titulo {
  text-align: center;
  margin-top: 0px;
  margin-bottom: 0px;
}
</style>
