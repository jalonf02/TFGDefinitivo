<template>
  <div id="app" style="margin-top: 0px">
    <div class = "superior">
    <h3>Calculo de resistencias en tipos de acero</h3>
    <div class="supizq">
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
            selected.resN < resistencias['Resistencia N'] ? 'color: red' : ''
          "
          v-model="selected.resN"
          placeholder="Resistencia N"
        />
        <select v-model="selected.claseN">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
        </select>
        <input
          v-model="selected.resMy"
          placeholder="Resistencia My"
        />
        <select v-model="selected.claseMy">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
        </select>
        <input
          v-model="selected.resMz"
          placeholder="Resistencia Mz"
        />
        <select v-model="selected.claseMz">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
        </select>
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
          v-model="selected.resVy"
          placeholder="VyEd"
        />
        <input
          v-model="selected.resVz"
          placeholder="VzEd"
        />
        <button
          id="button-3"
          type="button"
          v-on:click="cambioInformacion3()"
          variant="dark"
        >
          Iniciar
        </button>
      </form>
    </div>
    <div class="formulas">
      <img
        id="imagenPaso3"
        src='../assets/CurvaPandeo.png'
        v-show="this.paso===4"
        class="curvaPandeo"
      />
      <br>
      <img
        id="imagenPaso0"
        src='../assets/CalculoFyD.png'
        v-show="pantallaInicial"
        class="imagen"
      />
      <img
        id="imagenPaso0"
        src='../assets/CalculoLk.png'
        v-if="hover0 && this.paso!==1 || this.paso===1"
        class="imagen"
      />
      <img
        id="imagenPaso1"
        src='../assets/CalculoLambda.png'
        v-if="hover1 && this.paso!==2 || this.paso===2"
        class="imagen"
      />
      <img
        id="imagenPaso2"
        src='../assets/CalculoLambdaRed.png'
        v-if="hover2 && this.paso!==3 || this.paso===3"
        class="imagen"
      />
      <img
        id="imagenPaso4"
        src='../assets/CalcularChi.png'
        v-if="hover4 && this.paso!==5 || this.paso===5"
        class="imagen2"
      />
      <img
        id="imagenPaso5"
        src='../assets/CalculoNbrd.png'
        v-if="hover5 && this.paso!==6 || this.paso===6"
        class="imagen"
      />
      <img
        id="imagenPaso6"
        src='../assets/CalculoInteraccion.png'
        v-if="hover6 && this.paso!==7 || this.paso===7"
        class="imagen"
      />
    </div>
    <div class="centro">
      <h4 class="titulo">Desarrollo paso a paso</h4>
      {{ nextPaso["texto"] }}
      {{ nextPaso["resultado0"] }}
      <br/>
      <button
        id="button4"
        type="button"
        v-show="ocultar2"
        v-on:click="getPasoAnterior()"
        variant="dark"
        class="botton"
      >
      Anterior
      </button>
      <button
        id="button2"
        type="button"
        v-show="ocultar"
        v-on:click="getPasoSiguiente()"
        variant="dark"
        class="boton"
      >
        Siguiente
      </button>
    </div>
    </div>
    <div class="abajo">
      <p></p>
      <table class="table" id="tablaContenido">
        <thead>
          <tr>
            <th></th>
            <th @mouseover="hover0=true" @mouseleave="hover0 = false">N (kN)</th>
            <th @mouseover="hover1=true" @mouseleave="hover1 = false">My (kNm)</th>
            <th @mouseover="hover2=true" @mouseleave="hover2 = false">Mz (kNm)</th>
            <th @mouseover="hover3=true" @mouseleave="hover3 = false">Interaccion CTE</th>
            <th @mouseover="hover4=true" @mouseleave="hover4 = false">Interaccion EC-3</th>
            <th @mouseover="hover5=true" @mouseleave="hover5 = false">Vy (kN)</th>
            <th @mouseover="hover6=true" @mouseleave="hover6 = false">Vz (kN)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Ed=</td>
            <td>{{ selected.resN }}</td>
            <td>{{ selected.resMy }}</td>
            <td>{{ selected.resMz }}</td>
            <td>{{ resistencias[5] }}</td>
            <td>{{ resistencias[6] }}</td>
            <td>{{ selected.resVy }}</td>
            <td>{{ selected.resVz }}</td>
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
          <tr>
            <td>Clase</td>
            <td>{{ selected.claseN }}</td>
            <td>{{ selected.claseMy }}</td>
            <td>{{ selected.claseMz }}</td>
            <td>{{ selected.clase }}</td>
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
        clase: '',
        resN: '',
        resMy: '',
        resMz: '',
        Vy: '',
        Vz: '',
        claseN: '',
        claseMy: '',
        claseMz: ''
      },
      resistencias: [],
      excel: {},
      excel2: {},
      excel3: {},
      nextPaso: [],
      hover0: false,
      hover1: false,
      hover2: false,
      hover3: false,
      hover4: false,
      hover5: false,
      hover6: false,
      paso: 0,
      contadorElementos: 0,
      informacionIntroducida: false,
      ocultar: false,
      ocultar2: false,
      informacionIntroducida2: false,
      informacionIntroducida3: false,
      datosIntroducidos: false,
      pantallaInicial: true
    }
  },
  methods: {
    cambioInformacion: function () {
      if (this.selected.name !== '' && this.selected.coeficiente !== '' && this.selected.tipoAcero !== '') {
        this.informacionIntroducida = true
        this.informacionIntroducida2 = true
        this.resistencias = ''
        this.pantallaIniciaul = false
        this.nextPaso['texto'] =
          'El tipo de acero seleccionado es ' +
          this.selected.tipoAcero +
          '.\n' +
          'El coeficiente seleccionado es ' +
          this.selected.coeficiente +
          '.\n' +
          'El perfil seleccionado es ' +
          this.selected.name +
          '.\n\n'
      }
      return false
    },
    cambioInformacion2: function () {
      if (this.selected.resN !== '' && this.selected.clase !== '' && this.selected.resMy !== '' && this.selected.resMz !== '') {
        this.informacionIntroducida2 = false
        this.informacionIntroducida3 = true
        this.paso = 0
        this.nextPaso['texto'] =
          'La longitud de barra seleccionada es L = '
      }
      return false
    },
    cambioInformacion3: function () {
      if (this.selected.resVy !== '' && this.selected.resVz !== '') {
        this.informacionIntroducida3 = false
        this.informacionIntroducida = false
        this.ocultar = true
        this.getResistencias()
        this.nextPaso['texto'] = 'Texto de prueba'
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
          resN: this.selected.resN,
          resMy: this.selected.resMy,
          resMz: this.selected.resMz,
          resVy: this.selected.resVy,
          resVz: this.selected.resVz
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
    },
    getPasoSiguiente: function () {
      console.log(this.paso)
      switch (this.paso) {
        case 0:
          this.nextPaso['resultado0'] = 'Lₖ para el eje y = ' + this.resistencias[0] + ' kN.'
          this.nextPaso['texto'] = 'Paso 1: \n\n'
          this.ocultar2 = false
          break
        case 1:
          this.nextPaso['resultado0'] = 'λmec para el eje y = ' + this.resistencias[1] + '.'
          this.nextPaso['texto'] = 'Paso 2: \n\n'
          this.ocultar2 = true
          break
        case 2:
          this.nextPaso['resultado0'] = 'λreducida para el eje y = ' + this.resistencias[2] + '.'
          this.nextPaso['texto'] = 'Paso 3: \n\n'
          break
        case 3:
          this.nextPaso['resultado0'] = 'La curva de pandeo para el eje y es: ' + this.resistencias[3] + '.'
          this.nextPaso['texto'] = 'Paso 4:\n\n'
          break
        case 4:
          this.nextPaso['resultado0'] = 'χ para el eje y = ' + this.resistencias[4] + '.'
          this.nextPaso['texto'] = 'Paso 5: \n\n'
          break
        case 5:
          this.nextPaso['resultado0'] = 'Nb,Rd para el eje y = ' + this.resistencias[5] + ' kN.'
          this.nextPaso['texto'] = 'Paso 6: \n\n'
          this.ocultar = true
          break
        case 6:
          this.nextPaso['resultado0'] = 'La interacción en el eje y = ' + this.resistencias[6] + '.'
          this.nextPaso['texto'] = 'Paso 7: \n\n'
          this.ocultar = false
          break
      }

      this.paso = this.paso + 1

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
    border-spacing:1cm;
    border: 1px solid;
}
.supizq{
    float: left;
    width: 25%;
    text-align: left;
    margin-left: 30px;
    height: 400px;
    background-color: aliceblue;
}
.abajo{
  margin-top: 0%;
  float: left;
  width: 100%;
  background-color: aliceblue;
}
.titulo{
  text-align: center;
  margin-top: 0px;
  margin-bottom: 0px;
}
.imagen{
  width: 160px;
  height: auto;
  margin-top: 10%;
  float: center;
}
.centro{
  white-space:pre-line;
  background-color: aliceblue;
  text-align:center;
  height: 400px;
  margin: 10px;
  text-align: justify;
}
.formulas{
  width: 30%;
  height: 400px;
  background-color: aliceblue;
  float: right;
}
.curvaPandeo{
  width: 420px;
}
.boton{
  float: right;
}
.superior{
  background-color:aliceblue;
}
</style>
