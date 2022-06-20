<template>
  <div id="app" style="margin-top: 0px">
    <div class = "superior">
    <h3 style="margin-bottom: 0px;">Calculo de resistencias en tipos de acero</h3>
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
      <form v-show="informacionIntroducida2">
      <p>Introduzca el valor de k₂:</p>
      <select v-model="selected.K2">
        <option>0.7</option>
        <option>1</option>
        <option>1.3</option>
      </select>
      <p>Introduzca el valor de L en metros, por defecto será 1:</p>
        <input placeholder="L() m " v-model="selected.L" />
      <p>Introduzca el valor de C₁ deseado según la tabla:</p>
        <input placeholder="C₁" v-model="selected.C1" />
      <p>Introduzca el valor de βₗₜ, por defecto será 1:</p>
        <input placeholder="βₗₜ" v-model="selected.Blt" />
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
        <p>Introduzca Ned:</p>
        <input placeholder="Ned" v-model="selected.Ned" />
        <p>Introduzca Myed:</p>
        <input placeholder="Myed" v-model="selected.Myed" />
        <p>Seleccione la clase de flexocompresión según la tabla:</p>
        <select v-model="selected.clase">
          <option>1</option>
          <option>2</option>
          <option>3</option>
        </select>
      <p>
        <button
          id="button-3"
          type="button"
          v-on:click="cambioInformacion3()"
          variant="dark"
        >
          Iniciar
        </button>
      </p>
    </form>
    </div>
    <div class="formulas">
      <h4>Formulas:</h4>
      <img
          id="imagenPaso0"
          src="../assets/VistaPL/TablaC1.png"
          v-show="informacionIntroducida2"
          class = "tablaPerfiles"
        />
      <img
          id="TablaPerfiles"
          src="../assets/TablaPerfiles.png"
          v-show="informacionIntroducida3"
          class = "tablaPerfiles"
      />
      <img
        id="imagenPaso1"
        src='../assets/VistaPL/CalcularMcr.png'
        v-if="hover1 && this.paso!==2 || this.paso===2"
        class="imagen2"
      />
      <br>
      <img
        id="imagenPaso4"
        src='../assets/VistaPL/CalcularChi2.png'
        v-if="this.paso===5"
        class="imagen"
      />
      <img
        id="imagenPaso0"
        src='../assets/VistaPL/CalcularLc.png'
        v-if="hover0 && this.paso!==1 || this.paso===1"
        class="imagen"
      />
      <img
        id="imagenPaso1"
        src='../assets/VistaPL/TablaEG.png'
        v-if="hover1 && this.paso!==2 || this.paso===2"
      />
      <img
        id="imagenPaso2"
        src='../assets/VistaPL/CalcularEsbPandeoLateral.png'
        v-if="hover2 && this.paso!==3 || this.paso===3"
        class="imagen"
      />
      <img
        id="imagenPaso2"
        src='../assets/VistaPL/EleccionCurvaPandeo.png'
        v-if="this.paso===4"
      />
      <img
        id="imagenPaso4"
        src='../assets/CalcularChi.png'
        v-if="this.paso===5"
        class="imagen2"
      />
      <img
        id="imagenPaso5"
        src='../assets/VistaPL/CalcularMbrd.png'
        v-if="hover5 && this.paso!==6 || this.paso===6"
        class="imagen2"
      />
      <img
        id="imagenPaso6"
        src='../assets/VistaPL/InteraccionPandeoLateral.png'
        v-if="hover6 && this.paso!==7 || this.paso===7"
        class="imagen"
      />
      <img
        id="imagenPaso7"
        src='../assets/VistaPL/CalcularLcLim.png'
        v-if="this.paso===8"
        class="imagen2"
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
      <br/>
      <br/>
      <img
          id="imagenPaso0"
          src="../assets/TipoAcero.png"
          v-show="pantallaInicial"
          class = "imagen2"
        />
      <img
          id="imagenPaso0"
          src="../assets/VistaPL/TablaK2.png"
          v-show="informacionIntroducida2"
          class = "imagen2"
        />
    </div>
    </div>
    <div class="abajo">
    <table class="table">
      <thead>
        <tr>
          <th>Datos:</th>
          <th>L (m)</th>
          <th>βₗₜ</th>
          <th>Lc (m)</th>
          <th>Lc limite (m)</th>
          <th>C₁</th>
          <th>h/b</th>
          <th>αLT</th>
          <th>Curva</th>
        </tr>
        <tr>
          <td></td>
          <td>{{selected.L}}</td>
          <td>{{selected.Blt}}</td>
          <td>{{ pandeo[8] }}</td>
          <td>{{ pandeo[9] }}</td>
          <td>{{selected.C1}}</td>
          <td>{{ pandeo[10] }}</td>
          <td>{{ pandeo[11] }}</td>
          <td>{{ pandeo[12] }}</td>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Resultados:</th>
          <th>Mltw (kNm)</th>
          <th>Mltv (kNm)</th>
          <th>Mcr (kNm)</th>
          <th>λlt</th>
          <th>Φ</th>
          <th>χlt</th>
          <th>Mbrd (kNm)</th>
          <th>interac.</th>
        </tr>
        <tr>
          <td></td>
          <td>{{ pandeo[0] }}</td>
          <td>{{ pandeo[1] }}</td>
          <td>{{ pandeo[2] }}</td>
          <td>{{ pandeo[3] }}</td>
          <td>{{ pandeo[4] }}</td>
          <td>{{ pandeo[5] }}</td>
          <td>{{ pandeo[6] }}</td>
          <td>{{ pandeo[7]}}</td>
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
        Ned: '',
        L: '',
        C1: '',
        Blt: '',
        K2: '',
        clase: '',
        Myed: ''
      },
      pandeo: [],
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
        this.pantallaInicial = false
        this.ocultar = false
        this.ocultar2 = false
        this.paso = 0
        this.nextPaso['resultado0'] = ''
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
      if (this.selected.Blt !== '' && this.selected.L !== '' && this.selected.C1 !== '' && this.selected.K2 !== '') {
        this.informacionIntroducida2 = false
        this.informacionIntroducida3 = true
        this.nextPaso['texto'] =
          'La longitud de barra seleccionada es L = '
      }
      return false
    },
    cambioInformacion3: function () {
      if (this.selected.resN !== '' && this.selected.resMy !== '' && this.selected.clase !== '') {
        this.informacionIntroducida3 = false
        this.informacionIntroducida = false
        this.ocultar = true
        this.getPandeoLateral()
        this.nextPaso['texto'] = 'Texto de prueba'
      }
      return false
    },
    getPandeoLateral: function () {
      const path = 'http://127.0.0.1:5000/PandeoLateral'
      axios
        .post(path, {
          name: this.selected.name,
          coeficiente: this.selected.coeficiente,
          tipoAcero: this.selected.tipoAcero,
          Ned: this.selected.Ned,
          L: this.selected.L,
          clase: this.selected.clase,
          C1: this.selected.C1,
          Blt: this.selected.Blt,
          K2: this.selected.K2,
          Myed: this.selected.Myed
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
          this.nextPaso['texto'] = 'El primer paso seria seleccionar en los desplegables el tipo de acero y su coeficiente.\n\n' +
          'Además, se deberá indicar con que perfil se desea realizar los cálculos.\n\n' +
          'Si desea introducir valores decimales utilice el punto en lugar de la coma.'
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
      switch (this.paso) {
        case 0:
          this.nextPaso['resultado0'] = 'Lc = ' + this.pandeo[8] + ' m.'
          this.nextPaso['texto'] = 'Paso 1 Calcular Lc: \n\n' +
          'Para realizar este cálculo simplemente tenemos que seguir la formula, ya que L y βₗₜ son datos introducidos por el usuario.\n'
          this.ocultar2 = false
          break
        case 1:
          this.nextPaso['resultado0'] = 'Mcr = ' + this.pandeo[2] + ' kNm.'
          this.nextPaso['texto'] = 'Paso 2 Calcular momento crítico: \n\n' +
          'A continuación, para calcular el momento crítico, ya tenemos todos los datos necesarios.\n\n' +
          'El Lc ha sido calculado en el paso anterior. Además, E y G son datos que vienen dados por el acero y se muestran en la tabla en el apartado de las fórmulas.\n\n' +
          'Por otro lado, C₁ y k₂ vienen dados por el usuario, y el resto de datos son datos propios del perfil ' + this.selected.name +
          '.\n\nPor lo tanto, ya podemos aplicar la fórmula y calcular.\n'
          this.ocultar2 = true
          break
        case 2:
          this.nextPaso['resultado0'] = 'λlt = ' + this.pandeo[3] + '.'
          this.nextPaso['texto'] = 'Paso 3 Calcular esbeltez a PL: \n\n' +
          'Después de calcular el momento crítico podemos calcular la esbeltez. Para ello será necesario utilizar el Fy que viene dado por nuestro tipo de acero, ' +
          'en este caso ' + this.selected.tipoAcero + ', y la Wy la obtendríamos de la tabla de nuestro perfil.\n'
          break
        case 3:
          this.nextPaso['resultado0'] = 'Curva = ' + this.pandeo[12] + '.'
          this.nextPaso['texto'] = 'Paso 4 Curva de pandeo lateral: \n\n' +
          'La curva viene determinada por h/b, que a su vez también determina αLT.\n\n' +
          'Como h/b = ' + this.pandeo[10] + '.\n\n' +
          'Esto significa que αLT = ' + this.pandeo[11] + '.\n'
          break
        case 4:
          this.nextPaso['resultado0'] = 'χlt = ' + this.pandeo[5] + '.'
          this.nextPaso['texto'] = 'Paso 5 Calcular χlt:\n\n' +
          'Para calcular χ necesitamos Φ. Para ello necesitaremos el coeficiente de imperfección (αLT)  = ' + this.pandeo[11] + '.\n' +
          'Además, necesitaremos la esbeltez adimensional, que se calcula con la fórmula que aparece en la parte derecha.\n\n' +
          'Ahora que hemos calculado la esbeltez adimensional, ya podremos calcular Φ.\n\n' +
          'Con esto, ya podemos aplicar la fórmula de χlt para calcularlo.'
          break
        case 5:
          this.nextPaso['resultado0'] = 'Mbrd = ' + this.pandeo[6] + ' kNm.'
          this.nextPaso['texto'] = 'Paso 6 Calcular Resistencia a la barra: \n\n' +
          'Una vez hemos calculado χlt, ya podemos calcular Mbrd.\n\n' +
          'Para eso necesitaremos Wy, que es un dato de la tabla del perfil seleccionado, en este caso ' + this.selected.name + '.\n' +
          'Y el Fyd conseguido con nuestro tipo de acero y su coeficiente.\n\n'
          break
        case 6:
          this.nextPaso['resultado0'] = 'Interacción = ' + this.pandeo[7] + '.'
          this.nextPaso['texto'] = 'Paso 7 Calcular interacción: \n\n' +
          'Una vez tenemos el resultado de Mbrd, simplemente tenemos que seguir la fórmula para hallar la interacción.\n\n' +
          'De nuevo, se debe comprobar que el resultado sea menor o igual que 1.\n'
          this.ocultar = true
          break
        case 7:
          this.nextPaso['resultado0'] = 'Lc lim = ' + this.pandeo[9] + 'm.'
          this.nextPaso['texto'] = 'Paso 8 Calcular Lc lim: \n\n' +
          'Para realizar este cálculo necesitamos Ned y C1, además del fy que viene dado por el tipo de acero. Son los 3 datos introducidos antes de la ejecución.\n' +
          'El resto de datos, son datos que son obtenidos de la tabla del perfil.\n\n' +
          'El resultado es una distancia en metros, que sirve para compararla con Lc'
          this.ocultar = false
          break
      }

      this.paso = this.paso + 1

      return false
    },
    getPasoAnterior: function () {
      if (this.selected.name !== '' && this.selected.coeficiente !== '' && this.selected.tipoAcero !== '') {
        this.paso = this.paso - 2
        this.getPasoSiguiente()
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
    border-spacing:1cm;
    border: 1px solid;
}
.supizq{
    float: left;
    width: 25%;
    text-align: left;
    margin-left: 30px;
    height: 550px;
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
  width: 200px;
  height: auto;
  margin-top: 5%;
  float: center;
}
.imagen2{
  width: 400px;
  height: auto;
  margin-top: 5%;
  float: center;
}
.centro{
  white-space:pre-line;
  background-color: aliceblue;
  text-align:center;
  height: 550px;
  margin: 10px;
  text-align: justify;
}
.formulas{
  width: 30%;
  height: 550px;
  background-color: aliceblue;
  float: right;
}
.tablaPerfiles{
  height: 470px;
  margin-top: 0px;
  float: center;
}
.boton{
  float: right;
}
.superior{
  background-color:aliceblue;
  height: 550px;
}
.curvaPandeo {
  width: 460px;
}
</style>
