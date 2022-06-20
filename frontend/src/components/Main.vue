<template>
  <div id="app" style="margin-top: 0px; margin-bottom: 0px;">
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
      <p></p>
      <form v-show="informacionIntroducida2">
        <p>Introduzca Ned y la clase:</p>
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
        <p>Introduzca Myed y la clase:</p>
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
        <p>Introduzca Mzed y la clase:</p>
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
        <p>Seleccione la clase de flexocompresión según la tabla:</p>
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
        <p>Introduzca Vyed:</p>
        <input
          v-model="selected.resVy"
          placeholder="VyEd"
        />
        <p>Introduzca Vzed:</p>
        <input
          v-model="selected.resVz"
          placeholder="VzEd"
        />
        <p></p>
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
      <h4>Formulas:</h4>
      <img
        id="imagenPaso3"
        src='../assets/TablaPerfiles.png'
        v-show="informacionIntroducida2"
        class="tablaPerfiles"
      />
      <img
        id="imagenPaso1"
        src='../assets/VistaRes/CalcularResMy1.png'
        v-if="this.paso===2"
        class="imagen"
      />
      <img
        id="imagenPaso2"
        src='../assets/VistaRes/CalcularResMz.png'
        v-if="this.paso===3"
        class="imagen"
      />
      <img
        id="imagenPaso1"
        src='../assets/VistaRes/CalcularResMy1.1.png'
        v-if="this.paso===2 || this.paso ===3"
        class="imagen"
      />
      <img
        id="imagenPaso5"
        src='../assets/VistaRes/InteraccionEC3.png'
        v-if="this.paso===5 && this.selected.clase !=='3'"
        class="imagen2"
      />
      <img
        id="imagenPaso1"
        src='../assets/VistaRes/CalcularVy.png'
        v-if="this.paso === 6"
        class="imagen"
      />
      <img
        id="imagenPaso6"
        src='../assets/VistaRes/InteraccionV.png'
        v-if="this.paso===8"
        class="imagen"
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
        src='../assets/VistaRes/CalcularResN.png'
        v-if="hover0 && this.paso!==1 || this.paso===1"
        class="imagen"
      />
      <img
        id="imagenPaso0"
        src='../assets/VistaRes/CalcularResN2.png'
        v-if="this.paso===1"
        class="imagen"
      />
      <img
        id="imagenPaso1"
        src='../assets/VistaRes/CalcularResMy2.png'
        v-if="hover1 && this.paso!==2 || this.paso===2"
        class="imagen"
      />
      <img
        id="imagenPaso2"
        src='../assets/VistaRes/CalcularResMz1.png'
        v-if="hover2 && this.paso!==3 || this.paso===3"
        class="imagen"
      />
      <img
        id="imagenPaso1"
        src='../assets/VistaRes/CalcularResMy2.2.png'
        v-if="this.paso===2 || this.paso ===3"
        class="imagen"
      />
      <img
        id="imagenPaso4"
        src='../assets/VistaRes/InteraccionCTE.png'
        v-if="this.paso===4 || this.selected.clase ==='3' && this.paso===5"
        class="imagen2"
      />
      <img
        id="imagenPaso5"
        src='../assets/VistaRes/InteraccionEC3.3.png'
        v-if="this.paso===5 && this.selected.clase !=='3'"
        class="imagen"
      />
      <img
        id="imagenPaso6"
        src='../assets/VistaRes/CalcularAvy.png'
        v-if="this.paso===6"
        class="imagen"
      />
      <img
        src='../assets/VistaRes/CalcularVz.png'
        v-if="hover6 && this.paso!==7 || this.paso===7"
        class="imagen"
      />
      <img
        id="imagenPaso6"
        src='../assets/VistaRes/InteraccionV.3.png'
        v-if="this.paso===8"
        class="imagen"
      />
      <br/>
      <img
        id="imagenPaso5"
        src='../assets/VistaRes/InteraccionEC3.4.png'
        v-if="this.paso===5 && this.selected.clase !=='3'"
        class="imagen2"
      />
      <img
        id="imagenPaso6"
        src='../assets/VistaRes/InteraccionV.2.png'
        v-if="this.paso===8"
        class="imagen"
      />
      <br>
      <img
        id="imagenPaso1"
        src='../assets/VistaRes/CalcularVy2.png'
        v-if="this.paso === 6 || this.paso === 7"
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
      <br/>
      <br/>
      <img
          src="../assets/TipoAcero.png"
          v-show="pantallaInicial"
        />
      <img
        src='../assets/VistaRes/TablaValoresAlphaBeta.png'
        v-if="this.paso===5 && this.selected.clase !=='3'"
      />
      <img
        src='../assets/VistaRes/InteraccionEC3.2.png'
        v-if="this.paso===5 && this.selected.clase !=='3'"
        class="imagen3"
      />
      <img
        src='../assets/VistaRes/InteraccionV.4.png'
        v-if="this.paso===8"
        class="imagen3"
      />
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
            <td></td>
            <td>Interaccion V:</td>
            <td>{{ resistencias[8] }}</td>
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
        this.paso = 0
        this.nextPaso['resultado0'] = ''
        this.nextPaso['resultado01'] = ''
        this.nextPaso['resultado1'] = ''
        this.nextPaso['resultado11'] = ''
        this.pantallaInicial = false
        this.ocultar = false
        this.ocultar2 = false
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
          'A continuación, debemos introducir las esfuerzos en las secciones y la clase correspondiente.\n' +
          'La clase viene dada por la tabla según el perfil. Además se debe introducir la clase a flexocompresión correspondiente.\n\n' +
          'Siguiendo la tabla, vemos que las casillas sombreadas significan que un perfil nunca podrá ser de esa clase y el asterisco indica ' +
          'que la sección no cambia para los valores de Ned superiores a esa clase.\n\n'
      }
      return false
    },
    cambioInformacion2: function () {
      if (this.selected.resN !== '' && this.selected.clase !== '' && this.selected.resMy !== '' && this.selected.resMz !== '') {
        this.informacionIntroducida2 = false
        this.informacionIntroducida3 = true
        this.paso = 0
        this.nextPaso['texto'] =
          'Los datos elegidos en el paso anterior se muestran en la tabla.\n\n' +
          'Ahora, debemos introducir los esfuerzos V en ambos ejes para poder iniciar la ejecución.\n'
      }
      return false
    },
    cambioInformacion3: function () {
      if (this.selected.resVy !== '' && this.selected.resVz !== '') {
        this.informacionIntroducida3 = false
        this.informacionIntroducida = false
        this.ocultar = true
        this.getResistencias()
        this.nextPaso['texto'] = 'Ahora que ya se han introducido todos los datos puedes ver los resultados en la tabla.\n\n' +
        'Para ver una ejecución por pasos utilice el botón siguiente, en caso de querer introducir nuevos datos rellene nuevamente el formulario.\n'
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
          Vyed: this.selected.resVy,
          Vzed: this.selected.resVz
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
      console.log(this.paso)
      switch (this.paso) {
        case 0:
          this.nextPaso['resultado0'] = 'Resistencia a esfuerzo axil = ' + this.resistencias[0] + ' kN.'
          this.nextPaso['texto'] = 'Paso 1 Calculo de resistencia a esfuerzo axil: \n\n' +
          'Para la realización de este cálculo, solo necesitaremos utilizar el Fy obtenido de la clase de acero y su coeficiente. \n' +
          'Además, la A es un valor que obtenemos de la tabla del perfil, que en este caso es: ' + this.selected.name + '\n\n' +
          'Una vez tenemos el resultado, tendríamos que compararlo con el Ned introducido previamente, ya que Ned debe ser menor o igual que dicho resultado.\n' +
          'Si esta condición no se cumple, el resultado estará resaltado en rojo en la tabla.\n'
          this.ocultar2 = false
          break
        case 1:
          this.nextPaso['resultado0'] = 'Resistencia a flexión en el eje y = ' + this.resistencias[1] + 'kN.'
          this.nextPaso['texto'] = 'Paso 2 Calculo de resistencia a flexión en el eje y: \n\n' +
          'En este caso, disponemos de dos formulas para calcular la resistencia. La superior para las clases 1 y 2, y la inferior para la clase 3.\n' +
          'En esta ejecución, nuestra clase es: ' + this.selected.clase + ', por lo que usamos la formula correspondiente.\n' +
          'La diferencia entre ambas fórmulas es si usamos el W elastico o el W plastico, que ambos son datos obtenidos del perfil.\n\n' +
          'De nuevo, comparamos el resultado con nuestro Myed introducido previamente.\n'
          this.ocultar2 = true
          break
        case 2:
          this.nextPaso['resultado0'] = 'Resistencia a flexión en el eje z = ' + this.resistencias[2] + 'kN.'
          this.nextPaso['texto'] = 'Paso 3 Calculo de resistencia a flexión en el eje z: \n\n' +
          'Como en el paso anterior, disponemos de dos formulas para calcular la resistencia. La superior para las clases 1 y 2, y la inferior para la clase 3.\n' +
          'En esta ejecución, nuestra clase es: ' + this.selected.clase + ', por lo que usamos la formula correspondiente.\n' +
          'La diferencia entre ambas fórmulas es si usamos el W elastico o el W plastico, que ambos son datos obtenidos del perfil.\n\n' +
          'De nuevo, comparamos el resultado con nuestro Myed introducido previamente.\n'
          break
        case 3:
          this.nextPaso['resultado0'] = 'La interacción según CTE: ' + this.resistencias[5] + '.'
          this.nextPaso['texto'] = 'Paso 4: Cálculo interacción según CTE\n\n' +
          'A continuación, veremos como se calcula la interacción. Para ello simplemente tendremos que seguir la formula, ' +
          'ya que todos los datos se han obtenido en pasos previos.\n'
          break
        case 4:
          if (this.selected.clase === '3') {
            this.nextPaso['resultado0'] = 'La interaccion según EC3: ' + this.resistencias[6] + '.'
            this.nextPaso['texto'] = 'Paso 5: Cálculo interac. cuando flexocompresión = 3\n\n' +
            'La interacción según EC3 es algo más compleja, ya que, dependiendo de la clase de flexocompresión introducida, la interacción variará.\n' +
            'En este caso la clase es 3, por lo que la fórmula sería la misma que usamos para CTE.\n'
          } else {
            this.nextPaso['resultado0'] = 'La interaccion según EC3: ' + this.resistencias[6] + '.'
            this.nextPaso['texto'] = 'Paso 5: Cálculo interac. cuando flexocompresión = 1 o 2\n\n' +
            'La interacción según EC3 es algo más compleja, ya que, dependiendo de la clase de flexocompresión introducida, la interacción variará.\n' +
            'En este caso la clase es ' + this.selected.clase + ', por lo que la fórmula sería distinta.\n' +
            'En este caso, necesitaremos primero hallar n y a para poder realizar las formulas.\n' +
            'Además, α y β se obtienen de la tabla inferior, dado que también son necesarios para el cálculo.'
          }
          break
        case 5:
          this.nextPaso['resultado0'] = 'La resistencia esfuerzo cortante para el eje y = ' + this.resistencias[3] + ' kN.'
          this.nextPaso['texto'] = 'Paso 6 Calculo de resistencia a esfuerzo cortante para el eje y: \n\n' +
          'Para la realización de esta fórmula, el único paso previo sería calcular Avy, ya que es el único dato que no obtenemos del perfil.\n' +
          'Una vez hemos calculado Avy, ya podemos utilizar la fórmula y obtener el resultado.\n\n' +
          'Como en el cálculo de las demás resistencias, será necesario realizar la misma comprobación.\n'
          break
        case 6:
          this.nextPaso['resultado0'] = 'La resistencia esfuerzo cortante para el eje z =  ' + this.resistencias[4] + ' kN.'
          this.nextPaso['texto'] = 'Paso 7 Calculo de resistencia a esfuerzo cortante para el eje z: \n\n' +
          'Al contrario que en el eje y, en este caso Avz viene dado por los datos del perfil, por lo que no serían necesarios cálculos previos.\n\n' +
          'Una vez más, se comprueba que este resultado sera mayor o igual que nuestro Vzed dado.\n'
          this.ocultar = true
          break
        case 7:
          this.nextPaso['resultado0'] = 'La interacción momento y cortante = ' + this.resistencias[8] + '.'
          this.nextPaso['texto'] = 'Paso 8 interacción momento y cortante: \n\n' +
          'Por último, para calcular la interacción en este caso será necesario encontrar p, para así calcular Mvrd.\n' +
          'Una vez obtenemos estos datos, hay que comprobar que Mvrd no sea mayor que Myrd.\n' +
          'Una vez realizada dicha comprobación, podemos aplicar la fórmula y obtener el resultado.\n\n' +
          'EXCEPCIÓN: Este cálculo no se realizara en caso de que Vzed <= 0.5 * Vzrd. \n'
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
  width: 320px;
  height: auto;
  margin-top: 5%;
  float: center;
}
.imagen3{
  width: 200px;
  height: auto;
  float: right;
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
</style>
