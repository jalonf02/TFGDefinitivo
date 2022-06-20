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
        <p></p>
        <button
          id="button-2"
          type="button"
          v-on:click="cambioInformacion4()"
          variant="dark"
        >
          Iniciar
        </button>
        </form>
        <form v-show="informacionIntroducida5">
      <p>Introduzca el valor de Cmy:</p>
        <input placeholder="C₁" v-model="selected.Cmy" />
      <p>Introduzca el valor de Cmz:</p>
        <input placeholder="C₁" v-model="selected.Cmz" />
      <p>Introduzca el valor de Cmlt:</p>
        <input placeholder="βₗₜ" v-model="selected.Cmlt" />
        <p></p>
        <button
          id="button-2"
          type="button"
          v-on:click="cambioInformacion5()"
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
          src="../assets/CurvaPandeo.png"
          v-show="this.paso === 4"
          class="curvaPandeo"
        />
        <br />
        <img
          id="imagenPaso0"
          src="../assets/CalculoFyD.png"
          v-show="pantallaInicial"
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
        <br/><br/>
        <img
          id="imagenPaso0"
          src="../assets/TipoAcero.png"
          v-show="pantallaInicial"
        />
      </div>
    </div>
    <div class="abajo">
      <table class="table" id="tablaContenido">
        <thead>
          <tr>
            <th></th>
            <th @mouseover="hover0 = true" @mouseleave="hover0 = false">
              interac. CTE
            </th>
            <th @mouseover="hover1 = true" @mouseleave="hover1 = false">
              interac EC3
            </th>
            <th @mouseover="hover2 = true" @mouseleave="hover2 = false">
              interac. Pandeo y
            </th>
            <th>interac. Pandeo z</th>
            <th @mouseover="hover4 = true" @mouseleave="hover4 = false">interac. PL</th>
            <th @mouseover="hover5 = true" @mouseleave="hover5 = false">
              interac. x
            </th>
            <th @mouseover="hover6 = true" @mouseleave="hover6 = false">
              interac. y
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Interacciones</td>
            <td>{{ interaccion['interacCTE'] }}</td>
            <td>{{ interaccion['interacEC3'] }}</td>
            <td>{{ interaccion['interacy'] }}</td>
            <td>{{ interaccion['interacz'] }}</td>
            <td>{{ interaccion['interacPL'] }}</td>
            <td>{{ interaccion['interacFinalz'] }}</td>
            <td>{{ interaccion['interacFinaly'] }}</td>
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
      hover0: false,
      hover1: false,
      hover2: false,
      hover4: false,
      hover5: false,
      hover6: false,
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
        this.nextPaso['texto'] = 'El tipo de acero seleccionado es ' + this.selected.tipoAcero + '.\n' +
        'El coeficiente seleccionado es ' + this.selected.coeficiente + '.\n' +
        'El perfil seleccionado es ' + this.selected.name + '.\n\n'
      }
      return false
    },
    cambioInformacion2: function () {
      if (this.selected.resN !== '' && this.selected.clase !== '' && this.selected.resMy !== '' && this.selected.resMz !== '') {
        this.informacionIntroducida2 = false
        this.informacionIntroducida3 = true
        this.nextPaso['texto'] = 'Texto de prueba 2.'
      }
      return false
    },
    cambioInformacion3: function () {
      if (this.selected.L !== '' && this.selected.By !== '' && this.selected.Bz !== '') {
        this.informacionIntroducida3 = false
        this.informacionIntroducida4 = true
        this.nextPaso['texto'] = 'Texto de prueba 3.'
      }
      return false
    },
    cambioInformacion4: function () {
      if (this.selected.L !== '' && this.selected.By !== '' && this.selected.Bz !== '') {
        this.informacionIntroducida4 = false
        this.informacionIntroducida5 = true
        this.nextPaso['texto'] = 'Texto de prueba 4.'
      }
      return false
    },
    cambioInformacion5: function () {
      if (this.selected.Cmy !== '' && this.selected.Cmz !== '' && this.selected.Cmlt !== '') {
        this.informacionIntroducida5 = false
        this.informacionIntroducida = false
        this.ocultar = true
        this.getInteraccion()
        this.nextPaso['texto'] = 'Texto de prueba 5.'
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
