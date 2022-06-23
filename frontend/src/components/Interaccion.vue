<template>
  <div id="app" style="margin-top: 0px; margin-bottom: 0px;">
    <div class = "superior">
    <h3 style="margin-bottom: 0px;">Interaccion de esfuerzos en barra</h3>
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
          v-model="selected.Ned"
          placeholder="Ned"
        />
        <select v-model="selected.claseN">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
        </select>
        <p>Introduzca Myed y la clase:</p>
        <input
          v-model="selected.Myed"
          placeholder="Myed"
        />
        <select v-model="selected.claseMy">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
        </select>
        <p>Introduzca Mzed y la clase:</p>
        <input
          v-model="selected.Mzed"
          placeholder="Mzed"
        />
        <select v-model="selected.claseMz">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
        </select>
        <p>Seleccione la clase de flexocompresión:</p>
        <select v-model="selected.clase">
          <option>1</option>
          <option>2</option>
          <option>3</option>
        </select>
        <p>
        <button
          id="button-2"
          type="button"
          v-on:click="cambioInformacion2()"
          variant="dark"
        >
          Introducir Datos
        </button>
        </p>
      </form>
      <form v-show="informacionIntroducida3">
          <p>Introduzca L() m:</p>
          <input placeholder="L() m " v-model="selected.L" />
          <p>Introduzca βy y βz:</p>
          <input placeholder="βy" v-model="selected.By" />
          <input placeholder="βz" v-model="selected.Bz" />
          <p>
            <button
              id="button-1"
              type="button"
              v-on:click="cambioInformacion3()"
              variant="dark"
            >
              Introducir Datos
            </button>
          </p>
        </form>
        <form v-show="informacionIntroducida4">
      <p>Introduzca el valor de k₂:</p>
      <select v-model="selected.k2">
        <option>0.7</option>
        <option>1</option>
        <option>1.3</option>
      </select>
      <p>Introduzca el valor de C₁ deseado según la tabla:</p>
        <input placeholder="C₁" v-model="selected.C1" />
      <p>Introduzca el valor de βₗₜ, por defecto será 1:</p>
        <input placeholder="βₗₜ" v-model="selected.Blt" />
        <p>
        <button
          id="button-2"
          type="button"
          v-on:click="cambioInformacion4()"
          variant="dark"
        >
          Introducir Datos
        </button>
        </p>
        </form>
        <form v-show="informacionIntroducida5">
      <p>Introduzca el valor de Cmy:</p>
        <input placeholder="C₁" v-model="selected.Cmy" />
      <p>Introduzca el valor de Cmz:</p>
        <input placeholder="C₁" v-model="selected.Cmz" />
      <p>Introduzca el valor de Cmlt:</p>
        <input placeholder="βₗₜ" v-model="selected.Cmlt" />
        <p>
        <button
          id="button-2"
          type="button"
          v-on:click="cambioInformacion5()"
          variant="dark"
        >
          Iniciar
        </button>
        </p>
        </form>
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
            <div class="formulas">
        <h4>Formulas:</h4>
        <img
        id="Tabla"
        src='../assets/TablaPerfiles.png'
        v-show="informacionIntroducida2"
        class="tablaPerfiles"
        />
        <img
          id="TablaC1"
          src="../assets/VistaPL/TablaC1.png"
          v-show="informacionIntroducida4"
          class = "tablaPerfiles"
        />
        <img
          id="TablaCmi"
          src="../assets/VistaInteracciones/TablaCmi.png"
          v-show="informacionIntroducida5"
          class = "coeficientesK"
        />
        <img
          id="imagenPaso1.1"
          src="../assets/VistaInteracciones/CoeficientesK1.png"
          v-show="this.paso === 1"
          class="coeficientesK"
        />
        <img
          id="imagenPaso1.2"
          src="../assets/VistaInteracciones/CoeficientesK2.png"
          v-show="this.paso === 2"
          class="coeficientesK"
        />
        <img
          id="imagenPaso2"
          src="../assets/VistaInteracciones/InteraccionY.png"
          v-show="this.paso === 3"
          class="imagen2"
        />
        <br />
        <img
          id="imagenInicial"
          src="../assets/CalculoFyD.png"
          v-show="pantallaInicial"
          class="imagen"
        />
        <img
          id="imagenPaso2"
          src="../assets/VistaInteracciones/InteraccionZ.png"
          v-show="this.paso === 3"
          class="imagen2"
        />
      </div>
      <div class="centro">
        <h4 class="titulo">Desarrollo paso a paso</h4>
        {{ nextPaso["texto"] }}
        {{ nextPaso["resultado0"] }}
        {{ nextPaso["resultado1"] }}
        <br/><br/>
        <img
          id="imagenPaso0"
          src="../assets/TipoAcero.png"
          v-show="pantallaInicial"
        />
        <img
          id="imagenPaso0"
          src="../assets/VistaPL/TablaK2.png"
          v-show="informacionIntroducida4"
        />
      </div>
    </div>
    <div class="abajo">
      <table class="table" id="tablaContenido">
        <thead>
          <tr>
            <th>{{selected.name}}</th>
            <th>
              interac. secciones CTE
            </th>
            <th>
              interac. secciones EC3
            </th>
            <th>
              interac. Pandeo y
            </th>
            <th>interac. Pandeo z</th>
            <th>interac. PL</th>
            <th>
              interac. en barras z
            </th>
            <th>
              interac. en barras y
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Interacciones (EC3)</td>
            <td v-bind:style="1 < interaccion['interacCTE'] ? 'color: red':'' ">{{ interaccion['interacCTE'] }}</td>
            <td v-bind:style="1 < interaccion['interacEC3'] ? 'color: red':'' ">{{ interaccion['interacEC3'] }}</td>
            <td v-bind:style="1 < interaccion['interacy'] ? 'color: red':'' ">{{ interaccion['interacy'] }}</td>
            <td v-bind:style="1 < interaccion['interacz'] ? 'color: red':'' ">{{ interaccion['interacz'] }}</td>
            <td v-bind:style="1 < interaccion['interacPL'] ? 'color: red':'' ">{{ interaccion['interacPL'] }}</td>
            <td v-bind:style="1 < interaccion['interacFinalz'] ? 'color: red':'' ">{{ interaccion['interacFinalz'] }}</td>
            <td v-bind:style="1 < interaccion['interacFinaly'] ? 'color: red':'' ">{{ interaccion['interacFinaly'] }}</td>
          </tr>
          <tr>
            <td>Datos</td>
            <td>Kyy</td>
            <td>Kyz</td>
            <td>Kzy</td>
            <td>Kzz</td>
            <td>Cm,y</td>
            <td>Cm,z</td>
            <td>Cm,LT</td>
          </tr>
          <tr>
            <td></td>
            <td>{{ interaccion['Kyy'] }}</td>
            <td>{{ interaccion['Kyz'] }}</td>
            <td>{{ interaccion['Kzy'] }}</td>
            <td>{{ interaccion['Kzz'] }}</td>
            <td>{{ this.selected.Cmy }}</td>
            <td>{{ this.selected.Cmz }}</td>
            <td>{{ this.selected.Cmlt }}</td>
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
        Ned: '',
        Myed: '',
        Mzed: '',
        L: '',
        By: '',
        Bz: '',
        Blt: '',
        C1: '',
        clase: '',
        claseN: '',
        claseMy: '',
        claseMz: '',
        k2: '',
        Cmy: '',
        Cmz: '',
        Cmlt: ''
      },
      imagen: '',
      interaccion: [],
      excel: {},
      excel2: {},
      excel3: {},
      nextPaso: [],
      paso: 0,
      informacionIntroducida: false,
      ocultar: false,
      ocultar2: false,
      informacionIntroducida2: false,
      informacionIntroducida3: false,
      informacionIntroducida4: false,
      informacionIntroducida5: false,
      pantallaInicial: true,
      pandeo: []
    }
  },
  methods: {
    cambioInformacion: function () {
      if (this.selected.name !== '' && this.selected.coeficiente !== '' && this.selected.tipoAcero !== '') {
        this.informacionIntroducida = true
        this.informacionIntroducida2 = true
        this.pantallaInicial = false
        this.ocultar = false
        this.ocultar2 = false
        this.interaccion = ''
        this.paso = 0
        this.nextPaso['resultado0'] = ''
        this.nextPaso['resultado01'] = ''
        this.nextPaso['resultado1'] = ''
        this.nextPaso['resultado11'] = ''
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
          'A continuación, debemos introducir los esfuerzos en las secciones y la clase correspondiente.\n\n' +
          'La clase viene dada por la tabla según el perfil. Además se debe introducir la clase a flexocompresión correspondiente.\n\n' +
          'Siguiendo la tabla, vemos que las casillas sombreadas significan que un perfil nunca podrá ser de esa clase y el asterisco indica ' +
          'que la sección no cambia para los valores de Ned superiores a esa clase.\n\n'
      }
      return false
    },
    cambioInformacion2: function () {
      let aux1 = this.selected.Ned.replace(/,/g, '.')
      let aux2 = this.selected.Myed.replace(/,/g, '.')
      let aux3 = this.selected.Mzed.replace(/,/g, '.')
      if ((this.selected.Ned !== '' && !isNaN(aux1)) && this.selected.clase !== '' && (this.selected.Myed !== '' && !isNaN(aux2)) &&
      (this.selected.Mzed !== '' && !isNaN(aux3))) {
        this.informacionIntroducida2 = false
        this.informacionIntroducida3 = true
        this.nextPaso['texto'] = 'Ahora, para el cálculo de pandeo de barras a compresión será necesario añadir los siguientes valores: \n\n' +
        'Primero, debemos introducir tanto la longitud de la barra (L) en metros.' +
        ' Además, serán necesarios los coeficientes β tanto para el eje y como  para el eje x.\n '
      } else {
        this.$alert('Valores introducidos incorrectos.')
      }
      return false
    },
    cambioInformacion3: function () {
      let aux1 = this.selected.L.replace(/,/g, '.')
      let aux2 = this.selected.By.replace(/,/g, '.')
      let aux3 = this.selected.Bz.replace(/,/g, '.')
      if ((this.selected.L !== '' && !isNaN(aux1)) && (this.selected.By !== '' && !isNaN(aux2)) && (this.selected.Bz !== '' && !isNaN(aux3))) {
        this.informacionIntroducida3 = false
        this.informacionIntroducida4 = true
        this.nextPaso['texto'] = 'A continuación, será necesario introducir los valores de k₂, C₁, βₗₜ.\n\n' +
        'k₂ dependerá de la posición de la carga en la viga, como se indica en la tabla mostrada.\n\n' +
        'C₁ es un coeficiente que se debe elegir según la tabla. Su valor por defecto será 1.0.\n\n' +
        'βₗₜ es un parametro adimensional, su valor por defecto será 1.0.\n\n'
      } else {
        this.$alert('Valores introducidos incorrectos.')
      }
      return false
    },
    cambioInformacion4: function () {
      let aux1 = this.selected.C1.replace(/,/g, '.')
      let aux2 = this.selected.Blt.replace(/,/g, '.')
      if ((this.selected.C1 !== '' && !isNaN(aux1)) && (this.selected.Blt !== '' && !isNaN(aux2)) && this.selected.k2 !== '') {
        this.informacionIntroducida4 = false
        this.informacionIntroducida5 = true
        this.nextPaso['texto'] = 'Por último, se deben introducir los valores Cm,i.\n\n' +
        'Estos valores no pueden ser superiores a 1, ni inferiores a 0.4.\n\n'
      } else {
        this.$alert('Valores introducidos incorrectos.')
      }
      return false
    },
    cambioInformacion5: function () {
      let aux1 = this.selected.Cmy.replace(/,/g, '.')
      let aux2 = this.selected.Cmz.replace(/,/g, '.')
      let aux3 = this.selected.Cmlt.replace(/,/g, '.')
      aux1 = parseFloat(aux1)
      aux2 = parseFloat(aux2)
      aux3 = parseFloat(aux3)
      if ((this.selected.Cmy !== '' && aux1 >= 0.4 && aux1 <= 1.0) && (this.selected.Cmz !== '' && aux2 >= 0.4 && aux2 <= 1.0) &&
        (this.selected.Cmlt !== '' && aux3 >= 0.4 && aux3 <= 1.0)) {
        this.informacionIntroducida5 = false
        this.informacionIntroducida = false
        this.ocultar = true
        this.getInteraccion()
        this.nextPaso['texto'] = 'Ahora que ya se han introducido todos los datos, puedes ver los resultados en la tabla.\n\n' +
        'Para ver una ejecución por pasos utilice el botón siguiente, en caso de querer introducir nuevos datos rellene nuevamente el formulario.\n'
      } else {
        this.$alert('Recuerde que estos valores no pueden ser superiores a 1, ni inferiores a 0.4.')
      }
      return false
    },
    getInteraccion: function () {
      const path = 'http://127.0.0.1:5000/Interaccion'
      axios.post(path, {
        name: this.selected.name,
        coeficiente: this.selected.coeficiente,
        tipoAcero: this.selected.tipoAcero,
        L: this.selected.L,
        By: this.selected.By,
        Bz: this.selected.Bz,
        Ned: this.selected.Ned,
        Myed: this.selected.Myed,
        Mzed: this.selected.Mzed,
        Blt: this.selected.Blt,
        C1: this.selected.C1,
        clase: this.selected.clase,
        k2: this.selected.k2,
        Cmy: this.selected.Cmy,
        Cmz: this.selected.Cmz,
        Cmlt: this.selected.Cmlt
      }
      )
        .then(body => {
          this.interaccion = body.data
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
          this.nextPaso['texto'] = 'El primer paso seria seleccionar en los desplegables el tipo de acero y su coeficiente.\n\n' +
          'Además, se deberá indicar con que perfil se desea realizar los cálculos.\n\n' +
          'Si desea introducir valores decimales utilice el punto en lugar de la coma.'
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
      console.log(this.paso)
      switch (this.paso) {
        case 0:
          this.nextPaso['resultado0'] = 'Coeficiente Kyy = ' + this.interaccion['Kyy'] + '.'
          this.nextPaso['resultado1'] = 'Coeficiente Kzz = ' + this.interaccion['Kzz'] + '.'
          this.nextPaso['texto'] = 'Paso 1.1 Coeficientes K: \n\n' +
          'En este paso calcularemos los coeficientes Kyy y Kzz. \n' +
          'Para ello, necesitaremos saber la clase introducida según la tabla, que en este caso es ' + this.selected.clase + '.\n ' +
          'Una vez sabemos la clase, podemos seguir las formulas mostradas para hallar Kyy y Kzz.\n\n' +
          'Ned, Cmy, Cmz y Cmlt son datos introducidos previamente.\n' +
          'Por otro lado, necesitaremos también la esbeltez reducida para ambos ejes y el Nb,rd de ambos ejes también.\n' +
          'En caso de querer comprobar como se obtienen, puedes regresar al apartado de pandeo por compresión.\n\n'
          this.ocultar2 = false
          break
        case 1:
          this.nextPaso['resultado0'] = 'Coeficiente Kyz = ' + this.interaccion['Kyz'] + '.'
          this.nextPaso['resultado1'] = 'Coeficiente Kzy = ' + this.interaccion['Kzy'] + '.'
          this.nextPaso['texto'] = 'Paso 1.2 Coeficientes K: \n\n' +
          'En este paso calcularemos los coeficientes Kyz y Kzy. \n' +
          'Para ello, necesitaremos saber la clase introducida según la tabla, que en este caso es ' + this.selected.clase + '.\n ' +
          'Una vez sabemos la clase, podemos seguir las formulas mostradas para hallar Kyz y Kzy.\n\n' +
          'Ned, Cmy, Cmz y Cmlt son datos introducidos previamente.\n' +
          'Por otro lado, necesitaremos también la esbeltez reducida para ambos ejes y el Nb,rd de ambos ejes también.\n' +
          'En caso de querer comprobar como se obtienen, puedes regresar al apartado de pandeo por compresión.\n\n'
          this.ocultar2 = true
          this.ocultar = true
          break
        case 2:
          this.nextPaso['resultado1'] = 'Pandeo en el plano debil (x-y) del perfil (eje z) = ' + this.interaccion['interacFinalZ'] + '.'
          this.nextPaso['resultado0'] = 'Pandeo en el plano fuerte (x-z) del perfil (eje y) = ' + this.interaccion['interacFinalY'] + '.'
          this.nextPaso['texto'] = 'Paso 2 Calculo pandeo en el plano debil y fuerte del perfil: \n\n' +
          'Una vez hemos calculado todos los coeficientes K, podemos calcular las interacciones.\n\n' +
          'Para ello, utilizaremos la formula correspondiente.\n' +
          'Los dividendos son datos introducidos en el programa previamente.\n' +
          'Por otro lado, los divisores, son datos que hemos calculado en los otros apartados, para ver su paso a paso compruebe en el apartado respectivo.\n\n' +
          'El Nb,Rd lo hayamos en el pandeo lateral, y el Nb,Rd para cada eje es calculado en el pandeo por compresion.\n' +
          'Por último, la resistencia a flexión en el eje z se calcula en el apartado de resistencias.\n\n'
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
    border-spacing:1.2cm;
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
  width: 60%;
  height: auto;
  margin-top: 5%;
  float: center;
}
.imagen2{
  width: 60%;
  height: auto;
  margin-top: 5%;
  float: center;
}
.imagen3{
  width: 60%;
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
  max-height: 88%;
  max-width: auto;
  margin-top: 0px;
  float: center;
}
.coeficientesK{
  max-width: 94%;
  max-width: auto;
  margin-top: 0px;
  float: center;
}
.boton{
  float: right;
  margin-right: 100px;
}
.superior{
  background-color:aliceblue;
  height: 550px;
}
</style>
