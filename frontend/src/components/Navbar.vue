<template>
    <div class="navbar">
        <div class="navLink">
            <a href="/">Calculo Resistencias</a>
            <a href="PandeoLateral">Pandeo Lateral</a>
            <a href="PandeoCompresion">Pandeo de barras a compresión</a>
        </div>
    </div>
</template>
<script>
export default {
  name: 'Navbar'
}
</script>
<style scoped>
.navbar{
    background: grey;
    padding: 1rem;
    font-size: 1.5rem;
    border-bottom: 1px solid white;
}
.navLink{
text-align: center;
}
a{
    text-decoration: none;
    padding: 1rem;
    color:#fff;
    text-align: center;
}
@media only screen and (max-width: 600px) {
    .navLink{
        display: flex;
        flex-direction: column;
    }
}
</style>
