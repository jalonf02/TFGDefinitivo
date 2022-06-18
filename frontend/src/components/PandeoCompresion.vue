<template>
  <div id="app" style="margin-top: 10px">
    <h3 @mouseover="hover = true" @mouseleave="hover = false">
      Calculo de pandeo de barras a compresión
    </h3>
    <div class = "superior">
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
        <p>Introduzca L() m:</p>
        <input placeholder="L() m " v-model="selected.L" />
        <p>Introduzca βy y βz:</p>
        <input placeholder="βy" v-model="selected.By" />
        <input placeholder="βz" v-model="selected.Bz" />
        <p>Introduzca NEd:</p>
        <input placeholder="NEd" v-model="selected.resNecN" />
        <p>
          <button
            id="button-1"
            type="button"
            v-on:click="cambioInformacion2()"
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
      {{ nextPaso["resultado1"] }}
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
      <img
        id="imagenPaso0"
        src='../assets/TipoAcero.png'
        v-show="pantallaInicial"
      />
      <img
        id="imagenPaso2"
        src='../assets/CalculoLambdaRed2.png'
        v-show="this.paso===3"
      />
      <br/>
      <img
        id="imagenPaso0"
        src='../assets/CalcularChi2.png'
        v-show="this.paso===5"
        class="imagen2"
      />
    </div>
    </div>
    <p></p>
    <div class="abajo">
      <table class="table" id="tablaContenido">
        <thead>
          <tr>
            <th></th>
            <th @mouseover="hover0=true" @mouseleave="hover0 = false">Lₖ (mm)</th>
            <th @mouseover="hover1=true" @mouseleave="hover1 = false">λmec</th>
            <th @mouseover="hover2=true" @mouseleave="hover2 = false">λreducida</th>
            <th>curva</th>
            <th @mouseover="hover4=true" @mouseleave="hover4 = false">χ</th>
            <th @mouseover="hover5=true" @mouseleave="hover5 = false">Nb,Rd</th>
            <th @mouseover="hover6=true" @mouseleave="hover6 = false">interac.</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Eje Y</td>
            <td>{{ pandeo[0] }}</td>
            <td>{{ pandeo[2] }}</td>
            <td>{{ pandeo[4] }}</td>
            <td>{{ pandeo[6] }}</td>
            <td>{{ pandeo[8] }}</td>
            <td>{{ pandeo[10] }}</td>
            <td>{{ pandeo[12] }}</td>
          </tr>
          <tr>
            <td>Eje Z</td>
            <td>{{ pandeo[1] }}</td>
            <td>{{ pandeo[3] }}</td>
            <td>{{ pandeo[5] }}</td>
            <td>{{ pandeo[7] }}</td>
            <td>{{ pandeo[9] }}</td>
            <td>{{ pandeo[11] }}</td>
            <td>{{ pandeo[13] }}</td>
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
      hover0: false,
      hover1: false,
      hover2: false,
      hover4: false,
      hover5: false,
      hover6: false,
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
      pantallaInicial: true
    }
  },
  methods: {
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
        this.pantallaInicial = false
        this.ocultar = false
        this.ocultar2 = false
        this.pandeo = ''
        this.nextPaso['resultado0'] = ''
        this.nextPaso['resultado01'] = ''
        this.nextPaso['resultado1'] = ''
        this.nextPaso['resultado11'] = ''
        this.nextPaso['texto'] = 'El tipo de acero seleccionado es ' + this.selected.tipoAcero + '.\n' +
        'El coeficiente seleccionado es ' + this.selected.coeficiente + '.\n' +
        'El perfil seleccionado es ' + this.selected.name + '.\n\n' +
        'Ahora, para el cálculo de pandeo de barras a compresión será necesario añadir los siguientes valores: \n\n' +
        'Primero, debemos introducir tanto la longitud de la barra (L) en metros.' +
        ' Además, serán necesarios los coeficientes β tanto para el eje y como  para el eje x.\n ' +
        'Por último, se debe añadir el esfuerzo axil (NEd) en kN ya que será necesario para cáculos posteriores.'
      }
      return false
    },
    cambioInformacion2: function () {
      if (this.selected.restNecN !== '' && this.selected.L !== '' && this.selected.By !== '' && this.selected.Bz !== '') {
        this.informacionIntroducida = false
        this.informacionIntroducida2 = false
        this.paso = 0
        this.ocultar = true
        this.getPandeoCompresion()
        this.nextPaso['resultado0'] = ''
        this.nextPaso['resultado01'] = ''
        this.nextPaso['resultado1'] = ''
        this.nextPaso['resultado11'] = ''
        this.nextPaso['texto'] = 'La longitud de barra seleccionada es L = ' + this.selected.L + ' m.\n' +
        'El coeficiente β seleccionado para el eje y es ' + this.selected.By + '.\n' +
        'El coeficiente β seleccionado para el eje z es ' + this.selected.Bz + '.\n' +
        'El esfuerzo axil seleccionado para el eje z es Ned = ' + this.selected.resNecN + 'kN.\n\n' +
        'En la tabla inferior se muestran todos los resultados.\n' +
        'Para ver el proceso paso a paso utilice el boton siguiente.'
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
      console.log(this.paso)
      switch (this.paso) {
        case 0:
          this.nextPaso['resultado0'] = 'Lₖ para el eje y = ' + this.pandeo[0] + ' mm.'
          this.nextPaso['resultado1'] = 'Lₖ para el eje z = ' + this.pandeo[1] + ' mm.'
          this.nextPaso['texto'] = 'Paso 1: \n\n' +
          'Para calcular la resistencia a pandeo necesitaremos realizar diversos cálculos primero. \n' +
          'El primer paso sera calcular el valor de Lₖ en mm para ambos ejes.\n ' +
          'Para ello, utilizamos la formula que se muestra a la derecha, donde se utilizara el coeficiente β elegido para cada eje para calcular su Lₖ correspondiente.\n'
          this.ocultar2 = false
          break
        case 1:
          this.nextPaso['resultado0'] = 'λmec para el eje y = ' + this.pandeo[2] + '.'
          this.nextPaso['resultado1'] = 'λmec para el eje z = ' + this.pandeo[3] + '.'
          this.nextPaso['texto'] = 'Paso 2: \n\n' +
          'A continuación, calcularemos el valor de la Esbeltez mecánica.\n\n' +
          'Para realizar este calculoe es necesario el valor de Lₖ, calculado en el paso anterior y el valor i de cada eje, que se obtiene de la tabla del perfil seleccionado.'
          this.ocultar2 = true
          break
        case 2:
          this.nextPaso['resultado0'] = 'λreducida para el eje y = ' + this.pandeo[4] + '.'
          this.nextPaso['resultado1'] = 'λreducida para el eje z = ' + this.pandeo[5] + '.'
          this.nextPaso['texto'] = 'Paso 3: \n\n' +
          'Una vez hemos calculado la Esbeltez mecánica podemos calcular la esbeltez reducida.\n\n' +
          'En este caso, sería necesario realizar el cálculo previo de λE. Para ello se utiliza la formula mostrada en la parte inferior.\n' +
          'Una vez realizamos este calculo, utilizando la formula del apartado de formulas obtendriamos el resultado. ' +
          'Este resultado tiene que ser menor que 2 en ambos casos, en caso de no serlo, se deben introducir nuevos valores para satisfacer esta condición.'
          break
        case 3:
          this.nextPaso['resultado0'] = 'La curva de pandeo para el eje y es: ' + this.pandeo[6] + '.'
          this.nextPaso['resultado1'] = 'La curva de pandeo para el eje z es: ' + this.pandeo[7] + '.'
          this.nextPaso['texto'] = 'Paso 4:\n\n' +
          'En caso de que se cumpla la condición previa, ahora se elije la curva de pandeo.\n' +
          'La curva de pandeo depende del tipo de Acero elegido, que en este caso es ' + this.selected['tipoAcero'] +
          ' por lo que las curvas son las siguientes: \n'
          break
        case 4:
          this.nextPaso['resultado0'] = 'χ para el eje y = ' + this.pandeo[8] + '.'
          this.nextPaso['resultado1'] = 'χ para el eje z = ' + this.pandeo[9] + '.'
          this.nextPaso['texto'] = 'Paso 5: \n\n' +
          'Para calcular χ primero necesitamos el coeficiente de imperfección, que viene dado por la tabla inferior.\n' +
          'Una vez lo tengamos primero hayamos Φ siguiendo la formula, y con esto ya podemos calcular χ para ambos ejes.'
          break
        case 5:
          this.nextPaso['resultado0'] = 'Nb,Rd para el eje y = ' + this.pandeo[10] + ' kN.'
          this.nextPaso['resultado1'] = 'Nb,Rd para el eje z = ' + this.pandeo[11] + ' kN.'
          this.nextPaso['texto'] = 'Paso 6: \n\n' +
          'Ahora que ya hemos calculado χ podemos calcular la resistencia a pandeo.\n' +
          'Para realizar este calculo, además necesitaremos los datos elegidos al principio, dados por nuestra clase de acero ' + this.selected.tipoAcero +
          ' y por nuestro coeficiente ' + this.selected.coeficiente + '.'
          this.ocultar = true
          break
        case 6:
          this.nextPaso['resultado0'] = 'La interacción en el eje y = ' + this.pandeo[12] + '.'
          this.nextPaso['resultado1'] = 'La interacción en el eje z = ' + this.pandeo[13] + '.'
          this.nextPaso['texto'] = 'Paso 7: \n\n' +
          'Por último, para calcular la interacción y verificar que todo es correcto necesitamos que el resultado sea menor que 1.\n' +
          'Para esta formula utilizaremos el esfuerzo axil (Ned) ' + this.selected.resNecN + ' kN.\n' +
          'Con esto podemos calcular la intearacción y verificar que el resultado es correcto.'
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
    border-spacing:2cm;
    border: 1px solid;
}
.supizq{
    float: left;
    width: 25%;
    text-align: left;
    margin-left: 30px;
    height: 400px;
    background-color: azure;
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
  background-color: aqua;
  float: right;
}
.curvaPandeo{
  width: 420px;
}
.boton{
  float: right;
}
</style>
